import './DiscoverPage.css';
import { React } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { Link } from 'react-router-dom';
import { useEffect, useState } from 'react';
import { getNewUsers, removeUser } from '../../store/discover';
import { createLike } from '../../store/likes';
import { getCurrentUserAndAnswers } from '../../store/session';
import { createDislike } from '../../store/dislikes';
import { MdKeyboardArrowRight } from 'react-icons/md';
import { GiConsoleController, GiWeight } from 'react-icons/gi';
import { FiUser, FiMapPin } from 'react-icons/fi';
import { FaQuestionCircle } from 'react-icons/fa';
import { getAllLikedBy } from '../../store/likes';
import MatchNotification from '../MatchNotification';
import PreferencesBar from '../../components/PreferencesBar';

const DiscoverPage = () => {
  const dispatch = useDispatch();
  const [notification, setNotification] = useState(false);
  const [clicked, setClicked] = useState(false);
  const allUsersNotLiked = useSelector((state) =>
    Object.values(state.discover)
  );
  const likedArray = useSelector((state) => {
    return state.likes?.likers;
  });
  const { user } = useSelector((state) => state.session);
  const id = Number(user.id);
  const firstUser = allUsersNotLiked[0];
  const [likeButton, setLikeButton] = useState(
    'https://user-images.githubusercontent.com/35717793/131560710-8ab4eac9-9a09-4c21-98f7-5d09dd545ad3.png'
  );
  const [dislikeButton, setDislikeButton] = useState(
    'https://user-images.githubusercontent.com/35717793/131560719-0d1acee6-a0c9-4182-aab5-555b80e4771c.png'
  );
  const [swipeDirection, setSwipeDirection] = useState('');
  const [show, setShow] = useState(false);

  const handleClickDislike = () => {
    dispatch(createDislike(id, firstUser?.id));
    setSwipeDirection('left');
    setTimeout(function () {
      dispatch(removeUser(firstUser));
    }, 800);
    setTimeout(function () {
      setSwipeDirection('');
    }, 1000);
  };

  const handleClickLike = () => {
    setClicked(true);
    dispatch(createLike(id, firstUser?.id));
    setSwipeDirection('right');
    setTimeout(function () {
      dispatch(removeUser(firstUser));
    }, 800);
    setTimeout(function () {
      setSwipeDirection('');
    }, 1000);
  };

  useEffect(() => {
    if (firstUser && likedArray) {
      if (Number(firstUser.id) in likedArray && clicked) {
        setNotification(true);
        setTimeout(function () {
          setClicked(false);
          setNotification(false);
        }, 2000);
      }
    }
  }, [notification, firstUser, clicked, likedArray]);

  const changeImageSourceLiked = () => {
    if (
      likeButton ===
      'https://user-images.githubusercontent.com/35717793/131560710-8ab4eac9-9a09-4c21-98f7-5d09dd545ad3.png'
    ) {
      setLikeButton(
        'https://user-images.githubusercontent.com/35717793/131561660-54793b25-6e24-4ceb-89d6-b13b97625361.png'
      );
    } else {
      setLikeButton(
        'https://user-images.githubusercontent.com/35717793/131560710-8ab4eac9-9a09-4c21-98f7-5d09dd545ad3.png'
      );
    }
  };

  const changeImageSourceDisliked = () => {
    if (
      dislikeButton ===
      'https://user-images.githubusercontent.com/35717793/131560719-0d1acee6-a0c9-4182-aab5-555b80e4771c.png'
    ) {
      setDislikeButton(
        'https://user-images.githubusercontent.com/35717793/131561652-ca11d430-33b1-47c2-ac49-1ca3efe93ec6.png'
      );
    } else {
      setDislikeButton(
        'https://user-images.githubusercontent.com/35717793/131560719-0d1acee6-a0c9-4182-aab5-555b80e4771c.png'
      );
    }
  };

  useEffect(() => {}, [show]);

  useEffect(() => {
    dispatch(getNewUsers(id));
    dispatch(getCurrentUserAndAnswers(id));
    dispatch(getAllLikedBy(id));
  }, [dispatch, id]);

  let weightClass;
  if (Number(firstUser?.weight_class) === 0)
    weightClass = "Women's Strawweight";
  if (Number(firstUser?.weight_class) === 1)
    weightClass = "Women's Bantamweight";
  if (Number(firstUser?.weight_class) === 2)
    weightClass = "Women's Featherweight";
  if (Number(firstUser?.weight_class) === 3)
    weightClass = "Women's Lightweight";
  if (Number(firstUser?.weight_class) === 4) weightClass = 'Lightweight';
  if (Number(firstUser?.weight_class) === 5) weightClass = 'Middleweight';
  if (Number(firstUser?.weight_class) === 6) weightClass = 'Heavyweight';

  let gender;
  if (Number(firstUser?.gender) === 0) {
    gender = 'Female';
  } else if (Number(firstUser?.gender) === 1) {
    gender = 'Male';
  } else {
    gender = 'Other';
  }

  const createMatchPercentage = () => {
    let total = 0;

    if (user.gender === firstUser?.gender) {
      total += 49;
    } else if (Number(firstUser?.gender) === 2) {
      total += 33;
    } else {
      total += 0;
    }
    if (user.location.split(',')[1] === firstUser?.location.split(',')[1])
      total += 22;
    if (user.weight_class === firstUser?.weight_class) total += 11;
    if (user.professional_level === firstUser?.professional_level) total += 8;
    if (user.availability === firstUser?.availability) total += 4;
    if (user.reach === firstUser?.reach) total += 1;
    if (user.vaccinated === firstUser?.vaccinated) total += 3;
    if (user.discipline === firstUser?.discipline) total += 2;

    return total;
  };

  let usersLeftOrNoUsers;
  if (allUsersNotLiked.length === 0) {
    usersLeftOrNoUsers = (
      <div className='outOfUsers'>
        <h2>No more users to swipe!</h2>
      </div>
    );
  } else {
    usersLeftOrNoUsers = (
      <div className='main-area-container'>
        <div className='discover-title'>
          <PreferencesBar notification={notification} />
        </div>
        {notification ? (
          <div className='notification-wrapper'>
            <MatchNotification />
          </div>
        ) : null}
        <div className={`user-info-container ${swipeDirection}`}>
          <div className='top-row'>
            <div className='user-info'>
              <div className='full-name'>
                <p className='first-name'>{firstUser?.first_name}</p>
                <p className='last-name'>{firstUser?.last_name}</p>
              </div>
              <p>|</p>
              <p>{createMatchPercentage()}% Compatibility </p>
              <p
                onMouseEnter={() => setShow(true)}
                onMouseLeave={() => setShow(false)}
                className={show ? 'tooltip-icon active' : 'tooltip-icon'}
              >
                <FaQuestionCircle />
              </p>
              <div
                className={
                  show
                    ? 'tooltip-outer-container'
                    : 'tooltip-outer-container hidden'
                }
              >
                <div
                  className={show ? 'left-arrow' : 'left-arrow hidden'}
                ></div>
                <div
                  className={
                    show ? 'tooltip-container' : 'tooltip-container hidden'
                  }
                >
                  <p className={show ? 'tooltip-text' : 'tooltip-text hidden'}>
                    This percentage is calculated based upon how many answers
                    you and the other use have in common from the personality
                    questionnaire.
                  </p>
                </div>
              </div>
              <p>|</p>
              <Link
                to={`/users/${firstUser?.id}`}
                className='view-profile-link'
              >
                View Profile <MdKeyboardArrowRight className='arrow-link' />
              </Link>
            </div>
            <div className='discover-btns'>
              <div onClick={handleClickDislike} className='pass-btn'>
                <img
                  className={`discover-button`}
                  src={dislikeButton}
                  onMouseDown={changeImageSourceDisliked}
                  onMouseUp={changeImageSourceDisliked}
                  alt=''
                />
              </div>
              <div onClick={handleClickLike} className='like-btn'>
                <img
                  className='discover-button'
                  src={likeButton}
                  onMouseDown={changeImageSourceLiked}
                  onMouseUp={changeImageSourceLiked}
                  alt=''
                />
              </div>
            </div>
          </div>
          <div className='user-picture'>
            <img
              alt=''
              src={
                firstUser?.img_url === 'inTheWorks.jpg'
                  ? 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_1280.png'
                  : firstUser?.img_url
              }
              className='user-img'
            ></img>
          </div>
        </div>
        <div className={`bio-container ${swipeDirection}`}>
          <div className='bio-left'>
            <div className='about-me'>
              <h3>About Me</h3>
              <p>{firstUser?.about}</p>
            </div>
          </div>
          <div className='bio-right'>
            <div className='gender'>
              <FiUser className='bio-right-icon' />
              <p>{gender}</p>
            </div>
            <div className='location'>
              <FiMapPin className='bio-right-icon' />
              <p>{firstUser?.location}</p>
            </div>
            <div className='weightclass'>
              <GiWeight className='bio-right-icon' />
              <p>{weightClass}</p>
            </div>
          </div>
        </div>
      </div>
    );
  }
  return <div className='discover-page'>{usersLeftOrNoUsers}</div>;
};

export default DiscoverPage;
