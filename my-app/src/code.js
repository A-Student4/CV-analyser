import React, { useEffect, useState } from "react";
import './App.css';

import { IoPaperPlaneOutline } from "react-icons/io5";


const CVAnalyser = () => {

  const [prompt, setPrompt] = useState("");
  // Add a new state for the job link input
  const [jobLink, setJobLink] = useState("");
  const [data, setData] = useState(null);

  useEffect(() => {
    // Fetch data from the backend when the component mounts
    fetch('/ExamplePOSTOutput.json')
      .then((response) => response.json()) // Parse the JSON response and return it
      .then((data) => setData(data)) // Set the fetched data to state
      .catch((error) => console.error("Error fetching data:", error));
  }, []);

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!prompt.trim() && !jobLink.trim()) return; // Don't submit if both are empty
    alert(`Job Link: ${jobLink}\nMessage: ${prompt}`);
    setPrompt(""); // Clear the input after sending
  };



  return (
    <div className="app-container">
      <header className="chat-header">
        <h1>CV Analyser</h1>
      </header>
      <div className="chat-widget">
        <p>{data ? data.match_score : "Loading..."}</p>
      </div>

      <main className="chat-interface">
        {/* Chat messages will appear here */}
      </main>

      <footer className="input-area">
        <form className="chat-input-form" onSubmit={handleSubmit}>
          {/* The "Add" and "Tools" buttons are replaced with these: */}
          
          {/* 1. New "Upload CV" button */}
          <button type="button" className="action-button">
            Upload CV
          </button>

          {/* 2. New "Job Link" input box */}
          <input
            type="text"
            placeholder="Paste Job Link..."
            className="job-link-input"
            value={jobLink}
            onChange={(e) => setJobLink(e.target.value)}
          />
          
          <textarea
            placeholder="Message..."
            className="input-field"
            value={prompt}
            onChange={(e) => setPrompt(e.target.value)}
            onKeyDown={(e) => {
              if (e.key === 'Enter' && !e.shiftKey) {
                e.preventDefault();
                handleSubmit(e);
              }
            }}
          />

          <button type="submit" className="send-button">
            <IoPaperPlaneOutline size={24} />
          </button>
        </form>
      </footer>
    </div>
  );
}

export default CVAnalyser;