import React from "react";
import {useDispatch} from "react-redux";
import {useHistory} from "react-router";
import authSlice from "../store/slices/auth";
import '../css/Logout.scss'

const Logout = () => {
    const dispatch = useDispatch();
    const history = useHistory(); 

    const handleLogout = () => {
        dispatch(authSlice.actions.setLogout());
        history.push("/login");
    };

    return (
        <div>
            <button onClick={handleLogout} className="logout-button">
                Log out
            </button>
        </div>
    ) 
}

export default Logout