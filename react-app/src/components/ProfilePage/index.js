import './ProfilePage.css';
import { useSelector, useDispatch } from 'react-redux';
import { useParams, useHistory, Link } from 'react-router-dom';
import { useEffect, useState } from 'react';
import { getOneUser } from '../../store/users';
import { getNewUsers, removeUser } from '../../store/discover';
import { createLike, getAllUserLikes } from '../../store/likes';
import { createDislike } from '../../store/dislikes';
import { GiWeight, GiCage, GiBoxingGlove } from 'react-icons/gi';
import { BiRuler, BiMedal } from 'react-icons/bi';
import { VscGraph } from 'react-icons/vsc';
import { FiUser, FiMapPin } from 'react-icons/fi';

const ProfilePage = () => {
  const dispatch = useDispatch();
  const history = useHistory();
  const { userId } = useParams();
  const firstUser = useSelector((state) => state.users[userId]);
  const { user } = useSelector((state) => state.session);
  const id = Number(user.id);
  const userLikesObj = useSelector((state) => state.likes.likes);
  const userLikes = userLikesObj?.user_likes;

  const [likeButton, setLikeButton] = useState('/like-button-unclicked.png');
  const [dislikeButton, setDislikeButton] = useState(
    '/dislike-button-unclicked.png'
  );
  const [swipeDirection, setSwipeDirection] = useState('');

  const handleClickDislike = () => {
    dispatch(createDislike(id, firstUser?.id));
    setSwipeDirection('left');
    setTimeout(function () {
      dispatch(removeUser(firstUser));
    }, 800);
    setTimeout(function () {
      setSwipeDirection('');
      history.push('/discover');
    }, 1000);
  };

  const handleClickLike = () => {
    dispatch(createLike(id, firstUser?.id));
    setSwipeDirection('right');
    setTimeout(function () {
      dispatch(removeUser(firstUser));
    }, 800);
    setTimeout(function () {
      setSwipeDirection('');
      history.push('/discover');
    }, 1000);
  };

  const changeImageSourceLiked = () => {
    if (likeButton === '/like-button-clicked.png') {
      setLikeButton('/like-button-unclicked.png');
    } else {
      setLikeButton('/like-button-clicked.png');
    }
  };

  const changeImageSourceDisliked = () => {
    if (dislikeButton === '/dislike-button-clicked.png') {
      setDislikeButton('/dislike-button-unclicked.png');
    } else {
      setDislikeButton('/dislike-button-clicked.png');
    }
  };

  useEffect(() => {
    dispatch(getNewUsers(id));
    dispatch(getOneUser(userId));
  }, [dispatch, id, userId]);

  let available;
  if (Number(firstUser?.availability) === 0) {
    available = 'All Week';
  } else if (Number(firstUser?.availability) === 1) {
    available = 'Week Days';
  } else {
    available = 'Weekends';
  }

  let weightClass;
  if (Number(firstUser?.weight_class) === 0) {
    weightClass = "Women's Strawweight";
  } else if (Number(firstUser?.weight_class) === 1) {
    weightClass = "Women's Bantamweight";
  } else if (Number(firstUser?.weight_class) === 2) {
    weightClass = "Women's Featherweight";
  } else if (Number(firstUser?.weight_class) === 3) {
    weightClass = "Women's Lightweight";
  } else if (Number(firstUser?.weight_class) === 4) {
    weightClass = 'Lightweight';
  } else if (Number(firstUser?.weight_class) === 5) {
    weightClass = 'Middleweight';
  } else {
    weightClass = 'Heavyweight';
  }

  let discipline;
  if (Number(firstUser?.discipline) === 0) discipline = 'Southpaw';
  if (Number(firstUser?.discipline) === 1) discipline = 'Kickboxing';
  if (Number(firstUser?.discipline) === 2) discipline = 'Orthodox';
  if (Number(firstUser?.discipline) === 3) discipline = 'Judo';
  if (Number(firstUser?.discipline) === 4) discipline = 'Muay Thai';
  if (Number(firstUser?.discipline) === 5) discipline = 'Grappling';
  if (Number(firstUser?.discipline) === 6) discipline = 'Counter Striker';
  if (Number(firstUser?.discipline) === 7) discipline = 'Karate';
  if (Number(firstUser?.discipline) === 8) discipline = 'Switch';
  if (Number(firstUser?.discipline) === 9) discipline = 'Brazilian Jiu-Jitsu';

  let professionalLevel;
  if (Number(firstUser?.professional_level) === 0) {
    professionalLevel = 'Beginner';
  } else if (Number(firstUser?.professional_level) === 1) {
    professionalLevel = 'Amateur';
  } else {
    professionalLevel = 'Professional';
  }

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

    if (user?.gender === firstUser?.gender) {
      total += 49;
    } else if (Number(firstUser?.gender) === 2) {
      total += 33;
    } else {
      total += 0;
    }
    if (user?.location.split(',')[1] === firstUser?.location.split(',')[1])
      total += 22;
    if (user?.weight_class === firstUser?.weight_class) total += 11;
    if (user?.professional_level === firstUser?.professional_level) total += 8;
    if (user?.availability === firstUser?.availability) total += 4;
    if (user?.reach === firstUser?.reach) total += 1;
    if (user?.vaccinated === firstUser?.vaccinated) total += 3;
    if (user?.discipline === firstUser?.discipline) total += 2;

    return total + '% Compatability';
  };

  let loggedInUserHeaderOrOtherUserHeader;
  if (Number(firstUser?.id) !== Number(id)) {
    loggedInUserHeaderOrOtherUserHeader = (
      <div className='discover-title'>
        <h2>
          {firstUser?.first_name} {firstUser?.last_name}'s Profile
        </h2>
      </div>
    );
  } else {
    loggedInUserHeaderOrOtherUserHeader = (
      <div className='discover-title'>
        <h2>Your Profile</h2>
      </div>
    );
  }

  let currentUserPageOrDifferentUserPage;
  if (Number(firstUser?.id) !== Number(id)) {
    currentUserPageOrDifferentUserPage = (
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
    );
  } else {
    console.log('Hello');
    currentUserPageOrDifferentUserPage = (
      <div className='profile-edit-links'>
        <div>
          <Link to={`/users/${id}/edit-info`}>Edit Info</Link>
        </div>
        <div>|</div>
        <div>
          <Link to={`/users/${id}/edit-answers`}>Edit Answers</Link>
        </div>
      </div>
    );
  }

  return (
    <div className='discover-page'>
      <div className='main-area-container'>
        {loggedInUserHeaderOrOtherUserHeader}
        <div className={`user-info-container ${swipeDirection}`}>
          <div className='top-row'>
            <div className='user-info full-profile'>
              <div className='full-name'>
                <p className='first-name'>{firstUser?.first_name}</p>
                <p className='last-name'>{firstUser?.last_name}</p>
              </div>
              <p>{Number(firstUser?.id) !== Number(id) ? '|' : null}</p>
              <p>
                {Number(firstUser?.id) !== Number(id)
                  ? createMatchPercentage()
                  : null}
              </p>
            </div>
            {currentUserPageOrDifferentUserPage}
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
        <div className={`bio-container ${swipeDirection} full-profile`}>
          <div className='bio-left'>
            <div className='about-me'>
              <h3>About Me</h3>
              <p>{firstUser?.about}</p>
            </div>
            {firstUser?.fav_rocky_fighter === null ? null : (
              <div className='fav-rocky-fighter'>
                <h3>Favorite Rocky Fighter</h3>
                <p>{firstUser?.fav_rocky_fighter}</p>
              </div>
            )}
            {firstUser?.walkout_song === null ? null : (
              <div className='walkout-song'>
                <h3>Walkout Song</h3>
                <p>{firstUser?.walkout_song}</p>
              </div>
            )}
            {firstUser?.availability === null ? null : (
              <div className='availability'>
                <h3>Availability</h3>
                <p>{available}</p>
              </div>
            )}
            {firstUser?.has_kids === false ||
            firstUser?.has_kids === null ? null : (
              <div>
                <h3>Has Kids</h3>
                <p>{firstUser?.has_kids}</p>
              </div>
            )}
            {firstUser?.nickname === null ? null : (
              <div>
                <h3>Nickname</h3>
                <p>{firstUser?.nickname}</p>
              </div>
            )}
            {firstUser?.religion === null ? null : (
              <div>
                <h3>Religion</h3>
                <p>{firstUser?.religion}</p>
              </div>
            )}
            {firstUser?.pets === null ? null : (
              <div>
                <h3>Pets</h3>
                <p>{firstUser?.pets}</p>
              </div>
            )}
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
            <div className='discipline'>
              <GiBoxingGlove className='bio-right-icon' />
              <p>{discipline}</p>
            </div>
            <div className='reach'>
              <BiRuler className='bio-right-icon' />
              <p>{firstUser?.reach} in.</p>
            </div>
            <div className='profession-level'>
              <GiCage className='bio-right-icon' />
              <p>{professionalLevel}</p>
            </div>
            <div className='current-record'>
              <VscGraph className='bio-right-icon' />
              <p>{firstUser?.current_record}</p>
            </div>
            <div className='prev-titles'>
              <BiMedal className='bio-right-icon' />
              <p>
                {firstUser?.previous_titles === null
                  ? 'No Previous Titles'
                  : firstUser?.previous_titles}
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default ProfilePage;
