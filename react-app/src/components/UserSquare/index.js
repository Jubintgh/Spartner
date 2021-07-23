import { NavLink } from 'react-router-dom';
import './UserSquare.css';

const UserSquare = ({ user }) => {
    return (
        <div className='user-square'>
            <div className='user-info'>
                <div>
                    <img
                        style={{ width: "200px", height: "200px", borderRadius: "50%", objectFit: "cover" }}
                        src={user.img_url ?
                            user.img_url :
                            'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_1280.png' }
                        alt="spartner-profile"
                    />
                </div>
                <div className='profileLink'>
                    <NavLink to={`/users/${user.id}`}>
                        {user.first_name} {user.last_name}
                    </NavLink>
                </div>
            </div>
        </div>
    )
}

export default UserSquare;
