import React from 'react';
import { useDispatch } from 'react-redux';
import { login } from '../../store/session';

const DemoUserButton = () => {
  // const [errors, setErrors] = useState([]);
  const dispatch = useDispatch()
  const email = 'demouser@mail.com'
  const password = 'Password1!'

  const onDemoSignIn = async (e) => {
    e.preventDefault();
    const data = await dispatch(login(email, password));
    // if (data) {
    //   setErrors(data);
    // }
  };

  return <button onClick={onDemoSignIn}>Demo User</button>;
};

export default DemoUserButton;
