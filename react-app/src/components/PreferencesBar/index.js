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
          <img className='coachIcon' src='https://user-images.githubusercontent.com/35717793/131560451-2c296a54-a8b1-4a83-8a3a-29d56e37dda0.png' />
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
            <img className='redommendedIcon' src='https://user-images.githubusercontent.com/35717793/131560454-cc0aa895-6dee-43d9-bbf1-6e1386cc3e2f.png' />
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
              src='https://user-images.githubusercontent.com/35717793/131560503-eb17a1a6-7752-43ea-9530-fc4f580f0c04.png'
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
            <img className='vaxIcon' src='https://user-images.githubusercontent.com/35717793/131560483-baff9f92-757d-47e4-8e6b-ce0c26a46901.png' />
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
            <img className='proLevelIcon' src='https://user-images.githubusercontent.com/35717793/131560470-a1bcbc70-1bf0-4a8b-b7b7-c79bbedddd43.png' />
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
