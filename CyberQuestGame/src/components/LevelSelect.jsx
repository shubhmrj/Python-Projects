import React from "react";

const levels = [
  { id: 1, name: "Password Safety", emoji: "🔒" },
  { id: 2, name: "Phishing Awareness", emoji: "🎣" },
  { id: 3, name: "Malware Detection", emoji: "🦠" },
  { id: 4, name: "Online Privacy", emoji: "👤" },
];

function LevelSelect({ onSelect, onBack }) {
  return (
    <div className="card" style={{ textAlign: 'center' }}>
      <h2 style={{ marginBottom: '1.5rem' }}>Select a Level</h2>
      <ul style={{ listStyle: "none", padding: 0, marginBottom: '2rem' }}>
        {levels.map((level) => (
          <li key={level.id} style={{ margin: '1rem 0' }}>
            <button onClick={() => onSelect(level)} style={{ fontSize: '1.1rem', minWidth: 200 }}>
              <span style={{ fontSize: '1.5rem', marginRight: 8 }}>{level.emoji}</span>
              {level.name}
            </button>
          </li>
        ))}
      </ul>
      <button onClick={onBack} style={{ background: "#64748b" }}>Back</button>
    </div>
  );
}

export default LevelSelect;
