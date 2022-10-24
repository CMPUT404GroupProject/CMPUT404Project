import React, { useState } from "react";
import {useDispatch, useSelector} from "react-redux";
import {useHistory, useLocation} from "react-router";
import authSlice from "../store/slices/auth";
import useSWR from 'swr';
import {fetcher} from "../utils/axios";
import {UserResponse} from "../utils/types";
import {RootState} from "../store";
import '../css/UserProfile.scss'
import { FaPencilAlt } from "react-icons/fa";
import axios from "axios";

interface LocationState {
    userId: string;
}

const UserProfile = () => {
  const account = useSelector((state: RootState) => state.auth.account);
  const dispatch = useDispatch();
  const history = useHistory();
  // @ts-ignore
  const userId = account?.id;
  const user = useSWR<UserResponse>(`/authors/${userId}/`, fetcher)
  // Here we have the update switches
  const [usernameSwitch, toggleUsernameSwitch] = useState(false);
  const [githubLinkSwitch, toggleGithubLinkSwitch] = useState(false);
  const [passwordSwitch, togglePasswordSwitch] = useState(false);
  const [inputUserName, setInputUserName] = useState("");

  const handleLogout = () => {
    dispatch(authSlice.actions.setLogout());
    history.push("/login");
  };

  const handlePasswordUpdate = () => {
    // UPDATE PASSWORD HERE
    togglePasswordSwitch(false);
  }

  const handleGithubUpdate = () => {
    // UPDATE GITHUB HERE
    toggleGithubLinkSwitch(false);
  }

  const handleUsernameUpdate = () => {
    // UPDATE USERNAME HERE
    console.log(inputUserName);
    console.log(userId);
    setInputUserName("");
    toggleUsernameSwitch(false);
  }

  return (
    <div className="ProfilePageContainer">
        <div className="LeftPanel">
            <div className="ProfilePhoto">
                <img src={user.data?.profileImage}></img>
            </div>
            <div className="ProfileName">
                {user.data?.displayName}
            </div>
        </div>
        <div className="RightPanel">    
            <div className="UsernameContainer Container">
                <div className="UsernameTitle Title">
                    Username
                    <hr />
                </div>
                <div className="UsernameText Text">
                    {(usernameSwitch) ?
                        <input 
                            value={inputUserName} 
                            placeholder="Enter new username" 
                            type="text"
                            onChange={(e)=>setInputUserName(e.target.value)}/>:
                        <p>{user.data?.displayName}</p>
                    }
                </div>
                {(!usernameSwitch) ?
                    <div className="changePassword">
                        <button className="changeUsernameSwitch Switch SwitchOff" onClick={()=> toggleUsernameSwitch(true)}> <FaPencilAlt /> </button>
                    </div>:
                    <div className="updatePassword">
                        <button 
                            className="updateUsernameSwitch Switch SwitchOn" 
                            onClick={handleUsernameUpdate}> Update Username </button>
                    </div>
                }  
            </div>
            <div className="GitHubLinkContainer Container">
                <div className="GitHubLinkTitle Title">
                    Github Link
                    <hr />
                </div>
                <div className="GitHubLinkText Text">
                    {(githubLinkSwitch) ?
                        <input placeholder="Enter new link" type="text"/>:
                        <p>{user.data?.github}</p>
                    }
                </div>
                {(!githubLinkSwitch) ?
                    <div className="changePassword">
                        <button className="changeGithubSwitch Switch SwitchOff" onClick={()=> toggleGithubLinkSwitch(true)}> <FaPencilAlt /> </button>
                    </div>:
                    <div className="updatePassword">
                        <button className="updateGithubSwitch Switch SwitchOn" onClick={handleGithubUpdate}> Update Github Link </button>
                    </div>
                }     
            </div>
            <div className="PasswordContainer Container">   
                <div className="PasswordTitle Title">
                    Password
                    <hr />
                </div>

                <div className="PasswordText Text">
                    {(passwordSwitch) ?
                        <input placeholder="Enter new password" type="password"/>:
                        <p> ********* </p>
                    }
                </div>
                {(!passwordSwitch) ?
                    <div className="changePassword">
                        <button className="changePasswordSwitch Switch SwitchOff" onClick={()=> togglePasswordSwitch(true)}> <FaPencilAlt /> </button>
                    </div>:
                    <div className="updatePassword">
                        <button className="updatePasswordSwitch Switch SwitchOn" onClick={handlePasswordUpdate}> Update Password </button>
                    </div>
                }         
            </div>
        </div>

    </div>
  );
};

export default UserProfile;
