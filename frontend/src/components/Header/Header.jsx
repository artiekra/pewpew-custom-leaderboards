import { useState, useEffect, useRef } from 'react';
import { Link } from 'react-router-dom';
import './Header.css';

const Header = () => {
    const [isNavOpen, setIsNavOpen] = useState(false);
    const navRef = useRef(null);
    const toggleRef = useRef(null);

    useEffect(() => {
        const handleOutsideClick = (event) => {
            if (navRef.current && !navRef.current.contains(event.target) && !toggleRef.current.contains(event.target)) {
                setIsNavOpen(false);
            }
        };

        document.addEventListener('click', handleOutsideClick);

        return () => {
            document.removeEventListener('click', handleOutsideClick);
        };
    }, []);

    const handleNavToggle = () => {
        setIsNavOpen((prev) => !prev);
    };

    return (
        <header className="header">
            <nav ref={navRef} className={`nav ${isNavOpen ? 'open' : ''}`}>
                <ul className="nav-list">
                    <li className={`nav-item ${isNavOpen ? '' : 'hidden'}`}>
                        <Link to="/leaderboard">
                            <svg
                                width="140"
                                height="50"
                                xmlns="http://www.w3.org/2000/svg"
                                viewBox="0 0 200 50"
                                preserveAspectRatio="xMidYMid meet"
                                className="svg-icon"
                            >
                                <rect x="5" y="40" width="5" height="5" fill="none" stroke="rgb(19, 65, 150)" strokeWidth="2" />
                                <rect x="180" y="5" width="5" height="5" fill="none" stroke="rgb(19, 65, 150)" strokeWidth="2" />
                                <line x1="1" y1="12" x2="12" y2="1" stroke="rgb(19, 65, 150)" strokeWidth="2" />
                                <line x1="179" y1="49" x2="190" y2="37" stroke="rgb(19, 65, 150)" strokeWidth="2" />
                                <polygon points="20,0 190,0 190,30 172,50 0,50 0,40 0,20" fill="none" stroke="rgb(19, 65, 150)" strokeWidth="3" className="svg-border" />
                                <text className='text' x="50%" y="50%" textAnchor="middle" fill="white" dy=".3em" fontSize="30">Leaderboard</text>
                            </svg>
                        </Link>
                    </li>
                    <li className={`nav-item ${isNavOpen ? '' : 'hidden'}`}>
                        <Link to="/scores-feed">
                            <svg
                                width="140"
                                height="50"
                                xmlns="http://www.w3.org/2000/svg"
                                viewBox="0 0 200 50"
                                preserveAspectRatio="xMidYMid meet"
                                className="svg-icon"
                            >
                                <rect x="5" y="40" width="5" height="5" fill="none" stroke="rgb(19, 65, 150)" strokeWidth="2" />
                                <rect x="180" y="5" width="5" height="5" fill="none" stroke="rgb(19, 65, 150)" strokeWidth="2" />
                                <line x1="1" y1="12" x2="12" y2="1" stroke="rgb(19, 65, 150)" strokeWidth="2" />
                                <line x1="179" y1="49" x2="190" y2="37" stroke="rgb(19, 65, 150)" strokeWidth="2" />
                                <polygon points="20,0 190,0 190,30 172,50 0,50 0,40 0,20" fill="none" stroke="rgb(19, 65, 150)" strokeWidth="3" className="svg-border" />
                                <text className='text' x="50%" y="50%" textAnchor="middle" fill="white" dy=".3em" fontSize="30">Scores feed</text>
                            </svg>
                        </Link>
                    </li>
                    <li className={`nav-item ${isNavOpen ? '' : 'hidden'}`}>
                        <Link to="/about">
                            <svg
                                xmlns="http://www.w3.org/2000/svg"
                                viewBox="0 0 200 50"
                                preserveAspectRatio="xMidYMid meet"
                                className="svg-icon"
                            >
                                <rect x="5" y="40" width="5" height="5" fill="none" stroke="rgb(19, 65, 150)" strokeWidth="2" />
                                <rect x="180" y="5" width="5" height="5" fill="none" stroke="rgb(19, 65, 150)" strokeWidth="2" />
                                <line x1="1" y1="12" x2="12" y2="1" stroke="rgb(19, 65, 150)" strokeWidth="2" />
                                <line x1="179" y1="49" x2="190" y2="37" stroke="rgb(19, 65, 150)" strokeWidth="2" />
                                <polygon points="20,0 190,0 190,30 172,50 0,50 0,40 0,20" fill="none" stroke="rgb(19, 65, 150)" strokeWidth="3" className="svg-border" />
                                <text className='text' x="50%" y="50%" textAnchor="middle" fill="white" dy=".3em" fontSize="30">About</text>
                            </svg>
                        </Link>
                    </li>
                </ul>
            </nav>
            <div ref={toggleRef} className={`nav-toggle ${isNavOpen ? 'hidden' : ''}`} onClick={handleNavToggle}>
                <svg
                    width="140"
                    height="50"
                    xmlns="http://www.w3.org/2000/svg"
                    viewBox="0 0 200 50"
                    preserveAspectRatio="xMidYMid meet"
                    className={`navigationSvg ${isNavOpen ? 'hidden' : ''}`}
                >
                    <path
                        d="M 10 10 L 190 10 L 180 40 L 20 40 L 10 10"
                        fill="transparent"
                        stroke="rgb(19, 65, 150)"
                        strokeWidth="2"
                    />
                    <text className={`nav-toggle-label ${isNavOpen ? 'hidden' : ''}`} x="50%" y="50%" textAnchor="middle" fill="white" dy=".3em">Open navigation</text>
                </svg>
            </div>
        </header>
    );
};

export default Header;
