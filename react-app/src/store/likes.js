const GET_LIKES = 'user/GET_LIKES';
const GET_LIKERS = 'user/GET_LIKERS'
const CREATE_LIKE = 'user/CREATE_LIKE';
const REMOVE_LIKE = 'user/REMOVE_LIKE';

const getLikes = (likes) => ({
    type: GET_LIKES,
    likes
})

const getLikers = (likes) => ({
    type: GET_LIKERS,
    likes
})

const setOneLike = (like) => ({
    type: CREATE_LIKE,
    like,
});

const deleteOneLike = (like) => ({
    type: REMOVE_LIKE,
    like,
})

export const getAllUserLikes = (id) => async (dispatch) => {
    const res = await fetch(`/api/users/${id}/likes`);

    if (res.ok) {
      const likes = await res.json();
      dispatch(getLikes(likes));
      return likes
    }
};

export const getAllLikedBy = (id) => async (dispatch) => {
    const res = await fetch(`/api/users/${id}/liked`);

    if (res.ok) {
      const likes = await res.json();
      dispatch(getLikers(likes));
      return likes
    }
};

export const createLike = (id, liked_id) => async (dispatch) => {
    const res = await fetch(`/api/users/${id}/like`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            'liked_id' : liked_id
        })
    });

    if (res.ok) {
        const like = await res.json()
        dispatch(setOneLike(like))
        return like
    }
}

export const removeLike = (id, liked_id) => async (dispatch) => {
    const res = await fetch(`/api/users/${id}/like`, {
        method: 'DELETE',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            'liked_id' : liked_id
        })
    });

    if (res.ok) {
        const like = await res.json()
        dispatch(deleteOneLike(like))
        return like;
    }
}


const initialState = {}
const likesReducer = (state = initialState, action) => {
    let newState;
    switch (action.type) {
        case GET_LIKES:
            return {
                ...state,
                likes: action.likes
            }

        case GET_LIKERS:
            return {
                ...state,
                likers: action.likes
            }

        case CREATE_LIKE:
            return {
                ...state,
                likes: action.like
            }

        case REMOVE_LIKE:
            newState = { ...state };
            delete newState[action.like];
            return newState;

        default:
            return state
    }
}

export default likesReducer