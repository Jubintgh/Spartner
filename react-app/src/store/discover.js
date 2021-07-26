const _ = require('lodash');

const GET_UNSEEN_USERS = 'users/GET_UNSEEN_USERS';
const GET_MATCHES = 'users/GET_MATCHES';
const REMOVE_USER = 'users/REMOVE_USER';
const GET_SHUFFLED_USERS = 'users/GET_SHUFFLED_USERS';

const setUsers = (users) => ({
  type: GET_UNSEEN_USERS,
  users,
});

const setMatches = (users) => ({
  type: GET_MATCHES,
  users,
});

export const removeUser = (user) => ({
  type: REMOVE_USER,
  user,
});

const setShuffledUsers = (users) => ({
  type: GET_SHUFFLED_USERS,
  users,
});

export const getNewUsers = (id) => async (dispatch) => {
  const res = await fetch(`/api/users/${id}/discover`);

  if (res.ok) {
    const users_answers = await res.json();
    console.log(users_answers, 'THIS WAS HIT FIRST')
    dispatch(setUsers(users_answers));
    dispatch(setShuffledUsers(users_answers));
    return users_answers;
  }
};

export const getMatchedUsers = (id) => async (dispatch) => {
  const res = fetch(`/api/users/${id}/matches`);

  if (res.ok) {
    const matched_users = await res.json();
    dispatch(setMatches(matched_users));
    return matched_users;
  }
};

export const getFilteredUsers = (id, filter) => async (dispatch) => {
  const res = await fetch(`api/users/${id}/filter/${filter}`);
  if (res.ok) {
    const users = await res.json();
    console.log(users, 'THIS WAS HIT')
      dispatch(setUsers(users));
  }
}

const initialState = {};
const discoverReducer = (state = initialState, action) => {
  let newState;
  switch (action.type) {
    case GET_UNSEEN_USERS:
      let unseenUsers = {};
      let users = action.users.users_answers;
      users.forEach((user, i) => {
        user.index = i;
        unseenUsers[i] = user;
      });
      return {
        ...state,
        ...unseenUsers,
      };
    case REMOVE_USER:
      newState = { ...state };
      delete newState[action.user.index];
      return newState;
    case GET_MATCHES:
      const matchedUsers = {};
      action.users.forEach((user) => {
        matchedUsers[user.id] = user;
      });
      return {
        ...state,
        ...matchedUsers,
      };
    default:
      return state;
  }
};

export default discoverReducer;
