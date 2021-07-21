const GET_ANSWER = 'users/GET_ANSWER';
const GET_ANSWERS = 'users/GET_ANSWERS';
const REMOVE_ANSWER = 'users/REMOVE_ANSWER';


const setAnswers = (answers) => ({
    type: GET_ANSWERS,
    answers
})

const setOneAnswer= (answer) => ({
    type: GET_ANSWER,
    answer,
});

const deleteOneAnswer = (answer) => ({
    type: REMOVE_ANSWER,
    answer,
})

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
const answerReducer = (state = initialState, action) => {
    let newState;
    switch (action.type) {
        case GET_ANSWERS:
            return {
                ...state,
                answers: action.answers
            }
        case GET_ANSWER:
            return {
                ...state,
                answer: action.answer
            }
        case REMOVE_ANSWER:
            newState = { ...state };
            delete newState[action.answer];
            return newState;

        default:
            return state
    }
}

export default answerReducer;