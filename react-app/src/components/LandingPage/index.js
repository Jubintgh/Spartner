import React from 'react';
import { Link } from 'react-router-dom';
import './LandingPage.css';
import DemoUserButton from '../auth/DemoUserButton';

const LandingPage = () => {
  return (
    <div className='splash-background'>
      <div className='splash-container'>
        <div className='splash-banner'>
          <img
            src='https://user-images.githubusercontent.com/35717793/126702199-828042e7-7543-47e1-b3d3-67539211241e.png'
            className='splash-header'
            alt=''
          />
          <h3 className='splash-subheader'>Have the match of a lifetime</h3>
        </div>
        <div className='splash-buttons'>
          <Link to='/login'>
            <button>Log In</button>
          </Link>
          <Link to='/sign-up'>
            <button>Sign Up</button>
          </Link>
          <DemoUserButton />
        </div>
      </div>
    </div>
  );
};
export default LandingPage;
