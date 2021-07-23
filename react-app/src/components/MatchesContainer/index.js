import { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';

import { getUsers } from '../../store/users';
import UserSquare from '../UserSquare'
import './MatchesContainer.css'

const MatchesContainer = () => {
    const dispatch = useDispatch();
    const matchesArray = useSelector((state) => {
        return Object.values(state.users)
    })

    // change dispatch to getMatches

    useEffect(() => {
        dispatch(getUsers())
    }, [dispatch])

    return (
        <div>
        <h1> Matches </h1>
            <div className='users-container'>
                {matchesArray.map((user) => (
                    <div className='user-square'>
                        <UserSquare user={user} key={user.id}/>
                    </div>
                ))}
            </div>
        </div>
    )
}

export default MatchesContainer;
