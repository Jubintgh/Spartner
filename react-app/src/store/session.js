// constants
const SET_USER = 'session/SET_USER';
const REMOVE_USER = 'session/REMOVE_USER';
const SET_USER_INFO = 'session/SET_USER_INFO';

const setUser = (user) => ({
  type: SET_USER,
  payload: user,
});

const removeUser = () => ({
  type: REMOVE_USER,
});

const setUserInfo = (userAnswers) => ({
  type: SET_USER_INFO,
  userAnswers,
});

export const getCurrentUserAndAnswers = (id) => async (dispatch) => {
  const res = await fetch(`/api/users/${id}`);

  if (res.ok) {
    const data = await res.json();
    if (data.errors) {
      return;
    }

    dispatch(setUserInfo(data));
  }
};

export const authenticate = () => async (dispatch) => {
  const response = await fetch('/api/auth/', {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json',
    },
  });
  if (response.ok) {
    const data = await response.json();
    if (data.errors) {
      return;
    }

    dispatch(setUser(data));
  }
};

export const login = (email, password) => async (dispatch) => {
  const response = await fetch('/api/auth/login', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      email,
      password,
    }),
  });

  if (response.ok) {
    const data = await response.json();
    dispatch(setUser(data));
    return null;
  } else if (response.status < 500) {
    const data = await response.json();
    if (data.errors) {
      return data.errors;
    }
  } else {
    return ['An error occurred. Please try again.'];
  }
};

export const logout = () => async (dispatch) => {
  const response = await fetch('/api/auth/logout', {
    headers: {
      'Content-Type': 'application/json',
    },
  });

  if (response.ok) {
    dispatch(removeUser());
  }
};

export const signUp =
  (
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
  ) =>
  async (dispatch) => {
    const response = await fetch('/api/auth/signup', {
      method: 'POST',
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
        img_url,
        discipline,
      }),
    });
    
export const signUp = (username, email, password, first_name,
  last_name,
  age,
  location,
  gender,
  coach,
  discipline,
  img_url) => async (dispatch) => {
  const response = await fetch('/api/auth/signup', {
    method: 'POST',
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
      img_url,
    }),
  });

    if (response.ok) {
      const data = await response.json();
      dispatch(setUser(data));
      return null;
    } else if (response.status < 500) {
      const data = await response.json();
      if (data.errors) {
        return data.errors;
      }
    } else {
      return ['An error occurred. Please try again.'];
    }
  };

const initialState = { user: null };

export default function reducer(state = initialState, action) {
  switch (action.type) {
    case SET_USER:
      return { user: action.payload };
    case REMOVE_USER:
      return { user: null };
    case SET_USER_INFO:
      return { user: action.userAnswers };
    default:
      return state;
  }
}
