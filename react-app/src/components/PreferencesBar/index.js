import React from 'react';
import { Link } from 'react-router-dom';
import { useSelector } from 'react-redux'

const PreferencesBar = () => {
const user = useSelector(state => state.session.user);
const isCoach = user?.coach;

  
/* 
const changeImageSourceLiked = (e) => {
    if (likeButton === '/like-button-clicked.png') {
      setLikeButton('/like-button-unclicked.png');
    } else {
      setLikeButton('/like-button-clicked.png');
    }
  };

  const changeImageSourceDisliked = (e) => {
    if (dislikeButton === '/dislike-button-clicked.png') {
      setDislikeButton('/dislike-button-unclicked.png');
    } else {
      setDislikeButton('/dislike-button-clicked.png');
    }
  };

*/ 

let renderCoachContent = null;

  if (!isCoach) {
    renderCoachContent = (
        <div className="element">
        <div className="icon">
            <img/>
        </div>
        <div className="icon-label">
            <h5>Coaches</h5>
        </div>)
};
  
  return (
    <div className="block">
      <div className="element">
        <div className="icon">
            <img/>
        </div>
        <div className="icon-label">
            <h5>Recommended</h5>
        </div>
      </div>
      <div className="element">
        <div className="icon">
            <img/>
        </div>
        <div className="icon-label">
            <h5>Weight Class</h5>
        </div>
      </div>
      <div className="element">
        <div className="icon">
            <img/>
        </div>
        <div className="icon-label">
            <h5>Vaccinated</h5>
        </div>
      </div>
      <div className="element">
        <div className="icon">
            <img/>
        </div>
        <div className="icon-label">
            <h5>Professional Level</h5>
        </div>
      </div>
      {renderCoachContent}
      </div>
    </div>
  );
};
{/* { user? <div className="nav-logo">
    <Link id="navbar__brand-home" to='/discover' exact={true} activeClassName='active'>
        <img src='https://user-images.githubusercontent.com/35717793/126367109-4954f04b-0cb7-4ca9-a25a-d18e6b7cb74a.png' alt='logo' id='navbar__logo' />
    </Link>
  </div> : <div className="nav-logo">
    <Link id="navbar__brand-home" to='/' exact={true} activeClassName='active'>
        <img src='https://user-images.githubusercontent.com/35717793/126367109-4954f04b-0cb7-4ca9-a25a-d18e6b7cb74a.png' alt='logo' id='navbar__logo' />
    </Link>
  </div>}
{navContent} */};

export default PreferencesBar
