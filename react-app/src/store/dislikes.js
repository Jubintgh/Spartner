const CREATE_DISLIKE = 'user/CREATE_DISLIKE';

const setOneDislike = (like) => ({
  type: CREATE_DISLIKE,
  like,
});

export const createDislike = (id, disliked_id) => async (dispatch) => {
  const res = await fetch(`/api/users/${id}/dislike`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      disliked_id: disliked_id,
    }),
  });

  if (res.ok) {
    const like = await res.json();
    dispatch(setOneDislike(like));
    return like;
  }
};

const initialState = {};
const dislikesReducer = (state = initialState, action) => {
  switch (action.type) {
    case CREATE_DISLIKE:
      return {
        ...state,
        dislikes: action.dislike,
      };
    default:
      return state;
  }
};

export default dislikesReducer;
