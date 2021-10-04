import React, { useState, useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux'
import { useHistory } from 'react-router-dom';
import { getUserAnswers, editAnswer } from '../../store/answers';

const EditAnswersForm = () => {
  const user = useSelector(state => state.session.user);
  const answers = useSelector(state => state.answers.answer);


  const [errors, setErrors] = useState([]);
  const [about, setAbout] = useState(user.about);
  const [weightClass, setWeightClass] = useState(user.weightClass);
  const [reach, setReach] = useState(user.reach);
  const [professionalLevel, setProfessionalLevel] = useState(user.professionalLevel);
  const [currentRecord, setCurrentRecord] = useState(user.currentRecord);
  const [previousTitles, setPreviousTitles] = useState(user.previousTitles);
  const [favRockyFighter, setFavRockyFighter] = useState(user.favRockyFighter);
  const [walkoutSong, setWalkoutSong] = useState(user.walkoutSong);
  const [vaccinated, setVaccinated] = useState(user.vaccinated);
  const [hasKids, setHasKids] = useState(user.hasKids);
  const [inPerson, setInPerson] = useState(user.inPerson);
  const [nickname, setNickname] = useState(user.nickname);
  const [religion, setReligion] = useState(user.religion);
  const [pets, setPets] = useState(user.pets);
  const [availability, setAvailability] = useState(user.availability);
  const [rate, setRate] = useState(user.rate);
  const history = useHistory();
  const dispatch = useDispatch();
  const isCoach = user.coach;
  const gender = user.gender;
  const user_id = user.id

  const onSubmit = async (e) => {
    e.preventDefault();
    const data = await dispatch(editAnswer(
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

  useEffect(() => {
    dispatch(getUserAnswers(user.id))
  }, [dispatch, user])


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
          value={answers.about}
        ></input>
      </div>
      <div>
        <label>Walkout Song</label>
        <input
          type='text'
          name='walkoutSong'
          onChange={updateWalkoutSong}
          value={answers.walkoutSong}
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
      <button className='update_form-btn' type='submit'>Submit Answers</button>
    </form>
  );
};

export default EditAnswersForm;




// const user = useSelector(state => state.session.user);
//   const [errors, setErrors] = useState([]);
//   const [about, setAbout] = useState(user.answers.about);
//   const [weightClass, setWeightClass] = useState(user.answers.weightClass);
//   const [reach, setReach] = useState(user.answers.reach);
//   const [professionalLevel, setProfessionalLevel] = useState(user.answers.professionalLevel);
//   const [currentRecord, setCurrentRecord] = useState(user.answers.currentRecord);
//   const [previousTitles, setPreviousTitles] = useState(user.answers.previousTitles);
//   const [favRockyFighter, setFavRockyFighter] = useState(user.answers.favRockyFighter);
//   const [walkoutSong, setWalkoutSong] = useState(user.answers.walkoutSong);
//   const [vaccinated, setVaccinated] = useState(user.answers.vaccinated);
//   const [hasKids, setHasKids] = useState(user.answers.hasKids);
//   const [inPerson, setInPerson] = useState(user.answers.inPerson);
//   const [nickname, setNickname] = useState(user.answers.nickname);
//   const [religion, setReligion] = useState(user.answers.religion);
//   const [pets, setPets] = useState(user.answers.pets);
//   const [availability, setAvailability] = useState(user.answers.availability);
//   const [rate, setRate] = useState(user.answers.rate);
