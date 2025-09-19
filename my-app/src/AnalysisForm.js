// In src/AnalysisForm.js

import React, { useState } from 'react';
import { IoPaperPlaneOutline } from 'react-icons/io5';

const AnalysisForm = ({ onSubmit, isLoading }) => {
  const [prompt, setPrompt] = useState("");
  const [jobLink, setJobLink] = useState("");
  const [cvFile, setCvFile] = useState(null);

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!cvFile || !jobLink.trim()) {
      alert("Please provide a CV file and a job link.");
      return;
    }
    onSubmit({ cvFile, jobLink, prompt });
  };

  return (
    <footer className="input-area">
      <form className="chat-input-form" onSubmit={handleSubmit}>
        <label className="action-button" style={{ cursor: "pointer" }}>
          {cvFile ? cvFile.name : 'Upload CV'}
          <input
            type="file"
            accept=".pdf"
            onChange={(e) => setCvFile(e.target.files[0])}
            style={{ display: "none" }}
            disabled={isLoading}
          />
        </label>
        <input
          type="text"
          placeholder="Paste Job Link..."
          className="job-link-input"
          value={jobLink}
          onChange={(e) => setJobLink(e.target.value)}
          disabled={isLoading}
        />
        <textarea
          placeholder="Optional: Add extra info..."
          className="input-field"
          value={prompt}
          onChange={(e) => setPrompt(e.target.value)}
          disabled={isLoading}
        />
        <button type="submit" className="send-button" disabled={isLoading}>
          <IoPaperPlaneOutline size={24} />
        </button>
      </form>
    </footer>
  );
};

export default AnalysisForm;