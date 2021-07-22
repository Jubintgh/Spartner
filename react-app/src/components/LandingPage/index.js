import React from 'react';
import { Link } from 'react-router-dom';
import "./LandingPage.css"

const LandingPage = () => {

  return (
      <div className="splash-background">
    <div className="splash-container">
        <div className="splash-banner">
      <h1>Spartner</h1>
      <h3>Have the match of a lifetime</h3>
        </div>
      <div className="splash-buttons">
      <button>Log In</button>
      <button>Sign Up</button>
      </div>
    </div>
      </div>
  );
  }
export default LandingPage;