import React, { useState } from "react";

const CVAnalynser = () => {
  const [search, setSearch] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    // Do something with the search value
    alert(`You searched for: ${search}`);
  };

  return (
    <>
      <h1
        style={{
          fontSize: "3rem",
          textAlign: "center",
          marginTop: "30px",
          marginBottom: "20px"
        }}
      >
        CV Analyser
      </h1>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Search or type here..."
          style={{ marginBottom: "10px", padding: "8px", width: "60%" }}
          value={search}
          onChange={(e) => setSearch(e.target.value)}
        />
        <button type="submit" style={{ marginLeft: "10px" }}>
          Enter
        </button>
      </form>
      <br />
      <input
        type="text"
        placeholder="Job Link"
        style={{ marginBottom: "10px", padding: "8px", width: "60%" }}
      />
      <br />
      <button>Upload CV</button>
      <div id="prompt-box"></div>
      #prompt-box {
  background-color: #f4f7f9; /* A light grey background */
  border-left: 4px solid #007bff; /* A solid blue left border for emphasis */
  padding: 20px; /* Space inside the box */
  margin: 20px 0; /* Space outside the box */
  border-radius: 8px; /* Rounded corners */
  box-shadow: 0 2px 4px rgba(0,0,0,0.1); /* A subtle shadow */
  font-family: sans-serif; /* A clean font */
  line-height: 1.6; /* Spacing between lines of text */
}
// Get a reference to the HTML box using its ID
const promptBox = document.getElementById('prompt-box');

// Set a loading message while we fetch the data
promptBox.textContent = 'Loading prompt...';

// Fetch the JSON file
fetch('mockData.json')
  .then(response => response.json()) // Convert the response to a JSON object
  .then(data => {
    // Access the specific prompt you want to display.
    // This example takes the first suggestion from the array.
    const promptText = data.suggestedImprovements[0].suggestion;

    // Put the text inside the box
    promptBox.textContent = promptText;
  })
  .catch(error => {
    // If something goes wrong, show an error message
    console.error('Failed to fetch prompt:', error);
    promptBox.textContent = 'Error: Could not load the prompt.';
  });

    </>

  );
};

export default CVAnalyser;