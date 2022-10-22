import React from "react";
import {useDispatch} from "react-redux";
import {useHistory} from "react-router";
import authSlice from "../store/slices/auth";

const AddFriend = () => {

    return (
        <div className="p-6">
            <button 
                className="rounded p-2 w-32 bg-emerald-400 text-white">
                Add Friend
            </button>
        </div>
    ) 
}

export default AddFriend