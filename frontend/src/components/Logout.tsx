import React from "react";
import {useDispatch} from "react-redux";
import {useHistory} from "react-router";
import authSlice from "../store/slices/auth";

const Logout = () => {
    const dispatch = useDispatch();
    const history = useHistory(); 

    const handleLogout = () => {
        dispatch(authSlice.actions.setLogout());
        history.push("/login");
    };

    return (
        <div className="p-6">
            <button onClick={handleLogout} 
                className="rounded p-2 w-32 bg-red-700 text-white">
                Log out
            </button>
        </div>
    ) 
}

export default Logout