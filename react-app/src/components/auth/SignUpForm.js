import React, { useState, useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { Redirect } from 'react-router-dom';
import { signUp } from '../../store/session';
import DemoUserButton from './DemoUserButton';

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
  const [gender, setGender] = useState('');
  const [coach, setCoach] = useState(0);
  const [img_url, setImageUrl] = useState(
    'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_1280.png'
  );
  const [shownImgUrl, setShownImageUrl] = useState();
  const [discipline, setDiscipline] = useState('');
  const user = useSelector((state) => state.session.user);
  const dispatch = useDispatch();
  // const history = useHistory();
  // useEffect(() => {

  // }, [
  //   errors,
  //   username,
  //   email,
  //   password,
  //   repeatPassword,
  //   first_name,
  //   last_name,
  //   age,
  //   location,
  //   gender,
  //   coach,
  //   img_url,
  //   discipline,
  //   user,
  // ])

  const onSignUp = async (e) => {
    e.preventDefault();
    setImageUrl(
      !img_url
        ? 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_1280.png'
        : img_url
    );
    if (password === repeatPassword) {
      const data = await dispatch(
        signUp(
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
          img_url
        )
      );
      if (data) {
        setErrors(data);
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
    setShownImageUrl(e.target.value);
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

  // If the user does not provide an image url upon signup, a default img url is provided.  Needed two instances of use state so that the default image url would not show on the form if it was an empty input
  useEffect(() => {
    if (!shownImgUrl) {
      setImageUrl(
        'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_1280.png'
      );
    } else {
      setImageUrl(shownImgUrl);
    }
  }, [shownImgUrl, img_url]);

  if (user) {
    return <Redirect to={`/users/${user.id}/init-answers`} />;
  }

  return (
    <form onSubmit={onSignUp}>
      <div className='form-container'>
        <div className='form-actualForm'>
          <div className='form-half'>
            <div classname='form-question'>
              <div className='form-question-label'>
                <label>User Name</label>
              </div>
              <div className='form-input'>
                <input
                  type='text'
                  name='username'
                  onChange={updateUsername}
                  value={username}
                ></input>
              </div>
            </div>
            <div classname='form-question'>
              <div className='form-question-label'>
                <label>First Name</label>
              </div>
              <div className='form-input'>
                <input
                  type='text'
                  name='firstName'
                  onChange={updateFirstName}
                  value={first_name}
                ></input>
              </div>
            </div>
            <div classname='form-question'>
              <div className='form-question-label'>
                <label>Last Name</label>
              </div>
              <div className='form-input'>
                <input
                  type='text'
                  name='lastName'
                  onChange={updateLastName}
                  value={last_name}
                ></input>
              </div>
            </div>
            <div classname='form-question'>
              <div className='form-question-label'>
                <label>Age</label>
              </div>
              <div className='form-input'>
                <input
                  type='number'
                  name='age'
                  onChange={updateAge}
                  value={age}
                ></input>
              </div>
            </div>
            <div classname='form-question'>
              <div className='form-question-label'>
                <label>Location</label>
              </div>
              <div className='form-input'>
                <input
                  type='text'
                  name='location'
                  onChange={updateLocation}
                  value={location}
                ></input>
              </div>
            </div>
            <div classname='form-question'>
              <div className='form-question-label'>
                <label>Gender</label>
              </div>
              <div className='form-input'>
                <select
                  type='integer'
                  name='gender'
                  onChange={updateGender}
                  value={gender}
                >
                  <option value=''>Select</option>
                  <option value='0'>Female</option>
                  <option value='1'>Male</option>
                  <option value='2'>Other</option>
                </select>
              </div>
            </div>
          </div>
          <div className='form-half'>
            <div classname='form-question'>
              <div className='form-question-label'>
                <label>Coach</label>
              </div>
              <div className='form-input'>
                <select
                  type='integer'
                  name='coach'
                  onChange={updateCoach}
                  value={coach}
                >
                  <option value='False'>No, I am not a coach</option>
                  <option value='True'>Yes, I am a coach</option>
                </select>
              </div>
            </div>
            <div classname='form-question'>
              <div className='form-question-label'>
                <label>Image URL</label>
              </div>
              <div className='form-input'>
                <input
                  type='text'
                  name='imageurl'
                  onChange={updateImageUrl}
                  value={shownImgUrl}
                ></input>
              </div>
            </div>
            <div classname='form-question'>
              <div className='form-question-label'>
                <label>Email</label>
              </div>
              <div className='form-input'>
                <input
                  type='text'
                  name='email'
                  onChange={updateEmail}
                  value={email}
                ></input>
              </div>
            </div>
            <div classname='form-question'>
              <div className='form-question-label'>
                <label>Discipline</label>
              </div>
              <div className='form-input'>
                <select
                  name='discipline'
                  type='integer'
                  onChange={updateDiscipline}
                  value={discipline}
                >
                  <option value=''>Select</option>
                  <option value='0'>Southpaw</option>
                  <option value='1'>Kickboxing</option>
                  <option value='2'>Orthodox</option>
                  <option value='3'>Judo</option>
                  <option value='4'>Muay Thai</option>
                  <option value='5'>Grappling</option>
                  <option value='6'>Counter Striker</option>
                  <option value='7'>Karate</option>
                  <option value='8'>Switch</option>
                  <option value='9'>Brazilian Jiu-Jitsu</option>
                </select>
              </div>
            </div>
            <div classname='form-question'>
              <div className='form-question-label'>
                <label>Password</label>
              </div>
              <div className='form-input'>
                <input
                  type='password'
                  name='password'
                  onChange={updatePassword}
                  value={password}
                ></input>
              </div>
            </div>
            <div classname='form-question'>
              <div className='form-question-label'>
                <label>Repeat Password</label>
              </div>
              <div className='form-input'>
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
        <div className='form-errors'>
          {errors.map((error, ind) => (
            <div key={ind}>{error}</div>
          ))}
        </div>
        <button type='submit'>Sign Up</button>
      </div>
      <DemoUserButton />
    </form>
  );
};

export default SignUpForm;
