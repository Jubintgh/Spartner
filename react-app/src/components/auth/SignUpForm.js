import React, { useState } from 'react';
import { useEffect, useSelector, useDispatch } from 'react-redux'
import { Redirect, useHistory } from 'react-router-dom';
import { signUp } from '../../store/session';

const SignUpForm = () => {
  const [errors, setErrors] = useState([]);
  const [username, setUsername] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [repeatPassword, setRepeatPassword] = useState('');
  const [first_name, setFirstName] = useState('');
  const [last_name, setLastName] = useState('');
  const [age, setAge] = useState('');
  const [location, setLocation] = useState('');
  const [gender, setGender] = useState(0);
  const [coach, setCoach] = useState(0);
  const [img_url, setImageUrl] = useState('');
  const [discipline, setDiscipline] = useState(0);
  const user = useSelector(state => state.session.user);
  const dispatch = useDispatch();
  // const history = useHistory();

  const onSignUp = async (e) => {
    e.preventDefault();
    if (password === repeatPassword) {
      const data = await dispatch(signUp(
        username,
        email,
        password,
        first_name,
        last_name,
        age,
        location,
        gender,
        coach,
        discipline,
        img_url));
      if (data) {
        setErrors(data)
      }
    }
  };

  const updateFirstName = (e) => {
    setFirstName(e.target.value);
  };

  const updateLastName = (e) => {
    setLastName(e.target.value);
  };

  const updateAge = (e) => {
    setAge(e.target.value);
  };

  const updateLocation = (e) => {
    setLocation(e.target.value);
  };

  const updateGender = (e) => {
    setGender(e.target.value);
  };

  const updateCoach = (e) => {
    setCoach(e.target.value);
  };

  const updateImageUrl = (e) => {
    setImageUrl(e.target.value);
  };

  const updateUsername = (e) => {
    setUsername(e.target.value);
  };

  const updateEmail = (e) => {
    setEmail(e.target.value);
  };

  const updateDiscipline = (e) => {
    setDiscipline(e.target.value);
  };

  const updatePassword = (e) => {
    setPassword(e.target.value);
  };

  const updateRepeatPassword = (e) => {
    setRepeatPassword(e.target.value);
  };

  if (user) {
    return <Redirect to={`/users/${user.id}/init-answers`} />;
  }

  return (
    <form onSubmit={onSignUp}>
      <div className="form-errors">
        {errors.map((error, ind) => (
          <div key={ind}>{error}</div>
        ))}
      </div>
      <div className="form-container">
        <div className="form-half">

      <div classname="form-question">
        <div className="form-question-label">
        <label>User Name</label>
        </div>
        <div className="form-input">
        <input
          type='text'
          name='username'
          onChange={updateUsername}
          value={username}
          ></input>
        </div>
      </div>
      <div classname="form-question">
      <div className="form-question-label">
        <label>First Name</label>
      </div>
      <div className="form-input">
        <input
          type='text'
          name='firstName'
          onChange={updateFirstName}
          value={first_name}
          ></input>
      </div>
      </div>
      <div classname="form-question">
      <div className="form-question-label">
        <label>Last Name</label>
      </div>
      <div className="form-input">
        <input
          type='text'
          name='lastName'
          onChange={updateLastName}
          value={last_name}
          ></input>
      </div>
      </div>
      <div classname="form-question">
      <div className="form-question-label">
        <label>Age</label>
      </div>
      <div className="form-input">
        <input
          type='number'
          name='age'
          onChange={updateAge}
          value={age}
          ></input>
      </div>
      </div>
        <div classname="form-question">
        <div className="form-question-label">
        <label>Location</label>
        </div>
        <div className="form-input">
        <input
          type='text'
          name='location'
          onChange={updateLocation}
          value={location}
          ></input>
        </div>
      </div>
      <div classname="form-question">
      <div className="form-question-label">
        <label>Gender</label>
      </div>
      <div className="form-input">
        <select
          type='integer'
          name='gender'
          onChange={updateGender}
          value={gender}
          >
          <option value="0">Female</option>
          <option value="1">Male</option>
          <option value="2">Other</option>
        </select>
      </div>
      </div>
      </div>
      <div className="form-half">
      <div classname="form-question">
      <div className="form-question-label">
        <label>Coach</label>
      </div>
      <div className="form-input">
        <select
          type='integer'
          name='coach'
          onChange={updateCoach}
          value={coach}
          >
          <option value="False">No, I am not a coach</option>
          <option value="True">Yes, I am a coach</option>
        </select>
      </div>
      </div>
      <div classname="form-question">
      <div className="form-question-label">
        <label>Image URL</label>
      </div>
      <div className="form-input">
        <input
          type='text'
          name='imageurl'
          onChange={updateImageUrl}
          value={img_url}
          ></input>
      </div>
      </div>
      <div classname="form-question">
      <div className="form-question-label">
        <label>Email</label>
      </div>
      <div className="form-input">
        <input
          type='text'
          name='email'
          onChange={updateEmail}
          value={email}
          ></input>
      </div>
      </div>
      <div classname="form-question">
      <div className="form-question-label">
        <label>Discipline</label>
      </div>
      <div className="form-input">
        <select
          name='discipline'
          type='integer'
          onChange={updateDiscipline}
          value={discipline}
          >
          <option value="0">Southpaw</option>
          <option value="1">Kickboxing</option>
          <option value="2">Orthodox</option>
          <option value="3">Judo</option>
          <option value="4">Muay Thai</option>
          <option value="5">Grappling</option>
          <option value="6">Counter Striker</option>
          <option value="7">Karate</option>
          <option value="8">Switch</option>
          <option value="9">Brazilian Jiu-Jitsu</option>
        </select>
      </div> 
      </div>
      <div classname="form-question">
      <div className="form-question-label">
        <label>Password</label>
      </div>
      <div className="form-input">
        <input
          type='password'
          name='password'
          onChange={updatePassword}
          value={password}
          ></input>
      </div>
      </div>
      <div classname="form-question">
      <div className="form-question-label">
        <label>Repeat Password</label>
      </div>
      <div className="form-input">
        <input
          type='password'
          name='repeat_password'
          onChange={updateRepeatPassword}
          value={repeatPassword}
          required={true}
          ></input>
      </div>
      </div>
        </div>
      </div>
      <button type='submit'>Sign Up</button>
    </form>
  );
};

export default SignUpForm;
