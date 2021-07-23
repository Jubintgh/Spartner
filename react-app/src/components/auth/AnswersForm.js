import React, { useState } from 'react';
import { useSelector, useDispatch } from 'react-redux'
import { Redirect, useHistory } from 'react-router-dom';
import { createAnswer } from '../../store/answers';

const AnswersForm = () => {
  const [errors, setErrors] = useState([]);
  const [about, setAbout] = useState('');
  const [weightClass, setWeightClass] = useState(0);
  const [reach, setReach] = useState(50);
  const [professionalLevel, setProfessionalLevel] = useState(0);
  const [currentRecord, setCurrentRecord] = useState('0-0-0');
  const [previousTitles, setPreviousTitles] = useState('');
  const [favRockyFighter, setFavRockyFighter] = useState('');
  const [walkoutSong, setWalkoutSong] = useState('');
  const [vaccinated, setVaccinated] = useState('');
  const [hasKids, setHasKids] = useState('');
  const [inPerson, setInPerson] = useState(true);
  const [nickname, setNickname] = useState('');
  const [religion, setReligion] = useState('');
  const [pets, setPets] = useState('');
  const [availability, setAvailability] = useState(0);
  const [rate, setRate] = useState('');
  const user = useSelector(state => state.session.user);
  const history = useHistory();
  const dispatch = useDispatch();
  const isCoach = user?.coach;
  const gender = user?.gender;
  const user_id = user?.id;

  const onSubmit = async (e) => {
    e.preventDefault();
    const data = await dispatch(createAnswer(
      user_id,
      about,
      weightClass,
      reach,
      professionalLevel,
      currentRecord,
      previousTitles,
      favRockyFighter,
      walkoutSong,
      vaccinated,
      hasKids,
      inPerson,
      nickname,
      religion,
      pets,
      availability,
      rate ));
    if (data) {
      setErrors(data)
      history.push(`/discover`)
    }
  };

  const updateAbout = (e) => {
    setAbout(e.target.value);
  };

  const updateWeightClass = (e) => {
    setWeightClass(e.target.value);;
  };

  const updateReach = (e) => {
    setReach(e.target.value);
  };

  const updateProfessionalLevel = (e) => {
    setProfessionalLevel(e.target.value);
  };

  const updateCurrentRecord = (e) => {
    setCurrentRecord(e.target.value);
  };

  const updatePreviousTitles = (e) => {
    setPreviousTitles(e.target.value);
  };

  const updateFavRockyFighter = (e) => {
    setFavRockyFighter(e.target.value);
  };

  const updateWalkoutSong = (e) => {
    setWalkoutSong(e.target.value);
  };

  const updateVaccinated = (e) => {
    setVaccinated(e.target.value);
  };

  const updateHasKids = (e) => {
    setHasKids(e.target.value);
  };

  const updateInPerson = (e) => {
    setInPerson(e.target.value);
  };

  const updateNickname = (e) => {
    setNickname(e.target.value);
  };
  const updateReligion = (e) => {
    setReligion(e.target.value);
  };
  const updatePets = (e) => {
    setPets(e.target.value);
  };
  const updateAvailability = (e) => {
    setAvailability(e.target.value);
  };

  const updateRate = (e) => {
    setRate(e.target.value);
  };

  let coachContent = null;

  if (isCoach) {
    coachContent = (
      <div>
        <div>
          <label>Rate</label>
          <input
            type='number'
            name='rate'
            onChange={updateRate}
            value={rate}
          ></input>
        </div>
        <div>
        <label>In Person Coaching</label>
        <select
          type='boolean'
          name='inPerson'
          onChange={updateInPerson}
          value={inPerson}
        >
          <option value="False">Online</option>
          <option value="True">In Person</option>
        </select>
      </div>
      </div>
    )
  }

  let weightContent = null;

  if (gender === 1) {
    weightContent = (
      <div>
        <label>Weight Class</label>
        <select
          type='number'
          name='weightClass'
          onChange={updateWeightClass}
          value={weightClass}
          required={true}
        >
          <option value="0">Lightweight</option>
          <option value="1">Middleweight</option>
          <option value="2">Heavyweight</option>
        </select>
      </div>
    )
  }

  else if (gender === 0) {
    weightContent = (
      <div>
        <label>Weight Class</label>
        <select
          type='number'
          name='weightClass'
          onChange={updateWeightClass}
          value={weightClass}
          required={true}
        >
          <option value="3">Women's Flyweight</option>
          <option value="4">Women's Straweight</option>
          <option value="5">Women's Featherweight</option>
          <option value="6">Women's Bantamweight</option>
        </select>
      </div>
    )
  }

  else {
    weightContent = (
      <div>
        <label>Weight Class</label>
        <select
          type='number'
          name='weightClass'
          onChange={updateWeightClass}
          value={weightClass}
          required={true}
        >
          <option value="0">Lightweight</option>
          <option value="1">Middleweight</option>
          <option value="2">Heavyweight</option>
          <option value="3">Women's Flyweight</option>
          <option value="4">Women's Straweight</option>
          <option value="5">Women's Featherweight</option>
          <option value="6">Women's Bantamweight</option>
        </select>
      </div>
    )
  }


  return (
    <form onSubmit={onSubmit}>
      <div>
        {errors?.map((error, ind) => (
          <div key={ind}>{error}</div>
        ))}
      </div>
      <div>
        <label>About</label>
        <input
          type='text'
          name='about'
          onChange={updateAbout}
          value={about}
        ></input>
      </div>
      <div>
        <label>Walkout Song</label>
        <input
          type='text'
          name='walkoutSong'
          onChange={updateWalkoutSong}
          value={walkoutSong}
        ></input>
      </div>
      {weightContent}
      <div>
        <label>Reach</label>
        <input
          type='number'
          name='reach'
          onChange={updateReach}
          value={reach}
          required={true}
        ></input>
      </div>
      <div>
        <label>Professional Level</label>
        <select
          type='integer'
          name='professionalLevel'
          onChange={updateProfessionalLevel}
          value={professionalLevel}
          required={true}
        >
          <option value="0">Beginner</option>
          <option value="1">Amateur</option>
          <option value="2">Professional</option>
        </select>
      </div>
      <div>
        <label>Current Record</label>
        <input
          type='integer'
          name='currentRecord'
          onChange={updateCurrentRecord}
          value={currentRecord}
        ></input>
      </div>
      <div>
        <label>Previous Titles Held</label>
        <input
          type='boolean'
          name='previousTitles'
          onChange={updatePreviousTitles}
          value={previousTitles}
        ></input>
      </div>
      <div>
        <label>Favorite Rocky Fighter</label>
        <input
          type='string'
          name='favRockyFighter'
          onChange={updateFavRockyFighter}
          value={favRockyFighter}
        ></input>
      </div>
      <div>
        <label>Vaccinated</label>
        <select
          type='text'
          name='vaccinated'
          onChange={updateVaccinated}
          value={vaccinated}
        >
          <option value="False">Not vaccinated</option>
          <option value="True">Vaccinated</option>
        </select>
      </div>
      <div>
        <label>Has Kids</label>
        <input
          type='boolean'
          name='hasKids'
          onChange={updateHasKids}
          value={hasKids}
        ></input>
      </div>
      <div>
        <label>Pets</label>
        <input
          type='text'
          name='pets'
          onChange={updatePets}
          value={pets}
        ></input>
      </div>
      <div>
        <label>Nickname</label>
        <input
          type='text'
          name='nickname'
          onChange={updateNickname}
          value={nickname}
        ></input>
      </div>
      <div>
        <label>Religion</label>
        <input
          type='text'
          name='religion'
          onChange={updateReligion}
          value={religion}
        ></input>
      </div>
      <div>
          <label>Availability</label>
          <select
            type='text'
            name='availability'
            onChange={updateAvailability}
            value={availability}
          >
            <option value="0">Weekends</option>
            <option value="1">Weekdays</option>
            <option value="2">All week</option>
          </select>
        </div>
      { coachContent }
      <button type='submit'>Submit Answers</button>
    </form>
  );
};

export default AnswersForm;
