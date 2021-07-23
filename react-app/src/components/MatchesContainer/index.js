import { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';

import { getAllUserLikes, getAllLikedBy } from '../../store/likes';
import UserSquare from '../UserSquare'
import './MatchesContainer.css'

const MatchesContainer = () => {
    const dispatch = useDispatch();
    const loggedUser = useSelector((state) => state.session.user)
    const likesArray = useSelector((state) => {
        return Object.values(state.likes)
    })

    const userLikes = likesArray[0]?.user_likes
    const userLikers = likesArray[1]?.likes_user

    // const matchesArray = userLikes?.filter(user => userLikers?.includes(user.id))
    let matchesArray = []
    for (let i = 0; i < userLikes.length; i++) {
        for (let j = 0; j < userLikers.length; j++) {
            if (userLikes[i].id === userLikers[j].id) {
                matchesArray.push(userLikes[i])
            }
        }
    }

    useEffect(() => {
        dispatch(getAllUserLikes(loggedUser.id))
        dispatch(getAllLikedBy(loggedUser.id))
    }, [dispatch, loggedUser.id])

    return (
        <div>
        <h1> Matches </h1>
            <div className='users-container'>
                {matchesArray?.map((user) => (
                    <div className='user-square'>
                        <UserSquare user={user} key={user.id}/>
                    </div>
                ))}
            </div>
        </div>
    )
}

export default MatchesContainer;
