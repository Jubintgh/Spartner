import React, { useState } from 'react';
import { useSelector, useDispatch } from 'react-redux'
import { useHistory } from 'react-router-dom';
import { editOneUser } from '../../store/users';

const EditUserForm = () => {
    const user = useSelector(state => state.session.user);
    const [errors, setErrors] = useState([]);
    const [username, setUsername] = useState(user.username);
    const [email, setEmail] = useState(user.email);
    const [password, setPassword] = useState(user.password);
    const [first_name, setFirstName] = useState(user.first_name);
    const [last_name, setLastName] = useState(user.last_name);
    const [age, setAge] = useState(user.age);
    const [location, setLocation] = useState(user.location);
    const [gender, setGender] = useState(user.gender);
    const [coach, setCoach] = useState(user.coach);
    const [img_url, setImageUrl] = useState(user.img_url);
    const [discipline, setDiscipline] = useState(user.discipline);
    const dispatch = useDispatch();
    const history = useHistory();
    const userId = user.id

    const onSubmit = async (e) => {
        e.preventDefault()
        const data = await dispatch(editOneUser(
        userId,
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
            history.push(`/users/${userId}`)
        }
    };

    const handleCancelClick = (e) => {
        e.preventDefault();
        history.push(`/users/${userId}`)
    }

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

    return (
    <form onSubmit={onSubmit}>
      <div className="form-container">
        <div className="form-actualForm">
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
      </div>
      <div className="form-half">
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
          <option value="">Select</option>
          <option value="0">Female</option>
          <option value="1">Male</option>
          <option value="2">Other</option>
        </select>
      </div>
      </div>
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
          <option value="">Select</option>
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
        </div>
        </div>
      <div className="form-errors">
        {errors.map((error, ind) => (
          <div key={ind}>{error}</div>
        ))}
      </div>
      <button className='updateButton' type='submit'>Update</button>
      <button type="button" onClick={handleCancelClick}>Cancel</button>
      </div>
        {/* <div>
        {errors?.map((error, ind) => (
            <div key={ind}>{error}</div>
        ))}
        </div>
        <div>
        <label>User Name</label>
        <input
            type='text'
            name='username'
            onChange={updateUsername}
            value={username}
        ></input>
        </div>
        <div>
        <label>First Name</label>
        <input
            type='text'
            name='firstName'
            onChange={updateFirstName}
            value={first_name}
        ></input>
        </div>
        <div>
        <label>Last Name</label>
        <input
            type='text'
            name='lastName'
            onChange={updateLastName}
            value={last_name}
        ></input>
        </div>
        <div>
        <label>Age</label>
        <input
            type='number'
            name='age'
            onChange={updateAge}
            value={age}
        ></input>
        </div>
        <div>
        <label>Location</label>
        <input
            type='text'
            name='location'
            onChange={updateLocation}
            value={location}
        ></input>
        </div>
        <div>
        <label>Gender</label>
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
        <div>
        <label>Coach</label>
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
        <div>
        <label>Image URL</label>
        <input
            type='text'
            name='imageurl'
            onChange={updateImageUrl}
            value={img_url}
        ></input>
        </div>
        <div>
        <label>Email</label>
        <input
            type='text'
            name='email'
            onChange={updateEmail}
            value={email}
        ></input>
        </div>
        <div>
        <label>Discipline</label>
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
        <button type="submit">Update Your Spartner Profile</button>
        <button type="button" onClick={handleCancelClick}>Cancel</button> */}
    </form>
    );
};

export default EditUserForm;
