import React, { useState, useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux'
import { useHistory } from 'react-router-dom';
import { getUserAnswers, editAnswer } from '../../store/answers';

const EditAnswersForm = () => {
  const user = useSelector(state => state.session.user);
  const answers = useSelector(state => state.answers.answer ? state.answers.answer : {});
  const dispatch = useDispatch();
  
  const [errors, setErrors] = useState([]);
  const [about, setAbout] = useState(answers?.about);
  const [availability, setAvailability] = useState(answers?.availability);
  const [currentRecord, setCurrentRecord] = useState(answers?.currentRecord);
  const [favRockyFighter, setFavRockyFighter] = useState(answers?.favRockyFighter);
  const [hasKids, setHasKids] = useState(answers?.hasKids);
  const [nickname, setNickname] = useState(answers?.nickname);
  const [pets, setPets] = useState(answers?.pets);
  const [previousTitles, setPreviousTitles] = useState(answers?.previousTitles);
  const [professionalLevel, setProfessionalLevel] = useState(answers?.professionalLevel);
  const [rate, setRate] = useState(answers?.rate);
  const [reach, setReach] = useState(answers?.reach);
  const [religion, setReligion] = useState(answers?.religion);
  const [vaccinated, setVaccinated] = useState(answers?.vaccinated);
  const [walkoutSong, setWalkoutSong] = useState(answers?.walkoutSong);
  const [weightClass, setWeightClass] = useState(answers?.weightClass);
  const [inPerson, setInPerson] = useState(answers?.inPerson);
  
  const history = useHistory();
  const isCoach = user.coach;
  const gender = user.gender;
  const user_id = user.id

  const onSubmit = async (e) => {
    e.preventDefault();

    const data = await dispatch(editAnswer(user.id, {
      user_id,
      about,
      weightClass : answers.weight_class,
      reach : answers.reach,
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
      rate }));
    console.log(data, 'DATAAASDDSAD')
    if (data.errors) {
      setErrors(data)
      // history.push(`/discover`)
    }
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
            onChange={setRate(e => e.target.value)}
            value={rate}
          ></input>
        </div>
        <div>
        <label>In Person Coaching</label>
        <select
          type='boolean'
          name='inPerson'
          onChange={setInPerson(e => e.target.value)}
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
          onChange={e => setWeightClass(e.target.value)}
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
          onChange={setWeightClass(e => e.target.value)}
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
          onChange={setWeightClass(e => e.target.value)}
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
    if(!answers.about){
      dispatch(getUserAnswers(user.id))
    }
    // console.log(answers)
  },[dispatch, answers, user])
  
  return (
    <form onSubmit={onSubmit}>
      <div>
        {/* {errors?.map((error, ind) => (
          <div key={ind}>{error}</div>
        ))} */}
        {
          errors && console.log(errors)
        }
      </div>
      <div>
        <label>About</label>
        <input
          type='text'
          name='about'
          onChange={e => setAbout(e.target.value)}
          //defaultValue={answers.about}
        ></input>
      </div>
      <div>
        <label>Walkout Song</label>
        <input
          type='text'
          name='walkoutSong'
          onChange={e => setWalkoutSong(e.target.value)}
          //defaultValue={answers.walkout_song}
        ></input>
      </div>
      {weightContent}
      <div>
        <label>Reach</label>
        <input
          type='number'
          name='reach'
          onChange={e => setReach(e.target.value)}
          //defaultValue={answers.reach}
          required={true}
        ></input>
      </div>
      <div>
        <label>Professional Level</label>
        <select
          type='integer'
          name='professionalLevel'
          onChange={e => setProfessionalLevel(e.target.value)}
          //defaultValue={answers.professional_level}
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
          onChange={e => setCurrentRecord(e.target.value)}
          ////defaultValue={answers.current_record}
        ></input>
      </div>
      <div>
        <label>Previous Titles Held</label>
        <input
          type='boolean'
          name='previousTitles'
          onChange={e => setPreviousTitles(e.target.value)}
          //defaultValue={answers.previous_titles}
        ></input>
      </div>
      <div>
        <label>Favorite Rocky Fighter</label>
        <input
          type='string'
          name='favRockyFighter'
          onChange={e => setFavRockyFighter(e.target.value)}
          //defaultValue={answers.fav_rocky_fighter}
        ></input>
      </div>
      <div>
        <label>Vaccinated</label>
        <select
          type='text'
          name='vaccinated'
          onChange={e => setVaccinated(e.target.value)}
          //defaultValue={answers.vaccinated}
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
          onChange={e => setHasKids(e.target.value)}
          //defaultValue={answers.has_kids}
        ></input>
      </div>
      <div>
        <label>Pets</label>
        <input
          type='text'
          name='pets'
          onChange={e => setPets(e.target.value)}
          //defaultValue={answers.pets}
        ></input>
      </div>
      <div>
        <label>Nickname</label>
        <input
          type='text'
          name='nickname'
          onChange={ e => setNickname(e.target.value)}
          //defaultValue={answers.nickname}
        ></input>
      </div>
      <div>
        <label>Religion</label>
        <input
          type='text'
          name='religion'
          onChange={e => setReligion(e.target.value)}
          //defaultValue={answers.religion}
        ></input>
      </div>
      <div>
          <label>Availability</label>
          <select
            type='text'
            name='availability'
            onChange={e => setAvailability(e.target.value)}
            //defaultValue={answers.availability}
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