import React from 'react';
import { Link } from 'react-router-dom';
import "./LandingPage.css"

const LandingPage = () => {

  return (
      <div className="splash-background">
    <div className="splash-container">
        <div className="splash-banner">
      <img src="https://user-images.githubusercontent.com/35717793/126691381-d2839a71-94f6-4343-836d-216d8b97e9ec.png" className="splash-header" />
      <h3 className="splash-subheader">Have the match of a lifetime</h3>
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