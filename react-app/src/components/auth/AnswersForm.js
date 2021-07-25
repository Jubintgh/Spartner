import React, { useState } from 'react';
import { useSelector, useDispatch } from 'react-redux'
import { Redirect, useHistory } from 'react-router-dom';
import { createAnswer } from '../../store/answers';

const AnswersForm = () => {
  const [errors, setErrors] = useState([]);
  const [about, setAbout] = useState('');
  const [weightClass, setWeightClass] = useState(1);
  const [reach, setReach] = useState(50);
  const [professionalLevel, setProfessionalLevel] = useState(1);
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
  const [availability, setAvailability] = useState(1);
  const [rate, setRate] = useState(1);
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
      if(data.errors){
        let errs = Object.keys(data.errors)
        setErrors(errs)
      }
      else{
        history.push(`/discover`)
      }
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
        <div className="questionnaire-section-label">
          <h3>Since you're a coach, these fields are also required</h3>
      </div>
      <div className="form-actualForm-section">
        <div className="form-question">
          <div className="form-question-label">
          <label>Rate</label>
          </div>
          <div className="form-input">
          <input
            type='number'
            name='rate'
            onChange={updateRate}
            value={rate}
          ></input>
          </div>
        </div>
        <div className="form-question">
          <div className="form-question-label">
        <label>In Person Coaching</label>
          </div>
          <div className="form-input">
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
      </div>
      </div>
    )
  }

  let weightContent = null;

  if (gender === 1) {
    weightContent = (
      <div>
        <div className="form-question-label">
        <label>Weight Class</label>
          </div>
          <div className="form-input">    
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
      </div>
    )
  }

  else if (gender === 0) {
    weightContent = (
      <div>
        <div className="form-question-label">
        <label>Weight Class</label>
        </div>
        <div className="form-input">
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
      </div>
    )
  }

  else {
    weightContent = (
      <div>
        <div className="form-question-label">
        <label>Weight Class</label>
        </div>
        <div className="form-input">
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
      </div>
    )
  }


  return (
    <form onSubmit={onSubmit}>
      <div className="form-container">
        <div className="form-text-block">
          <div>
          <h1 className="questionnaire-title">Personality Questionnaire</h1>  
          </div>
          <div>
          <h2 className="questionnaire-subheader">Tell us a bit more about yourself</h2>  
          </div>
        </div>
        <div className="questionnaire-section-label">
          <h3>The following fields are required</h3>
        </div>
        <div className="form-actualForm-section">
      <div className="form-question">
        <div className="form-question-label">
        <label>About</label>
        </div>
        <div className="form-input">
        <input
          type='text'
          name='about'
          onChange={updateAbout}
          value={about}
          ></input>
        </div>
      </div>
      {weightContent}
      <div className="form-question">
      <div className="form-question-label">
        <label>Reach</label>
      </div>
      <div className="form-input">
        <input
          type='number'
          name='reach'
          onChange={updateReach}
          value={reach}
          required={true}
          ></input>
      </div>
      </div>
      <div className="form-question">
      <div className="form-question-label">
        <label>Professional Level</label>
</div>
<div className="form-input">
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
      </div>
        </div>
      { coachContent }
      <div className="questionnaire-section-label">
          <h3>The following fields are not required but will better suggest people you may be more compatible with</h3>
      </div>
      <div className="form-actualForm-section">

      <div className="form-question">
      <div className="form-question-label">
        <label>Walkout Song</label>
</div>
<div className="form-input">
        <input
          type='text'
          name='walkoutSong'
          onChange={updateWalkoutSong}
          value={walkoutSong}
          ></input>
</div>
      </div>
      <div className="form-question">
      <div className="form-question-label">
        <label>Current Record</label>
</div>
<div className="form-input">
        <input
          type='integer'
          name='currentRecord'
          onChange={updateCurrentRecord}
          value={currentRecord}
          ></input>
</div>
      </div>
      <div className="form-question">
      <div className="form-question-label">
        <label>Previous Titles Held</label>
</div>
<div className="form-input">
        <input
          type='boolean'
          name='previousTitles'
          onChange={updatePreviousTitles}
          value={previousTitles}
          ></input>
</div>
      </div>
      <div className="form-question">
      <div className="form-question-label">
        <label>Favorite Rocky Fighter</label>
</div>
<div className="form-input">
        <input
          type='string'
          name='favRockyFighter'
          onChange={updateFavRockyFighter}
          value={favRockyFighter}
          ></input>
</div>
      </div>
      <div className="form-question">
      <div className="form-question-label">
        <label>Vaccinated</label>
</div>
<div className="form-input">
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
      </div>
      <div className="form-question">
      <div className="form-question-label">
        <label>Has Kids</label>
</div>
<div className="form-input">
        <input
          type='boolean'
          name='hasKids'
          onChange={updateHasKids}
          value={hasKids}
          ></input>
</div>
      </div>
      <div className="form-question">
      <div className="form-question-label">
        <label>Pets</label>
</div>
<div className="form-input">
        <input
          type='text'
          name='pets'
          onChange={updatePets}
          value={pets}
          ></input>
</div>
      </div>
      <div className="form-question">
      <div className="form-question-label">
        <label>Nickname</label>
</div>
<div className="form-input">
        <input
          type='text'
          name='nickname'
          onChange={updateNickname}
          value={nickname}
          ></input>
</div>
      </div>
      <div className="form-question">
      <div className="form-question-label">
        <label>Religion</label>
</div>
<div className="form-input">
        <input
          type='text'
          name='religion'
          onChange={updateReligion}
          value={religion}
          ></input>
</div>
      </div>
      <div className="form-question">
      <div className="form-question-label">
          <label>Availability</label>
</div>
<div className="form-input">
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
      </div>
        </div>
      <button type='submit'>Submit Answers</button>
      </div>
        <div className="form-errors">
          {errors && errors.map(error => (
            <li key={error}>{error + " field is required"}</li>
          ))}

        </div>
    </form>
  );
};

export default AnswersForm;
