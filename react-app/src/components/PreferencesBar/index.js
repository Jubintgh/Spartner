import { useState, useEffect } from 'react';
import { Link, useParams } from 'react-router-dom';
import { useSelector, useDispatch } from 'react-redux';
import { getFilteredUsers} from '../../store/discover';
import "./PreferenceBar.css"

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




let renderCoachContent = null;

if (!isCoach) {
    renderCoachContent = (
        <div className="prefBar-element">
        <div className="prefBar-icon">
            <button
                    href="https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885__480.jpg"
                    value="coach"
                    onClick={(e) => setFilter(e.target.value)}
                    >
                        <img className="coachIcon" src="/coachIcon-static.png"/>
                    </button>
        </div>
        <div className="prefBar-icon-label">
            <h5>Coaches</h5>
        </div>
    </div>
    )
}

let filterAppliedLabel = null;

// this is where depending on what filter you select, instead of having the icon stay active , the text will hang above the card displaying what filter is active

/*
useParams()
if vaccination => fileterAppliedLabel = 'Vaccination';
if weight class => fileterAppliedLabel = 'weight class';
if professional level => fileterAppliedLabel = 'professional level';
if coaches  => fileterAppliedLabel = ' coaches';
if null => fileterAppliedLabel = 'general';
*/


useEffect(() => {
    dispatch(getFilteredUsers(userId, filter));
}, [filter]);

return (
    <div className="prefBar-container">
        <div className="prefBar-block">
            <div className="prefBar-element">
                <div className="prefBar-icon">
                     <button
                    href="https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885__480.jpg"
                    value="/"
                    onClick={(e) => setFilter(e.target.value)}
                    >
                        <img className="redommendedIcon" src="/fight-static.png"/>
                    </button>
                </div>
                <div className="prefBar-icon-label">
                    <h5>Recommended</h5>
                </div>
            </div>
            <div className="prefBar-element">
                <div className="prefBar-icon">
                     <button
                    href="https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885__480.jpg"
                    value="weight-class"
                    onClick={(e) => setFilter(e.target.value)}
                    >
                        <img className="weightClassIcon" src="/weightclassIcon-static.png"/>
                    </button>
                </div>
                <div className="prefBar-icon-label">
                    <h5>Weight Class</h5>
                </div>
            </div>
            <ul className="prefBar-element">
                <div className="prefBar-icon" 
                >
                    <button
                    href="https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885__480.jpg"
                    value="vaccination"
                    onClick={(e) => setFilter(e.target.value)}
                    >
                        <img className="vaxIcon" src="/vax-static.png"/>
                    </button>
                </div>
                <div className="prefBar-icon-label">
                    <h5>Vaccinated</h5>
                </div>
            </ul>
            <div className="prefBar-element">
                <div className="prefBar-icon">
                     <button
                    href="https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885__480.jpg"
                    value="professional-level"
                    onClick={(e) => setFilter(e.target.value)}
                    >
                        <img className="proLevelIcon" src="/proIcon-static.png"/>
                    </button>
                </div>
                <div className="prefBar-icon-label">
                    <h5>Professional Level</h5>
                </div>
            </div>
        {renderCoachContent}
    </div>
    {filterAppliedLabel}
    </div>
  );
};

export default PreferencesBar