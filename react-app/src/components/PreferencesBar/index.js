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

const [filter, setFilter] = useState();

let filterAppliedLabel = null;

// const handleOnClick = (e) => {
//     console.log(e.target.value);
//     setFilter(e.target.value)
//     filterAppliedLabel = filter;
// }



let renderCoachContent = null;

if (!isCoach) {
    renderCoachContent = (
        <div className="prefBar-element">
        <div className="prefBar-icon" onClick={(e) => setFilter("coach")}>
                        <img className="coachIcon" src="/coachIcon-static.png"/>
        </div>
        <div className="prefBar-icon-label">
            <h5>Coaches</h5>
        </div>
    </div>
    )
}

useEffect(() => {
    console.log("Store is changed")
    console.log(filter)
    dispatch(getFilteredUsers(userId, filter));
}, [filter]);

return (
    <div className="prefBar-container">
        <div className="prefBar-block">
            <div className="prefBar-element">
                <div className="prefBar-icon"
                    onClick={(e) => setFilter("recommended")}>
                        <img className="redommendedIcon" src="/fight-static.png"/>
                </div>
                <div className="prefBar-icon-label">
                    <h5>Recommended</h5>
                </div>
            </div>
            <div className="prefBar-element">
                <div className="prefBar-icon" onClick={(e) => setFilter("weight-class")}>
                        <img className="weightClassIcon" src="/weightclassIcon-static.png"/>
                </div>
                <div className="prefBar-icon-label">
                    <h5>Weight Class</h5>
                </div>
            </div>
            <div className="prefBar-element">
                <div className="prefBar-icon"
                    onClick={(e) => setFilter("vaccination")} >
                        <img className="vaxIcon" src="/vax-static.png" />
                </div>
                <div className="prefBar-icon-label">
                    <h5>Vaccinated</h5>
                </div>
            </div>
            <div className="prefBar-element">
                <div className="prefBar-icon" onClick={(e) => setFilter("professional-level")}>
                        <img className="proLevelIcon" src="/proIcon-static.png"/>
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