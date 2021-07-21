import React, { useState } from 'react';
import { useSelector, useDispatch } from 'react-redux'
import { Redirect, useHistory } from 'react-router-dom';
import { editAnswer } from '../../store/answers';

const EditAnswersForm = () => {
  const [errors, setErrors] = useState([]);
  const [about, setAbout] = useState('');
  const [weightClass, setWeightClass] = useState('');
  const [reach, setReach] = useState('');
  const [professionalLevel, setProfessionalLevel] = useState('');
  const [currentRecord, setCurrentRecord] = useState('0-0-0');
  const [previousTitles, setPreviousTitles] = useState('');
  const [favRockyFighter, setFavRockyFighter] = useState('');
  const [walkoutSong, setWalkoutSong] = useState('');
  const [vaccinated, setVaccinated] = useState('');
  const [hasKids, setHasKids] = useState('');
  const [inPerson, setInPerson] = useState('');
  const [nickname, setNickname] = useState('');
  const [religion, setReligion] = useState('');
  const [pets, setPets] = useState('');
  const [availability, setAvailability] = useState('');
  const [rate, setRate] = useState('');
  const user = useSelector(state => state.session.user);
  const history = useHistory();
  const dispatch = useDispatch();
  const isCoach = user.coach

  const onSubmit = async (e) => {
    e.preventDefault();
    const data = await dispatch(editAnswer(
      user_id=user.id,
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
      rate));
    if (data) {
      setErrors(data)
    }
    history.push('/discover')
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
          <label>Availability</label>
          <input
            type='text'
            name='availability'
            onChange={updateAvailability}
            value={availability}
          ></input>
        </div>
        <div>
          <label>Rate</label>
          <input
            type='integer'
            name='rate'
            onChange={updateRate}
            value={rate}
          ></input>
        </div>
      </div>
    )
  }


  return (
    <form onSubmit={onSubmit}>
      <div>
        {errors.map((error, ind) => (
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
      <div>
        <label>Weight Class</label>
        <input
          type='text'
          name='weightClass'
          onChange={updateWeightClass}
          value={weightClass}
          required={true}
        ></input>
      </div>
      <div>
        <label>Reach</label>
        <input
          type='integer'
          name='reach'
          onChange={updateReach}
          value={reach}
          required={true}
        ></input>
      </div>
        <div>
        <label>Professional Level</label>
        <input
          type='string'
          name='professionalLevel'
          onChange={updateProfessionalLevel}
          value={professionalLevel}
          required={true}
        ></input>
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
        <input
          type='text'
          name='vaccinated'
          onChange={updateVaccinated}
          value={vaccinated}
        ></input>
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
        <label>In Person Coaching</label>
        <input
          type='boolean'
          name='inPerson'
          onChange={updateInPerson}
          value={inPerson}
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
      { coachContent }
      <button type='submit'>Submit Answers</button>
    </form>
  );
};

export default EditAnswersForm;
