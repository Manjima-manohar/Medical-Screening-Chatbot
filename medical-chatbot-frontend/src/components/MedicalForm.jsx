import React, { useState } from 'react'
import axios from "axios";
import "./MedicalForm.css"

const MedicalForm = () => {
const [symptoms, setSymptoms] = useState("");
  const [duration, setDuration] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();

    setLoading(true);
    setResult(null);

    try {
      const response = await axios.post(
        "http://127.0.0.1:8000/api/screening/",
        {
          symptoms,
          duration,
        }
      );

      setResult(response.data);
    } catch (error) {
      console.error(error);
      alert("Failed to fetch response");
    }

    setLoading(false);
  };

  return (
    <>
      <h1>AI Medical Screening Chatbot</h1>
      <form onSubmit={handleSubmit}>
        <div>
          <label>Symptoms</label>
          <textarea
            value={symptoms}
            onChange={(e) => setSymptoms(e.target.value)}
            rows="4"
            required
          />
        </div>
            <div>
          <label>Duration</label>
          <input
            type="text"
            value={duration}
            onChange={(e) => setDuration(e.target.value)}
            placeholder="Example: 3 days"
            required
          />
        </div>
        <button type="submit">
          {loading ? "Analyzing..." : "Analyze"}
        </button>
      </form>

      {result && (
        <div className="result">
          <h2>Possible Conditions</h2>

          <ul>
            {result.possible_conditions?.map((item, index) => (
              <li key={index}>
                {item.condition} - {item.likelihood}
              </li>
            ))}
          </ul>

          <h3>Severity Assessment</h3>
          <p>{result.severity_assessment}</p>

          <h3>Common Causes</h3>
          <ul>
            {result.common_causes?.map((cause, index) => (
              <li key={index}>{cause}</li>
            ))}
          </ul>

          <h3>Warning Signs</h3>
          <ul>
            {result.warning_signs?.map((warning, index) => (
              <li key={index}>{warning}</li>
            ))}
          </ul>

          <h3>Recommended Action</h3>
          <p>{result.recommended_action}</p>

          <p className="disclaimer">
            {result.disclaimer}
          </p>
        </div>
      )}
    </>
  )
}

export default MedicalForm
