import React, { useState } from "react";
import questionsData from "../data/questions";

function GameScreen({ level, onFinish, onBack }) {
  const questions = questionsData[level?.name] || [];
  const [current, setCurrent] = useState(0);
  const [score, setScore] = useState(0);
  const [showFeedback, setShowFeedback] = useState(false);
  const [feedback, setFeedback] = useState("");

  if (!level) return null;

  const handleAnswer = (isCorrect) => {
    setShowFeedback(true);
    setFeedback(isCorrect ? "✅ Correct!" : "❌ Incorrect!");
    if (isCorrect) setScore((s) => s + 1);
    setTimeout(() => {
      setShowFeedback(false);
      if (current + 1 < questions.length) {
        setCurrent((c) => c + 1);
      } else {
        onFinish(score + (isCorrect ? 1 : 0));
      }
    }, 1100);
  };

  const q = questions[current];
  return (
    <div className="card" style={{ textAlign: 'center' }}>
      <h2 style={{ marginBottom: '1rem' }}>{level.name}</h2>
      <div style={{ marginBottom: '1rem' }}>
        <strong>Question {current + 1} of {questions.length}</strong>
        <p style={{ fontSize: '1.1rem' }}>{q.question}</p>
        <div style={{ display: 'flex', flexDirection: 'column', gap: '0.75rem', alignItems: 'center' }}>
          {q.options.map((opt, idx) => (
            <button
              key={idx}
              onClick={() => handleAnswer(opt.correct)}
              disabled={showFeedback}
              style={{ width: '100%', maxWidth: 320 }}
            >
              {opt.text}
            </button>
          ))}
        </div>
        {showFeedback && (
          <div style={{ marginTop: 16, fontWeight: 600, color: feedback.includes('Correct') ? '#22c55e' : '#ef4444' }}>
            {feedback} <br />
            <span style={{ fontWeight: 400, fontSize: '0.95rem' }}>{q.explanation}</span>
          </div>
        )}
      </div>
      <div style={{ marginTop: 20, display: 'flex', justifyContent: 'space-between' }}>
        <button onClick={onBack} style={{ background: "#64748b" }}>Quit</button>
        <span style={{ alignSelf: 'center', marginLeft: 10, fontWeight: 600 }}>Score: {score}</span>
      </div>
    </div>
  );
}

export default GameScreen;
