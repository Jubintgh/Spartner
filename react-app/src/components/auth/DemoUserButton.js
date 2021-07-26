import React from 'react';
import { useDispatch } from 'react-redux';
import { useHistory } from 'react-router-dom';
import { login } from '../../store/session';

const DemoUserButton = () => {
  // const [errors, setErrors] = useState([]);
  const history = useHistory();
  const dispatch = useDispatch();
  const email = 'demouser@mail.com';
  const password = 'Password1!';

  const onDemoSignIn = async (e) => {
    e.preventDefault();
    const data = await dispatch(login(email, password));
    history.push('/discover');
  };

  return <button onClick={onDemoSignIn}>Demo User</button>;
};

export default DemoUserButton;
