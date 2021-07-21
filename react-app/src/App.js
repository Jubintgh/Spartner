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


function App() {
  const [loaded, setLoaded] = useState(false);
  const dispatch = useDispatch();

  useEffect(() => {
    (async() => {
      await dispatch(authenticate());
      setLoaded(true);
    })();
  }, [dispatch]);

  if (!loaded) {
    return null;
  }

  return (
    <div className="page-container">
      <div className="content-wrap">
        <BrowserRouter>
          <NavBar />
            <Switch>
              <Route path='/login' exact={true}>
                <LoginForm />
              </Route>
              <Route path='/sign-up' exact={true}>
                <SignUpForm />
              </Route>
              <ProtectedRoute path='/users' exact={true} >
                <UsersList/>
              </ProtectedRoute>
              <ProtectedRoute path='/users/:userId' exact={true} >
                <User />
              </ProtectedRoute>
              <ProtectedRoute path='/discover' exact={true} >
                <h1>My Home Page</h1>
                <h2> what austin and jay are currently on</h2>
              </ProtectedRoute>
              <Route path='/users/:userId/answers' exact={true}>
                <AnswersForm />
              </Route>
            </Switch>
        </BrowserRouter>
        </div>
        <Footer />
    </div>

  );
}

export default App;
