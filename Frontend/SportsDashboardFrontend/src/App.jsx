import { Routes, Route, Link } from "react-router-dom";
import Home from "./Pages/Player.jsx";
import About from "./Pages/Team.jsx";

function App() {
  return (
    <div>
      {/* Simple navigation bar */}
      <nav style={{ marginBottom: "1rem" }}>
        <Link to="/" style={{ marginRight: "1rem" }}>
          Home
        </Link>
        <Link to="/about">About</Link>
      </nav>

      {/* Routes */}
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/about" element={<About />} />
        <Route path="*" element={<h2>404 Not Found</h2>} />
      </Routes>
    </div>
  );
}

export default App;
