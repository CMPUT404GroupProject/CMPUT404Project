import React from "react";
import {useDispatch, useSelector} from "react-redux";
import {useHistory, useLocation} from "react-router";
import authSlice from "../store/slices/auth";
import useSWR from 'swr';
import {fetcher} from "../utils/axios";
import {UserResponse} from "../utils/types";
import {RootState} from "../store";
import Post from "../components/Post";

interface LocationState {
    userId: string;
}


const Profile = () => {
  const account = useSelector((state: RootState) => state.auth.account);
  const dispatch = useDispatch();
  const history = useHistory();
  // @ts-ignore
  const userId = account?.id;

  const user = useSWR<UserResponse>(`/authors/${userId}/`, fetcher)
  console.log(user.data)
  const handleLogout = () => {
    dispatch(authSlice.actions.setLogout());
    history.push("/login");
  };
  return (
    <div className="w-full h-full flex flex-col content-center">
        {
            user.data ?
                <div className="w-full text-center items-center">
                    <p className="self-center my-auto">Welcome, {user.data?.displayName}</p>
                </div>
                :
                <p className="text-center items-center">Loading ...</p>
        }
        <Post></Post>
    </div>
  );
};

export default Profile;
