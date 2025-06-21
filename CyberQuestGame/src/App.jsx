import React, { useState } from "react";
import LandingPage from "./components/LandingPage.jsx";
import LevelSelect from "./components/LevelSelect.jsx";
import GameScreen from "./components/GameScreen.jsx";
import Leaderboard from "./components/Leaderboard.jsx";
import "./styles.css";

function App() {
  const [screen, setScreen] = useState("landing");
  const [level, setLevel] = useState(null);
  const [score, setScore] = useState(0);

  const startGame = () => setScreen("levelSelect");
  const selectLevel = (lvl) => {
    setLevel(lvl);
    setScreen("game");
  };
  const finishGame = (finalScore) => {
    setScore(finalScore);
    setScreen("leaderboard");
  };
  const goHome = () => {
    setScreen("landing");
    setLevel(null);
    setScore(0);
  };

  return (
    <div className="app-container">
      {screen === "landing" && <LandingPage onStart={startGame} />}
      {screen === "levelSelect" && <LevelSelect onSelect={selectLevel} onBack={goHome} />}
      {screen === "game" && <GameScreen level={level} onFinish={finishGame} onBack={goHome} />}
      {screen === "leaderboard" && <Leaderboard score={score} onRestart={goHome} />}
    </div>
  );
}

export default App;
