import { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { getAllUserLikes, getAllLikedBy } from '../../store/likes';
import UserSquare from '../UserSquare';
import './MatchesContainer.css';

const MatchesContainer = () => {
  const dispatch = useDispatch();
  const loggedUser = useSelector((state) => state.session.user);
  const likesArray = useSelector((state) => {
    return state.likes?.likes && Object.values(state.likes?.likes);
  });
  const likedArray = useSelector((state) => {
    return state.likes?.likers && Object.values(state.likes?.likers);
  });

  const userLikes = likesArray;
  const userLikers = likedArray;

  let matchesArray = [];
  for (let i = 0; i < userLikes?.length; i++) {
    for (let j = 0; j < userLikers?.length; j++) {
      if (userLikes[i]?.id === userLikers[j]?.id) {
        matchesArray.push(userLikes[i]);
      }
    }
  }

  useEffect(() => {
    if (loggedUser) {
      dispatch(getAllUserLikes(loggedUser.id));
      dispatch(getAllLikedBy(Number(loggedUser.id)));
    }
  }, [dispatch, loggedUser]);

  return (
    <div>
      <h1> Matches </h1>
      <div className='outer-container'>
        <div className='users-container'>
          {matchesArray?.map((user) => (
            <div className='user-square'>
              <UserSquare user={user} key={user.id} />
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

export default MatchesContainer;
