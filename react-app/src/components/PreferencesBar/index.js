import { useState, useEffect } from 'react';
import { Link, useParams } from 'react-router-dom';
import { useSelector, useDispatch } from 'react-redux';
import { getFilteredUsers } from '../../store/users';

const PreferencesBar = () => {
const dispatch = useDispatch();
const user = useSelector(state => state.session.user);
const userId  = user.id;
const isCoach = user?.coach;




// button stuff here

const [vaxIcon, setVaxIcon] = useState('/vax-static.png');
const [vaxIconStatus, setVaxIconStaus] = useState('');
// const [dislikeButton, setDislikeButton] = useState('/dislike-button-unclicked.png');



const changeVaxIcon = (e) => {
    // reducer connectivity here
    dispatch(getFilteredUsers(userId, "vaccination"));
    if (vaxIcon === '/vax-hover.png') {
        setVaxIcon('/vax-active.png');
        setVaxIconStaus('/vax-active.png');

    } else if ( vaxIconStatus === '/vax-active.png') {
        setVaxIcon('/vax-static.png');
        setVaxIconStaus('/vax-static.png');
    }
  };

    const changeVaxIconHover = (e) => {
        setVaxIcon('/vax-hover.png');

    };

    const handleOnMouseLeaveVax = (e) => {
        setVaxIcon(vaxIconStatus);
    }

//   const changeVaxStatic = (e) => {
//     if (dislikeButton === '/dislike-button-clicked.png') {
//       setDislikeButton('/dislike-button-unclicked.png');
//     } else {
//       setDislikeButton('/dislike-button-clicked.png');
//     }
//   };



let renderCoachContent = null;

  if (!isCoach) {
    renderCoachContent = (
        <div className="element">
            <div className="icon">
                <img/>
            </div>
            <div className="icon-label">
                <h5>Coaches</h5>
            </div>
        </div>
        )
  }

useEffect(() => {

}, []);

return (
        <div className="block">
            <div className="element">
                <div className="icon">
                    <img/>
                </div>
                <div className="icon-label">
                    <h5>Recommended</h5>
                </div>
            </div>
            <div className="element">
                <div className="icon">
                    <img/>
                </div>
                <div className="icon-label">
                    <h5>Weight Class</h5>
                </div>
            </div>
            <div className="element">
                <div className="icon">
                    <img
                    src= {vaxIcon}
                    onClick={changeVaxIcon}
                    onMouseLeave={handleOnMouseLeaveVax}
                    onMouseEnter={changeVaxIconHover}
                    />
                </div>
                <div className="icon-label">
                    <h5>Vaccinated</h5>
                </div>
            </div>
            <div className="element">
                <div className="icon">
                    <img/>
                </div>
                <div className="icon-label">
                    <h5>Professional Level</h5>
                </div>
            </div>
        {renderCoachContent}
    </div>
  );
};

export default PreferencesBar
