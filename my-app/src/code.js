import React, { useEffect, useState } from "react";
import './App.css';

import { IoPaperPlaneOutline } from "react-icons/io5";


const CVAnalyser = () => {

  const [prompt, setPrompt] = useState("");
  // Add a new state for the job link input
  const [jobLink, setJobLink] = useState("");
  const [data, setData] = useState(null);
  const [cvFile, setCvFile] = useState(null); // State to hold the uploaded CV file

  useEffect(() => {
    // Fetch data from the backend when the component mounts
    fetch('/ExamplePOSTOutput.json')
      .then((response) => response.json()) // Parse the JSON response and return it
      .then((data) => setData(data)) // Set the fetched data to state
      .catch((error) => console.error("Error fetching data:", error));
  }, []);



  //Making a new button for uploading CV PDF
  const handleFileChange = (e) => { // Handle file input change
    setCvFile(e.target.files[0]);// Store the selected file in state
  };
  // File input element will be rendered in the JSX below

  // Use the existing handleSubmit function for form submission and link it to CV upload and Job link 
  // Use form data to send the CV file and job link to the backend
  // Make the POST request to the backend with the CV file and job link
  const handleSubmit = async (e) => { 
    e.preventDefault(); // Prevent the default form submission behavior which refreshes the page 
    if (!jobLink.trim() || !cvFile) {// Don't submit if all are empty
    alert("Please provide a CV and No file uploaded");
    return;
  }
    // Use form data to send the CV file and job link to the backend
    const formData = new FormData(); // Create a new FormData object
    formData.append('jobLink', jobLink); // Append the job link
    formData.append('cvFile', cvFile);   // Append the CV file
    formData.append('message', prompt); // Append the message if needed

    try {

      const response = await fetch('http://127.0.0.1:8000/analyse', { // Replace with your backend endpoint
        method: 'POST', // Use POST method
        body: formData, // Set the form data as the request body
      });

      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      const result = await response.json(); // Parse the JSON response
      print (result); 
      console.log('Success:', result); // Handle the response data
      setData(result); // Update state with the response data
    } catch (error) {
      console.error('Error:', error); // Handle any errors
    }
  }; // <-- Close handleSubmit function here

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
          
          {/* 1. New "Upload CV" button and file input */}
          <label className="action-button" style={{ cursor: "pointer" }}>
            Upload CV
            <input
              type="file"
              accept=".pdf"
              onChange={handleFileChange}
              style={{ display: "none" }}
            />
          </label>

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