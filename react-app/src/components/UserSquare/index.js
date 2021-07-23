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
                            "https://smhlancers.org/wp-content/uploads/2016/06/profile-placeholder-300x300.png" }
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
