import { BrowserRouter as Router, Route, Routes, Navigate  } from 'react-router-dom'
import Leaderboard from './pages/Leaderboard'
import About from './pages/About'
import Scoresfeed from './pages/Scores-feed'
import Header from './components/Header/Header'
import './App.css'

const App = () => {
  return (
    <Router>
      <Header/>
      <Routes>
          <Route path="/about" element={<About />} />
          <Route path="/scores-feed" element={<Scoresfeed />} />
          <Route path="/" element={<Navigate to="/leaderboard" />} />
          <Route path="/leaderboard" element={<Leaderboard />} />
      </Routes>
    </Router>
  );
};

export default App;
