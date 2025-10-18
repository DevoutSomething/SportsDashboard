import { Link } from "react-router-dom";
import "./playerstyle.css";

export default function Player() {
  return (
    <div>
      <h1>Hello, world!</h1>
      <p>Welcome to the Player page.</p>
      <div className="stat grids">
        <RankingComponent />
        <PlayersComponent />
      </div>
    </div>
  );
}

function RankingComponent() {
  const data = {
    wins: Math.floor(Math.random() * 100),
    losses: Math.floor(Math.random() * 100),
  };

  const pct = (data.wins / (data.wins + data.losses)).toFixed(3);
  const gb = (Math.random() * 10).toFixed(1);

  return (
    <div className="ranking-box">
      <h3 className="ranking-title">Team Ranking</h3>
      <p className="wins">Wins: {data.wins}</p>
      <p className="losses">Losses: {data.losses}</p>
      <p className="pct">Win %: {pct}</p>
      <p className="gb">GB: {gb}</p>
    </div>
  );
}

function PlayersComponent() {
  const players = [
    { name: "Alex Rivera", position: "Forward", link: "/about" },
    { name: "Jordan Lee", position: "Guard", link: "/about" },
    { name: "Chris Taylor", position: "Center", link: "/about" },
    { name: "Marcus Hill", position: "Guard", link: "/about" },
  ];

  return (
    <div className="players-box">
      <h3 className="players-title">Notable Players</h3>
      <div className="players-grid">
        {players.map((player, index) => (
          <Link key={index} to={player.link} className="player-card">
            <p className="player-name">{player.name}</p>
            <p className="player-position">{player.position}</p>
          </Link>
        ))}
      </div>
    </div>
  );
}
