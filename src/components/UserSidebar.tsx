import useSWR from 'swr';
import {fetcher} from "../utils/axios";
import {UserResponse} from "../utils/types";
import {RootState} from "../store";
import {useSelector} from "react-redux";
import { Link } from "react-router-dom";
import '../css/UserSidebar.scss'

interface OwnProps {
    onChange: (newValue: any)=> void;
    postVisibility: boolean;
}



const UserSidebar = ({onChange, postVisibility}: OwnProps) => {
    const account = useSelector((state: RootState) => state.auth.account);
    // @ts-ignore
    const userId = account?.id;
    const user = useSWR<UserResponse>(`/authors/${userId}/`, fetcher);



    return (
        <div className="profile-card bg-white">
            <div className="profile-picture">
                <img style={{ width: "100%", height: "100%", objectFit: "cover" }}
                src={user.data?.profileImage} alt="profile-picture"></img>
            </div>
            {
                user.data ?
                <div className="username">{user.data?.displayName}</div>
                :
                <div className="username">Your Name</div>
            }
            <button className="profile-button">
                <Link to="/Profile">My profile</Link>
            </button>
            {(postVisibility) ? 
                <button className="see-posts-button" onClick={onChange}>
                    See my posts
                </button>:
                <button className="see-posts-button" onClick={onChange}>
                    See all posts
                </button>
            }
        </div>
    ) 
}

export default UserSidebar