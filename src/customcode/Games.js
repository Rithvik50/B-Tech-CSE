import React, { useState } from 'react';
import flappybird from "./imgs/flappybird.png";
import snake from "./imgs/snake.png";
import tetris from "./imgs/tetris.png";
import twentyfortyeight from "./imgs/2048.png";
import doodlejump from "./imgs/doodlejump.png";
import ataribreakout from "./imgs/ataribreakout.png";


function Games() {
  const [selectedGame, setSelectedGame] = useState(null);

  const handleGameClick = (gameId) => {
    // Use a switch statement to determine the game URL based on the clicked button
    let gameUrl;
    switch (gameId) {
      case "FlappyBird":
        gameUrl = "http://127.0.0.1:5500/wt-project/src/customcode/games/FlappyBird.html";
        break;
      case "Snake":
        gameUrl = "http://127.0.0.1:5500/wt-project/src/customcode/games/Snake.html";
        break;
      case "Tetris":
        gameUrl = "http://127.0.0.1:5500/wt-project/src/customcode/games/Tetris.html";
        break;
      case "2048":
        gameUrl = "http://127.0.0.1:5500/wt-project/src/customcode/games/2048.html";
        break;
      case "DoodleJump":
        gameUrl = "http://127.0.0.1:5500/wt-project/src/customcode/games/DoodleJump.html";
        break;
      case "AtariBreakout":
        gameUrl = "http://127.0.0.1:5500/wt-project/src/customcode/games/AtariBreakout.html";
        break;
      default:
        // Handle default case if needed
    }

    // Update the selectedGame state and navigate to the selected game URL
    setSelectedGame(gameId);
    window.location.href = gameUrl;
  };

  return (
    <>
      <nav className="but">
        <h1>GAMES</h1>
        
        <span>
          <button
            id="FlappyBird"
            onClick={() => handleGameClick("FlappyBird")}
            style={{
              textDecoration: 'none',
              color: 'inherit',
              textAlign: 'center',
              borderRadius: '10px',
              margin: '10px',
              border: selectedGame === "FlappyBird" ? '2px solid red' : 'none', // Add a border to the selected game
            }}
          >
            Flappy Bird<br></br>
            <img src={flappybird} alt="Flappy Bird" style={{ width: '200px', height: '200px' }} />
          </button>

          <button
            id="Snake"
            onClick={() => handleGameClick("Snake")}
            style={{
              textDecoration: 'none',
              color: 'inherit',
              textAlign: 'center',
              borderRadius: '10px',
              margin: '10px',
              border: selectedGame === "Snake" ? '2px solid red' : 'none', // Add a border to the selected game
            }}
          >
            Snake<br></br>
            <img src={snake} alt="Snake" style={{ width: '200px', height: '200px' }} />
          </button>

          <button
            id="Tetris"
            onClick={() => handleGameClick("Tetris")}
            style={{
              textDecoration: 'none',
              color: 'inherit',
              textAlign: 'center',
              borderRadius: '10px',
              margin: '10px',
              border: selectedGame === "Tetris" ? '2px solid red' : 'none', // Add a border to the selected game
            }}
          >
            Tetris<br></br>
            <img src={tetris} alt="Tetris" style={{ width: '200px', height: '200px' }} />
          </button>
        </span>

        <br></br>

        <span>
          <button
            id="2048"
            onClick={() => handleGameClick("2048")}
            style={{
              textDecoration: 'none',
              color: 'inherit',
              textAlign: 'center',
              borderRadius: '10px',
              margin: '10px',
              border: selectedGame === "2048" ? '2px solid red' : 'none', // Add a border to the selected game
            }}
          >
            2048<br></br>
            <img src={twentyfortyeight} alt="2048" style={{ width: '200px', height: '200px' }} />
          </button>

          <button
            id="DoodleJump"
            onClick={() => handleGameClick("DoodleJump")}
            style={{
              textDecoration: 'none',
              color: 'inherit',
              textAlign: 'center',
              borderRadius: '10px',
              margin: '10px',
              border: selectedGame === "DoodleJump" ? '2px solid red' : 'none', // Add a border to the selected game
            }}
          >
            Doodle Jump<br></br>
            <img src={doodlejump} alt="Doodle Jump" style={{ width: '200px', height: '200px' }} />
          </button>

          <button
            id="AtariBreakout"
            onClick={() => handleGameClick("AtariBreakout")}
            style={{
              textDecoration: 'none',
              color: 'inherit',
              textAlign: 'center',
              borderRadius: '10px',
              margin: '10px',
              border: selectedGame === "AtariBreakout" ? '2px solid red' : 'none', // Add a border to the selected game
            }}
          >
            Atari Breakout<br></br>
            <img src={ataribreakout} alt="Atari Breakout" style={{ width: '200px', height: '200px' }} />
          </button>
        </span>
      </nav>
      <html lang="en">
        <style>
          {`
            body {
              background-color: aquamarine;
            }
          `}
        </style>
      </html>
    </>
  );
}

export default Games;