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
        <div>
            <button onClick={handleLogout} 
                className="rounded-lg p-3 bg-red-700 text-white text-lg">
                Log out
            </button>
        </div>
    ) 
}

export default Logout