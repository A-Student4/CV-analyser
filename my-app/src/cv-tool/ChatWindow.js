// In src/ChatWindow.js

import React from 'react';
import Message from './Message';

const ChatWindow = ({ messages }) => {
  // We will also add a loading indicator for when the AI is 'thinking'
  // For now, it will be based on mock data in ChatPage.js

  return (
    <main className="chat-window">
      {messages.map((msg) => (
        <Message key={msg.id} message={msg} />
      ))}
      {/* We can format the loading indicator here later */}
    </main>
  );
};

export default ChatWindow;