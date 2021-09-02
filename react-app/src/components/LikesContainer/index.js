import { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { getAllUserLikes } from '../../store/likes';
import { NavLink } from 'react-router-dom';
import UserSquare from '../UserSquare';
import './LikesContainer.css';

const LikesContainer = () => {
  const dispatch = useDispatch();
  const loggedUser = useSelector((state) => state.session.user);
  const likesArray = useSelector((state) => {
    return state.likes?.likes && Object.values(state.likes?.likes);
  });

  useEffect(() => {
    dispatch(getAllUserLikes(loggedUser.id));
  }, [dispatch, loggedUser.id]);

  return (
    <div>
      <div className='outer-container'>
        <h1> Liked Users </h1>
        <div className='users-container'>
          {likesArray?.map((user) => (
            <div className='user-square-container'>
              <NavLink to={`/users/${user.id}`}>
                <UserSquare user={user} key={user.id} />
              </NavLink>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

export default LikesContainer;
