import React from "react";

function LandingPage({ onStart }) {
  return (
    <div className="card" style={{ textAlign: 'center' }}>
      <h1 style={{ fontSize: '2.5rem', marginBottom: '1rem' }}>Cyber Quest</h1>
      <p style={{ fontSize: '1.1rem', marginBottom: '2rem' }}>
        Welcome to <b>Cyber Quest</b>!<br />
        Test your cybersecurity knowledge and learn how to stay safe online.<br />
        <span role="img" aria-label="shield">🛡️</span>
      </p>
      <button onClick={onStart} style={{ fontSize: '1.3rem', padding: '1rem 2.5rem' }}>Start Game</button>
    </div>
  );
}

export default LandingPage;
