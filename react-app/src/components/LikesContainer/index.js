import { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';

import { getAllUserLikes } from '../../store/likes';
import UserSquare from '../UserSquare'
import './LikesContainer.css'

const LikesContainer = () => {
    const dispatch = useDispatch();
    const loggedUser = useSelector((state) => state.session.user)
    const likesArray = useSelector((state) => {
        return Object.values(state.likes)
    })
    const userLikes = likesArray[0]?.user_likes

    useEffect(() => {
        dispatch(getAllUserLikes(loggedUser.id))
    }, [dispatch, loggedUser.id])

    return (
        <div>
        <h1> Liked Users </h1>
            <div className='users-container'>
                {userLikes?.map((user) => (
                    <div className='user-square-container'>
                        <UserSquare user={user} key={user.id}/>
                    </div>
                ))}
            </div>
        </div>
    )
}

export default LikesContainer;
