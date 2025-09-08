const CVAnalyser = () => (
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
    <input
      type="text"
      placeholder="Search or type here..."
      style={{ marginBottom: "10px", padding: "8px", width: "60%" }}
    />
    <br />
    <button>Job Link</button>
    <button>Upload CV</button>
  </>
);

export default CVAnalyser;