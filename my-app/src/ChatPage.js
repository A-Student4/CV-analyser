// In src/ChatPage.js

import React, { useState } from 'react';
import Sidebar from './Sidebar';
import ChatWindow from './ChatWindow';
import ChatInput from './ChatInput';
import AnalysisForm from './AnalysisForm';
import './App.css';

// This helper function transforms the API response into chat messages
function transformAnalysisToMessages(apiResponse) {
  const messages = [];
  messages.push({
    id: 'summary_intro',
    sender: 'ai',
    text: `Analysis complete! Your initial match score is ${apiResponse.match_score}%. Here's the overall summary:`
  });
  messages.push({
    id: 'summary_text',
    sender: 'ai',
    text: apiResponse.analysis_summary
  });
  if (apiResponse.suggested_improvements?.length > 0) {
    messages.push({
      id: 'improvements_intro',
      sender: 'ai',
      text: "Here are my specific suggestions to strengthen your CV:"
    });
    apiResponse.suggested_improvements.forEach((suggestion, index) => {
      const suggestionText = `**Original Text:** "${suggestion.original_text}"\n\n**Suggested Text:** "${suggestion.suggested_text}"\n\n**Reason:** ${suggestion.improvement_reason}`;
      messages.push({ id: `suggestion_${index}`, sender: 'ai', text: suggestionText });
    });
  }
   messages.push({
    id: 'closing_remarks',
    sender: 'ai',
    text: apiResponse.closing_remarks
  });
  return messages;
}


const ChatPage = () => {
  // This is the single source of truth for the entire conversation
  const [messages, setMessages] = useState([]);
  
  // This state variable controls what the user sees
  const [appState, setAppState] = useState('initial'); // 'initial', 'loading', 'analysed'
  const [error, setError] = useState(null); 

  // This function handles the INITIAL form submission from AnalysisForm.js
  const handleAnalysisSubmit = async ({ cvFile, jobLink, prompt }) => {
    setAppState('loading'); // Show the loading indicator
    setMessages([]); // Clear any previous messages

    const formData = new FormData();
    formData.append('cv_file', cvFile);
    formData.append('job_link', jobLink);
    formData.append('initial_prompt', prompt);

    try {
      const response = await fetch("http://127.0.0.1:8000/analyse", {
        method: "POST",
        body: formData,
      });

      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(JSON.stringify(errorData.detail, null, 2));
      }

      const result = await response.json();
      const formattedMessages = transformAnalysisToMessages(result);
      setMessages(formattedMessages);
      setAppState('analysed'); // Switch to the chat view

    } catch (error) {
      alert("Failed to analyze CV: \n" + error.message);
      setAppState('initial'); // Go back to the initial form on error
    }
  };
  
  // This function handles subsequent messages from ChatInput.js
  const handleSendMessage = async (userMessage) => {
    const newUserMessage = { id: Date.now(), sender: 'user', text: userMessage };
    const updatedMessages = [...messages, newUserMessage];
    setMessages(updatedMessages);

    
    setAppState('loading'); // Use appState to show loading for chat responses too

    try {
        const response = await fetch("http://127.0.0.1:8000/chat", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                message: userMessage,
                history: updatedMessages // Send the whole history for context
            })
        });
          if (!response.ok) {
            const errorData = await response.json();
            // Create a detailed error message from the backend's response
            throw new Error(JSON.stringify(errorData.detail || 'The server returned an error.', null, 2));
        }
        // ... handle response and errors ...
        const result = await response.json();
        const aiResponseMessage = { id: Date.now() + 1, sender: 'ai', text: result.ai_response };
        setMessages(prev => [...prev, aiResponseMessage]);

      } catch (err) {
        // --- This is our "safety net" ---
        console.error("Failed to send message:", err);
        setError(err.message); // Store the error message to display to the user
    
    
      } finally {
        setAppState('analysed');
    }
  };

  return (
    <div className="chat-page-container">
      <Sidebar />
      <div className="main-content">
        <header className="chat-header">
          <h1>CV Analyser</h1>
        </header>
          {/* Display the error message if it exists */}
  {error && (
    <div className="error-message">
      <p>Sorry, an error occurred:</p>
      <pre>{error}</pre>
    </div>
  )}
        
        {/* The ChatWindow now only shows messages. It doesn't care about the app's state. */}
        <ChatWindow messages={messages} isLoading={appState === 'loading'} />

        {/* --- CONDITIONAL RENDERING --- */}
        {/* We use appState to decide which input component to show at the bottom */}
        {appState === 'initial' && <AnalysisForm onSubmit={handleAnalysisSubmit} isLoading={appState === 'loading'} />}
        
        {appState === 'analysed' && <ChatInput onSendMessage={handleSendMessage} disabled={appState === 'loading'} />}
      </div>
    </div>
  );
};

export default ChatPage;