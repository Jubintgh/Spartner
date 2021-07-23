import { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';

import { getUsers } from '../../store/users';
import UserSquare from '../UserSquare'
import './LikesContainer.css'

const LikesContainer = () => {
    const dispatch = useDispatch();
    const likesArray = useSelector((state) => {
        return Object.values(state.users)
    }) // change to Likes


    // change dispatch to getLikes

    useEffect(() => {
        dispatch(getUsers())
    }, [dispatch])

    return (
        <div>
        <h1> Liked Users </h1>
            <div className='users-container'>
                {likesArray.map((user) => (
                    <div className='user-square'>
                        <UserSquare user={user} key={user.id}/>
                    </div>
                ))}
            </div>
        </div>
    )
}

export default LikesContainer;
