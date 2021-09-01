import React, { useState } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { Redirect } from 'react-router-dom';
import { login } from '../../store/session';
import DemoUserButton from './DemoUserButton';

const LoginForm = () => {
  const [errors, setErrors] = useState([]);
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const user = useSelector((state) => state.session.user);
  const dispatch = useDispatch();

  const onLogin = async (e) => {
    e.preventDefault();
    const data = await dispatch(login(email, password));
    if (data) {
      setErrors(data);
    }
  };

  const updateEmail = (e) => {
    setEmail(e.target.value);
  };

  const updatePassword = (e) => {
    setPassword(e.target.value);
  };

  if (user) {
    return <Redirect to='/discover' />;
  }

  return (
    <form onSubmit={onLogin}>
      <div className='form-container'>
        <div className='form-question'>
          <div className='form-question-label'>
            <label htmlFor='email'>Email</label>
          </div>
          <div className='form-input'>
            <input
              name='email'
              type='text'
              placeholder='Email'
              value={email}
              onChange={updateEmail}
            />
          </div>
        </div>
        <div className='form-question'>
          <div className='form-question-label'>
            <label htmlFor='password'>Password</label>
          </div>
          <div className='form-input'>
            <input
              name='password'
              type='password'
              placeholder='Password'
              value={password}
              onChange={updatePassword}
            />
          </div>
          <button type='submit'>Login</button>
        </div>
          <div className="form-errors">
            {errors.map((error, ind) => (
              <div key={ind}>{error}</div>
              ))}
          </div>
          <DemoUserButton />
          </div>
    </form>
  );
};

export default LoginForm;
