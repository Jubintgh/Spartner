import React from 'react';
import { Link } from 'react-router-dom';
import { useSelector } from 'react-redux'

const PreferencesBar = () => {
  const user = useSelector(state => state.session.user);
  const profImage = user?.img_url
  let navContent = null;
  if(!user) {
    navContent = (
      <ul className='navbar'>
        <li className='navbar__link'>
          <Link to='/' exact={true} activeClassName='active'>
            Home
          </Link>
        </li>
        <li className='navbar__link'>
          <Link to='/login' exact={true} activeClassName='active'>
            Login
          </Link>
        </li>
        <li className='navbar__link'>
          <Link to='/sign-up' exact={true} activeClassName='active'>
            Sign Up
          </Link>
        </li>
        <li className='navbar__link'>
          <Link to='/users' exact={true} activeClassName='active'>
            Users
          </Link>
        </li>
        <li className="navbar__button">
          <DemoUserButton />
        </li>
      </ul>
    )
  } else {

    navContent = (
        <ul className="navbar">
          <li className="navbar__link">
            <Link to='/discover' exact={true}  activeClassName='active'>
              Home
            </Link>
          </li>
          <li className="navbar__link">
            <Link to='/users' exact={true} activeClassName='active'>
              Users
            </Link>
          </li>
          <li className="navbar__link">
            <Link to={`/users/${user.id}/likes`} exact={true} activeClassName='active'>
              Connections
            </Link>
          </li>
          <li className="navbar__link">
            <Link to={`/users/${user.id}`} exact={true} activeClassName='active'>
              Profile
            </Link>
          </li>
          <li className="navbar__link">
              <img src={`${profImage}`} style={{height:'65px', width:'65px', 'borderRadius':'50%', margin: '5px', marginTop : '10px', objectFit: 'cover'}}/>
          </li>
          <li className="navbar__button">
            <LogoutButton />
          </li>
        </ul>
    )
  }
  return (
    <div>
      { user? <div className="nav-logo">
          <Link id="navbar__brand-home" to='/discover' exact={true} activeClassName='active'>
              <img src='https://user-images.githubusercontent.com/35717793/126367109-4954f04b-0cb7-4ca9-a25a-d18e6b7cb74a.png' alt='logo' id='navbar__logo' />
          </Link>
        </div> : <div className="nav-logo">
          <Link id="navbar__brand-home" to='/' exact={true} activeClassName='active'>
              <img src='https://user-images.githubusercontent.com/35717793/126367109-4954f04b-0cb7-4ca9-a25a-d18e6b7cb74a.png' alt='logo' id='navbar__logo' />
          </Link>
        </div>}
      {navContent}
    </div>
  );
};

export default PreferencesBar;
