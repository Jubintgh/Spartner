import './DiscoverPage.css';
import { useSelector, useDispatch } from 'react-redux';
import { Link } from 'react-router-dom';
import { useEffect, useState } from 'react';
import { getNewUsers, removeUser } from '../../store/discover';
import { createLike } from '../../store/likes';
import { getCurrentUserAndAnswers } from '../../store/session';
import { createDislike } from '../../store/dislikes';
import { ImCancelCircle } from 'react-icons/im';
import { AiFillHeart } from 'react-icons/ai';
import { MdKeyboardArrowRight } from 'react-icons/md';
import { GiWeight, GiCage } from 'react-icons/gi';
import { BiRuler, BiMedal } from 'react-icons/bi';
import { VscGraph } from 'react-icons/vsc';

const DiscoverPage = () => {
  const dispatch = useDispatch();
  const allUsersNotLiked = useSelector((state) =>
    Object.values(state.discover)
  );
  const { user } = useSelector((state) => state.session);
  const id = Number(user.id);
  const firstUser = allUsersNotLiked[0]
    ? allUsersNotLiked[0]
    : 'No more users to display!';

  const [likeButton, setLikeButton] = useState('/like-button-unclicked.png');
  const [dislikeButton, setDislikeButton] = useState(
    '/dislike-button-unclicked.png'
  );

  const handleClickDislike = (e) => {
    e.preventDefault();
    dispatch(removeUser(allUsersNotLiked.shift()));
    dispatch(createDislike(id, firstUser?.id));
  };

  const handleClickLike = (e) => {
    e.preventDefault();
    dispatch(removeUser(allUsersNotLiked.shift()));
    dispatch(createLike(id, firstUser?.id));
  };

  const changeImageSourceLiked = (e) => {
    if (likeButton === '/like-button-clicked.png') {
      setLikeButton('/like-button-unclicked.png');
    } else {
      setLikeButton('/like-button-clicked.png');
    }
  };

  const changeImageSourceDisliked = (e) => {
    if (dislikeButton === '/dislike-button-clicked.png') {
      setDislikeButton('/dislike-button-unclicked.png');
    } else {
      setDislikeButton('/dislike-button-clicked.png');
    }
  };

  console.log(user);

  const createMatchPercentage = () => {
    let total = 1;

    // if (user)
  };

  useEffect(() => {
    dispatch(getNewUsers(id));
    dispatch(getCurrentUserAndAnswers(id));
  }, [dispatch, id]);

  let usersLeftOrNoUsers;
  if (allUsersNotLiked.length === 0) {
    usersLeftOrNoUsers = (
      <div>'Out of users for today, better luck next time!'</div>
    );
  } else {
    usersLeftOrNoUsers = (
      <div className='main-area-container'>
        <div className='discover-title'>
          <h1>Recommended Just For You</h1>
        </div>
        <div className='user-info-container'>
          <div className='top-row'>
            <div className='user-info'>
              <div className='full-name'>
                <p className='first-name'>{firstUser?.first_name}</p>
                <p className='last-name'>{firstUser?.last_name}</p>
              </div>
              <p>|</p>
              <p>Match %</p>
              <p>|</p>
              <Link to={`/users/${id}`} className='view-profile-link'>
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
            <img alt='' src={firstUser?.img_url} className='user-img'></img>
          </div>
        </div>
        <div className='bio-container'>
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
            {firstUser?.has_kids === null ? null : (
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
            <div className='weightclass'>
              <GiWeight className='bio-right-icon' />
              <p>{firstUser?.weight_class}</p>
            </div>
            <div className='reach'>
              <BiRuler className='bio-right-icon' />
              <p>{firstUser?.reach} in.</p>
            </div>
            <div className='profession-level'>
              <GiCage className='bio-right-icon' />
              <p>{firstUser?.professional_level}</p>
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
    );
  }

  return <div className='discover-page'>{usersLeftOrNoUsers}</div>;
};

export default DiscoverPage;
