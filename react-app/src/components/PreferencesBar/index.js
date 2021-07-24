import { useState, useEffect } from 'react';
import { Link, useParams } from 'react-router-dom';
import { useSelector, useDispatch } from 'react-redux';
import { getFilteredUsers, removeFilteredUsers } from '../../store/users';

const PreferencesBar = () => {
const dispatch = useDispatch();
const user = useSelector(state => state.session.user);
const users = useSelector(state => Object.values(state.users))
const userId  = user.id;
const isCoach = user?.coach;




// button stuff here

const [vaxIcon, setVaxIcon] = useState('/vax-static.png');
const [vaxIconStatus, setVaxIconStaus] = useState('');
const [filter, setFilter] = useState();

// const [dislikeButton, setDislikeButton] = useState('/dislike-button-unclicked.png');


const changeVaxIcon = (e) => {
    // reducer connectivity here
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
    dispatch(getFilteredUsers(userId, filter));
}, [filter]);

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
            <ul className="element">
                <div className="icon" 
                >
                    <button
                    // alt='filter-icon'
                    // src= {vaxIcon}
                    href="https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885__480.jpg"
                    value="vaccination"
                    onClick={(e) => setFilter(e.target.value)}
                    // onClick={changeVaxIcon}
                    // onMouseLeave={handleOnMouseLeaveVax}
                    // onMouseEnter={changeVaxIconHover}
                    >THIS BUTTON</button>
                </div>
                <div className="icon-label">
                    <h5>Vaccinated</h5>
                </div>
            </ul>
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
