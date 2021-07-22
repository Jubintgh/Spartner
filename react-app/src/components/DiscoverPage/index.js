import './DiscoverPage.css';
import { useSelector, useDispatch } from 'react-redux';
import { Link } from 'react-router-dom';
import { useEffect } from 'react';
import { getUsers } from '../../store/users';
import { ImCancelCircle } from 'react-icons/im';
import { AiFillHeart } from 'react-icons/ai';
import { MdKeyboardArrowRight } from 'react-icons/md';
import { GiWeight, GiCage } from 'react-icons/gi';
import { BiRuler, BiMedal } from 'react-icons/bi';
import { VscGraph } from 'react-icons/vsc';

const DiscoverPage = () => {
  // const dispatch = useDispatch();
  const allUsersNotLiked = useSelector((state) => Object.values(state.session));
  console.log(allUsersNotLiked);

  const handleClickDislike = (e) => {
    e.preventDefault();
    console.log('Passed');
  };

  const handleClickLike = (e) => {
    e.preventDefault();
    console.log('Liked');
  };

  // useEffect(() => {
  //   dispatch(getUsers());
  // }, [dispatch]);

  return (
    <div className='discover-page'>
      <div className='main-area-container'>
        <div className='discover-title'>
          <h1>Recommended Just For You</h1>
        </div>
        <div className='user-info-container'>
          <div className='top-row'>
            <div className='user-info'>
              <p>First Name</p>
              <p>Location</p>
              <p>Match %</p>
              <Link className='view-profile-link'>
                View Profile <MdKeyboardArrowRight className='arrow-link' />
              </Link>
            </div>
            <div className='discover-btns'>
              <div onClick={(e) => handleClickDislike(e)} className='pass-btn'>
                <ImCancelCircle />
              </div>
              <div onClick={(e) => handleClickLike(e)} className='like-btn'>
                <AiFillHeart />
              </div>
            </div>
          </div>
          <div className='user-picture'>
            <img
              alt=''
              src='https://img.favpng.com/12/22/4/computer-icons-avatar-user-profile-png-favpng-3p1iZVKa5YWcfPt11TumPDH30.jpg'
              className='user-img'
            ></img>
          </div>
        </div>
        <div className='bio-container'>
          <div className='bio-left'>
            <h3>Self Summary</h3>
            <p>user about</p>
            <h3>Favorite Rocky Fighter</h3>
            <p>user fav_rocky_fighter</p>
            <h3>Walkout Song</h3>
            <p>user walkout song</p>
            <h3>Has Kids</h3>
            <p>user has kids</p>
            <h3>Nickname</h3>
            <p>user nickname</p>
            <h3>Religion</h3>
            <p>user religion</p>
            <h3>Pets</h3>
            <p>user pets</p>
          </div>
          <div className='bio-right'>
            <div className='weightclass'>
              <GiWeight className='bio-right-icon' />
              <p>user weightclass</p>
            </div>
            <div className='reach'>
              <BiRuler className='bio-right-icon' />
              <p>user reach</p>
            </div>
            <div className='profession-level'>
              <GiCage className='bio-right-icon' />
              <p>user profession_level</p>
            </div>
            <div className='current-record'>
              <VscGraph className='bio-right-icon' />
              <p>user current_record</p>
            </div>
            <div className='prev-titles'>
              <BiMedal className='bio-right-icon' />
              <p>user previous_titles</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default DiscoverPage;
