const SET_USERS = 'users/SET_USERS';
const GET_USER = 'users/GET_USER';

const setUsers = (users) => ({
    type:SET_USERS,
    users
})

const setOneUser = (user) => ({
    type: GET_USER,
    user,
});

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

export const editOneUser = (
    userId,
    username,
    email,
    password,
    first_name,
    last_name,
    age,
    location,
    gender,
    coach,
    discipline,
    img_url) => async (dispatch) => {
    const res = await fetch(`/api/users/${userId}`, {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            username,
            email,
            password,
            first_name,
            last_name,
            age,
            location,
            gender,
            coach,
            discipline,
            img_url
        })
        }
    )
        
    if (res.ok) {
      const user = await res.json();
      dispatch(setOneUser(user));
      return user
    }
};

const initialState = {}
const usersReducer = (state = initialState, action) => {
    switch (action.type) {
        case SET_USERS:
            let allUsers = {};
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
        default:
            return state
    }
}

export default usersReducer;
