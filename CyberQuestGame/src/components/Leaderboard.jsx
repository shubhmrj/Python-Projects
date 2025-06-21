import React, { useEffect, useState } from "react";

function Leaderboard({ score, onRestart }) {
  const [scores, setScores] = useState([]);

  useEffect(() => {
    const prev = JSON.parse(localStorage.getItem("cq_scores") || "[]");
    const updated = [...prev, score].sort((a, b) => b - a).slice(0, 5);
    setScores(updated);
    localStorage.setItem("cq_scores", JSON.stringify(updated));
  }, [score]);

  return (
    <div className="card" style={{ textAlign: 'center' }}>
      <h2 style={{ marginBottom: '1rem' }}>Leaderboard</h2>
      <ol style={{ textAlign: 'left', margin: '0 auto 1.5rem', maxWidth: 200 }}>
        {scores.map((s, i) => (
          <li key={i} style={{ fontWeight: i === 0 ? 700 : 400, fontSize: i === 0 ? '1.2rem' : '1rem', color: i === 0 ? '#2563eb' : '#f1f5f9' }}>{s}</li>
        ))}
      </ol>
      <button onClick={onRestart} style={{ fontSize: '1.1rem', padding: '0.7rem 2rem' }}>Home</button>
    </div>
  );
}

export default Leaderboard;
