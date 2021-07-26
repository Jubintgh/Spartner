import { NavLink } from 'react-router-dom';
import './UserSquare.css';

const UserSquare = ({ user }) => {
    return (
        <div className='user-square'>
            <div className='user-info-matches-likes'>
                <div>
                    <img
                        style={{ width: "150px", height: "150px", borderRadius: "50%", objectFit: "cover", margin:'10px'}}
                        src={
                            user?.img_url === 'inTheWorks.jpg'
                              ? 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_1280.png'
                              : user?.img_url
                          }
                        alt="spartner-profile"
                    />
                </div>
                <div className='profileLink'>
                    <NavLink to={`/users/${user.id}`}>
                        {user.first_name} {user.last_name}
                    </NavLink>
                </div>
                <div>
                    {user.location}
                </div>
            </div>
        </div>
    )
}

export default UserSquare;
