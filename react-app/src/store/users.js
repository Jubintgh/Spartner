const SET_USERS = 'users/SET_USERS';
const GET_USER = 'users/GET_USER';
const GET_LIKES = 'users/GET_LIKES';
const GET_SINGLE = 'users/GET_SINGLE'
const REMOVE_SINGLE = 'users/REMOVE_SINGLE'

const setUsers = (users) => ({
    type:SET_USERS,
    users
})

const setOneUser = (user) => ({
    type: GET_USER,
    user,
});

const setLikes = (likes) => ({
    type: GET_LIKES,
    likes
})

const setOneLike = (like) => ({
    type: GET_SINGLE,
    like,
});

const deleteOneLike = (like) => ({
    type: REMOVE_SINGLE,
    like,
})

export const getUsers = () => async(dispatch) => {
    const res = await fetch('/api/users');

    if (res.ok) {
        const users = await res.json()
        dispatch(setUsers(users))
    }
}

export const getOneUser = (id) => async (dispatch) => {
    const res = await fetch(`/api/users/${id}`);

    if (res.ok) {
      const user = await res.json();
      dispatch(setOneUser(user));
    }
};

export const getAllUserLikes = (id) => async (dispatch) => {
    const res = await fetch(`/api/users/${id}/likes`);

    if (res.ok) {
      const likes = await res.json();
      dispatch(setLikes(likes));
      return likes
    }
};

export const createLike = (id, otherId) => async (dispatch) => {
    const res = await fetch(`/api/users/${id}/likes/${otherId}`, {
        method: 'POST'
    });

    if (res.ok) {
        const like = await res.json()
        dispatch(setOneLike(like))
        return like
    }
}

export const removeLike = (id, otherId) => async (dispatch) => {
    const res = await fetch(`/api/users/${id}/likes/${otherId}`, {
        method: 'DELETE'
    });

    if (res.ok) {
        const like = await res.json()
        dispatch(deleteOneLike(like))
        return like;
    }
}

const initialState = {}

const usersReducer = (state = initialState, action) => {
    switch (action.type) {
        case SET_USERS:
            const allUsers = {};
            action.users.forEach((user) => {
                allUsers[user.id] = user;
            }
            );
            return {
                ...state,
                ...allUsers
            };
        case GET_USER:
            return {
                ...state,
                [action.user.id] : action.user
            };
        case GET_LIKES:
            return {
                ...state,
                likes: action.likes
            }
        case GET_SINGLE:
            return {
                ...state,
                like: action.like
            }
        case REMOVE_SINGLE:
            const newState = { ...state };
            delete newState[action.like];
            return newState;
        default:
            return state
    }
}

export default usersReducer;
