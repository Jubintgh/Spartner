import React, { useState, useEffect } from 'react';
import { BrowserRouter, Route, Switch } from 'react-router-dom';
import { useDispatch } from 'react-redux';
import LoginForm from './components/auth/LoginForm';
import SignUpForm from './components/auth/SignUpForm';
import NavBar from './components/NavBar';
import ProtectedRoute from './components/auth/ProtectedRoute';
import UsersList from './components/UsersList';
import User from './components/User';
import { authenticate } from './store/session';
import AnswersForm from './components/auth/AnswersForm';
import Footer from './components/Footer';
import DiscoverPage from './components/DiscoverPage';
import EditAnswersForm from './components/EditAnswersForm/index';
import EditUserForm from './components/EditUserInfo/index';
import LandingPage from './components/LandingPage';
import MatchesContainer from './components/MatchesContainer';
import LikesContainer from './components/LikesContainer';
import ProfilePage from './components/ProfilePage';

function App() {
  const [loaded, setLoaded] = useState(false);
  const dispatch = useDispatch();

  useEffect(() => {
    (async () => {
      await dispatch(authenticate());
      setLoaded(true);
    })();
  }, [dispatch]);

  if (!loaded) {
    return null;
  }

  return (
    <div className='page-container'>
      <div className='content-wrap'>
        <BrowserRouter>
          <NavBar />
            <Switch>
              <Route path='/' exact={true}>
                <LandingPage />
              </Route>
              <Route path='/login' exact={true}>
                <LoginForm />
              </Route>
              <ProtectedRoute path='/discover' exact={true}>
                <DiscoverPage />
              </ProtectedRoute>
              <Route path='/sign-up' exact={true}>
                <SignUpForm />
              </Route>
              <ProtectedRoute path='/users' exact={true} >
                <UsersList/>
              </ProtectedRoute>
              <Route path='/users/:userId/init-answers' exact={true}>
                <AnswersForm />
              </Route>
              <Route path='/users/:userId/edit-answers' exact={true}>
                <EditAnswersForm />
              </Route>
              <ProtectedRoute path='/users/:userId' exact={true}>
                <ProfilePage />
              </ProtectedRoute>
              <Route path='/users/:userId/edit-info' exact={true}>
                <EditUserForm />
              </Route>
              <Route path='/users/:userId/matches' exact={true}>
                <MatchesContainer />
              </Route>
              <Route path='/users/:userId/likes' exact={true}>
                <LikesContainer />
              </Route>
              <ProtectedRoute path='/discover' exact={true}>
                <DiscoverPage />
              </ProtectedRoute>
            </Switch>
        </BrowserRouter>
      </div>
      <Footer />
    </div>
  );
}
{
  /* <ProtectedRoute path='/' exact={true}>
  <LandingPage />
</ProtectedRoute> */
}

export default App;
