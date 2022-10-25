import Logout from "./Logout";
import useSWR from 'swr';
import {fetcher} from "../utils/axios";
import {UserResponse} from "../utils/types";
import {RootState} from "../store";
import {useSelector} from "react-redux";
import { Link } from "react-router-dom";

const UserSidebar = () => {
    const account = useSelector((state: RootState) => state.auth.account);
    // @ts-ignore
    const userId = account?.id;
    const user = useSWR<UserResponse>(`/authors/${userId}/`, fetcher);

    return (
        <div className="profile-card grid grid-rows-12 grid-cols-12 rounded-lg sticky top-0 bg-gray-800">
            <div className="profile-picture row-start-1 col-start-6 col-span-2 m-4 self-center justify-self-center">
                <div className="picture bg-black rounded-full h-40 w-40"></div>
            </div>
            {
                user.data ?
                <div className="user-name row-start-2 col-start-3 col-span-8 text-center text-2xl justify-self-center text-white p-4">{user.data?.displayName}</div>
                :
                <div className="user-name row-start-2 col-start-3 col-span-8 text-center text-2xl justify-self-center text-white p-4">Your Name</div>
            }
            <div className="user-handle row-start-3 col-start-3 col-span-8 text-xl justify-self-center text-white p-4">@your_handle</div>
            <button className="profile-button row-start-4 col-start-3 col-span-8 text-white text-lg rounded-lg justify-self-center bg-gray-700 p-3 m-3">
                <Link to="/Profile">My profile</Link>
            </button>
            <div className="logout-button row-start-5 col-start-3 col-span-8 justify-self-center m-3 p-2">
                <Logout></Logout>
            </div>
        </div>
    ) 
}

export default UserSidebar