import React from "react";
import Logout from "./Logout";
import useSWR from 'swr';
import {fetcher} from "../utils/axios";
import {UserResponse} from "../utils/types";
import {RootState} from "../store";
import {useSelector} from "react-redux";
import AddFriend from "./AddFriend";

const Navbar = () => {
    const account = useSelector((state: RootState) => state.auth.account);
    // @ts-ignore
    const userId = account?.id;
    const user = useSWR<UserResponse>(`/authors/${userId}/`, fetcher);

    return (
        <div className="w-full h-24 bg-sky-900 flex justify-between">
            
            {userId ? <Logout></Logout> : ""}
            {userId ? <AddFriend></AddFriend> : ""}
            
        </div>
    ) 
}

export default Navbar