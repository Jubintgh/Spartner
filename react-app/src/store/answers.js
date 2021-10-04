const GET_ANSWER = 'users/GET_ANSWER';
const FIX_ANSWER = 'users/FIX_ANSWER';
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

const editOneAnswer= (answer) => ({
    type: FIX_ANSWER,
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
      console.log(answers, 'WAS HIT')
      dispatch(setOneAnswer(answers.answers))
      return answers
    } else {
        const errs = res.json()
        return errs
    }
};

export const createAnswer = (
    user_id,
    about,
    weightClass,
    reach,
    professionalLevel,
    currentRecord,
    previousTitles,
    favRockyFighter,
    walkoutSong,
    vaccinated,
    hasKids,
    inPerson,
    nickname,
    religion,
    pets,
    availability,
    rate ) => async (dispatch) => {
    const res = await fetch(`/api/users/${user_id}/answers`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            "user_id": user_id,
            "about": about,
            "weight_class": weightClass,
            "reach": reach,
            "professional_level": professionalLevel,
            "current_record": currentRecord,
            "previous_titles": previousTitles,
            "fav_rocky_fighter": favRockyFighter,
            "walkout_song": walkoutSong,
            "vaccinated": vaccinated,
            "has_kids": hasKids,
            "in_person": inPerson,
            "nickname": nickname,
            "religion": religion,
            "pets": pets,
            "availability": availability,
            "rate": rate
        })
    });

    if (res.ok) {
        const answer = await res.json()
        dispatch(setOneAnswer(answer))
        return answer
    } else {
        
        const data = await res.json();

        if(res.status > 499 || !data) return ['An error occurred. Please try again.']

        if(data.errors) {
            return data.errors;
        }
    }
}

export const editAnswer = (id) => async (dispatch) => {
    const res = await fetch(`/api/users/${id}/answers`, {
        method: 'PUT'
    });

    if (res.ok) {
        const answer = await res.json()
        dispatch(editOneAnswer(answer))
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
        case FIX_ANSWER:
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
