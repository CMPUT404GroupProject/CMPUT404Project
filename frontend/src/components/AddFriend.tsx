import React from "react";
import {useDispatch} from "react-redux";
import {useHistory} from "react-router";
import authSlice from "../store/slices/auth";

const AddFriend = () => {

    return (
        <div>
            <button 
                className="rounded-lg p-3 bg-green-700 text-white text-lg">
                Add friend
            </button>
        </div>
    ) 
}

export default AddFriend