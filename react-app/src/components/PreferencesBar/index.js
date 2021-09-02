import { useState, useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { getFilteredUsers } from '../../store/discover';
import './PreferenceBar.css';

const PreferencesBar = ({ notification }) => {
  const dispatch = useDispatch();
  const user = useSelector((state) => state.session.user);
  const users = useSelector((state) => Object.values(state.users));
  const userId = user?.id;
  const isCoach = user?.coach;

  // button stuff here

  const [filter, setFilter] = useState();

  let renderCoachContent = null;

  if (!isCoach) {
    renderCoachContent = (
      <div className='prefBar-element'>
        <div className='prefBar-icon' onClick={(e) => setFilter('coach')}>
          <img className='coachIcon' src='/coachIcon-static.png' alt='' />
        </div>
        <div className='prefBar-icon-label'>
          <h5>Coaches</h5>
        </div>
      </div>
    );
  }

  let filterAppliedLabel = null;
  if (filter === 'coach') {
    filterAppliedLabel = <h2>Coach</h2>;
  } else if (filter === 'weight-class') {
    filterAppliedLabel = <h2>Weight Class</h2>;
  } else if (filter === 'vaccination') {
    filterAppliedLabel = <h2>Vaccinated</h2>;
  } else if (filter === 'professional-level') {
    filterAppliedLabel = <h2>Professional Level</h2>;
  } else {
    filterAppliedLabel = <h2>Recommended</h2>;
  }

  useEffect(() => {
    dispatch(getFilteredUsers(userId, filter));
  }, [filter]);

  return (
    <div className='prefBar-container'>
      <div className='prefBar-block'>
        <div className='prefBar-element'>
          <div
            className='prefBar-icon'
            onClick={(e) => setFilter('recommended')}
          >
            <img className='redommendedIcon' src='/fight-static.png' />
          </div>
          <div className='prefBar-icon-label'>
            <h5>Recommended</h5>
          </div>
        </div>
        <div className='prefBar-element'>
          <div
            className='prefBar-icon'
            onClick={(e) => setFilter('weight-class')}
          >
            <img
              className='weightClassIcon'
              src='/weightclassIcon-static.png'
            />
          </div>
          <div className='prefBar-icon-label'>
            <h5>Weight Class</h5>
          </div>
        </div>
        <div className='prefBar-element'>
          <div
            className='prefBar-icon'
            onClick={(e) => setFilter('vaccination')}
          >
            <img className='vaxIcon' src='/vax-static.png' />
          </div>
          <div className='prefBar-icon-label'>
            <h5>Vaccinated</h5>
          </div>
        </div>
        <div className='prefBar-element'>
          <div
            className='prefBar-icon'
            onClick={(e) => setFilter('professional-level')}
          >
            <img className='proLevelIcon' src='/proIcon-static.png' />
          </div>
          <div className='prefBar-icon-label'>
            <h5>Professional Level</h5>
          </div>
        </div>
        {renderCoachContent}
      </div>
      {filterAppliedLabel}
    </div>
  );
};

export default PreferencesBar;
