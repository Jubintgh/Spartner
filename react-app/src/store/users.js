const SET_USERS = 'users/SET_USERS';
const GET_USER = 'users/GET_USER';
const GET_ANSWERS = 'users/GET_ANSWERS';
const GET_ANS_SINGLE = 'users/GET_ANS_SINGLE';
const REMOVE_ANS_SINGLE = 'users/REMOVE_ANS_SINGLE';

const setUsers = (users) => ({
    type:SET_USERS,
    users
})

const setOneUser = (user) => ({
    type: GET_USER,
    user,
});



const setAnswers = (answers) => ({
    type: GET_ANSWERS,
    answers
})

const setOneAnswer= (answer) => ({
    type: GET_ANS_SINGLE,
    answer,
});

const deleteOneAnswer = (answer) => ({
    type: REMOVE_ANS_SINGLE,
    answer,
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

export const getUserAnswers = (id) => async (dispatch) => {
    const res = await fetch(`/api/users/${id}/answers`);

    if (res.ok) {
      const answers = await res.json();
      dispatch(setAnswers(answers));
      return answers
    }
};

export const createAnswer = (id) => async (dispatch) => {
    const res = await fetch(`/api/users/${id}/answers`, {
        method: 'POST'
    });

    if (res.ok) {
        const answer = await res.json()
        dispatch(setOneAnswer(answer))
        return answer
    }
}

export const removeAnswer = (id) => async (dispatch) => {
    const res = await fetch(`/api/users/${id}/answers`, {
        method: 'DELETE'
    });

    if (res.ok) {
        const answer = await res.json()
        dispatch(deleteOneAnswer(answer))
        return answer;
    }
}

const initialState = {}
const usersReducer = (state = initialState, action) => {
    let newState;
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
        case GET_ANSWERS:
            return {
                ...state,
                answers: action.answers
            }
        case GET_ANS_SINGLE:
            return {
                ...state,
                answer: action.answer
            }
        case REMOVE_ANS_SINGLE:
            newState = { ...state };
            delete newState[action.answer];
            return newState;
        default:
            return state
    }
}

export default usersReducer;
