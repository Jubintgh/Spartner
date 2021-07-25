const GET_UNSEEN_USERS = 'users/GET_UNSEEN_USERS';
const GET_MATCHES = 'users/GET_MATCHES';
const REMOVE_USER = 'users/REMOVE_USER';

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

export const getNewUsers = (id) => async (dispatch) => {
  const res = await fetch(`/api/users/${id}/discover`);

  if (res.ok) {
    const users_answers = await res.json();
    dispatch(setUsers(users_answers));
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
      dispatch(setUsers(users));
  }
}

const initialState = {};
const discoverReducer = (state = initialState, action) => {
  let newState;
  switch (action.type) {
    case GET_UNSEEN_USERS:
      const unseenUsers = {};
      const users = action.users.users_answers;
      users.forEach((user) => {
        unseenUsers[user.id] = user;
      });
      return {
        ...state,
        ...unseenUsers,
      };
    case REMOVE_USER:
      console.log(action.user.id);
      newState = { ...state };
      delete newState[action.user.id];
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
