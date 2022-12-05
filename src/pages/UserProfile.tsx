import React, { useState, useEffect } from "react";
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
  const [displayNameSwitch, toggleDisplayNameSwitch] = useState(false);
  const [githubLinkSwitch, toggleGithubLinkSwitch] = useState(false);
  const [passwordSwitch, togglePasswordSwitch] = useState(false);
  const [inputDisplayName, setInputDisplayName] = useState("");
  const [displayName, setDisplayName] = useState(user.data?.displayName);
  const [profileImage, setProfileImage] = useState(user.data?.profileImage);
  const [inputProfileImage, setInputProfileImage] = useState("");
  const [inputGithubLink, setInputGithubLink] = useState("");
  const [githubLink, setGithubLink] = useState(user.data?.github);

  useEffect(() => {
    setDisplayName(user.data?.displayName);
    }, [user.data?.displayName]);

  useEffect(() => {
    setGithubLink(user.data?.github);
    }, [user.data?.github]);

    useEffect(() => {
    setProfileImage(user.data?.profileImage);
    }, [user.data?.profileImage]);

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
    axios
        .post(`/authors/${userId}/`, { displayName: displayName, github: inputGithubLink })
        .then((res) => {        
            setGithubLink(inputGithubLink);
            setInputGithubLink("");
            toggleGithubLinkSwitch(false);
        })
        .catch((err) => {
            console.log(err);
        });
  }
  const handleDisplayNameUpdate = () => {
    // UPDATE Display Name HERE
    axios
        .post(`/authors/${userId}/`, { displayName: inputDisplayName })
        .then((res) => {
            setDisplayName(inputDisplayName);
            setInputDisplayName("");
            toggleDisplayNameSwitch(false);
        })
        .catch((err) => {
            console.log(err);
        });
  }
  const handleProfileImageUpdate = () => {
    // UPDATE PROFILE IMAGE HERE
        togglePasswordSwitch(false);
        axios
        .post(`/authors/${userId}/`, { profileImage: inputProfileImage })
        .then((res) => {
            setProfileImage(inputProfileImage);
            setInputProfileImage("");
            togglePasswordSwitch(false);
        })
        .catch((err) => {
            console.log(err);
        });
    }
  return (
    <div className="ProfilePageContainer">
        <div className="LeftPanel">
            <div className="ProfilePhoto">
                <img
                    //Fit container
                    style={{ width: "100%", height: "100%", objectFit: "cover" }}
                    src={user.data?.profileImage}>
                </img>
            </div>
            <div className="ProfileName"
                // White text
                style={{color: "white"}}
            >
                {displayName}
            </div>
        </div>
        <div className="RightPanel">    
            <div className="DisplayNameContainer Container">
                <div className="DisplayNameTitle Title">
                    Display Name
                    <hr />
                </div>
                <div className="DisplayNameText Text">
                    {(displayNameSwitch) ?
                        <input 
                            value={inputDisplayName} 
                            placeholder={"Enter new display name" }
                            type="text"
                            onChange={(e)=>setInputDisplayName(e.target.value)}/>:
                        <p>{displayName}</p>
                    }
                </div>
                {(!displayNameSwitch) ?
                    <div className="changePassword">
                        <button className="changeDisplayNameSwitch Switch SwitchOff" onClick={()=> toggleDisplayNameSwitch(true)}> <FaPencilAlt /> </button>
                    </div>:
                    <div className="updatePassword">
                        <button 
                            className="updateDisplayNameSwitch Switch SwitchOn" 
                            onClick={handleDisplayNameUpdate}> Update Display Name </button>
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
                        <input 
                            value={inputGithubLink}
                            placeholder="Enter new link" 
                            type="text"
                            onChange={(e)=>setInputGithubLink(e.target.value)}/>:
                        <p>{githubLink}</p>
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
                    Profile Image
                    <hr />
                </div>

                <div className="PasswordText Text">
                    {(passwordSwitch) ?
                        <input 
                            placeholder="Link to image" 
                            type="text"
                            onChange={(e)=>setInputProfileImage(e.target.value)}/>:
                        <p
                        // Wrap if too long
                        style={{wordWrap: "break-word"}}
                        > {profileImage} </p>
                    }
                </div>
                {(!passwordSwitch) ?
                    <div className="changePassword">
                        <button className="changePasswordSwitch Switch SwitchOff" onClick={()=> togglePasswordSwitch(true)}> <FaPencilAlt /> </button>
                    </div>:
                    <div className="updatePassword">
                        <button className="updatePasswordSwitch Switch SwitchOn" onClick={handleProfileImageUpdate}> Update Image </button>
                    </div>
                }         
            </div>
        </div>

    </div>
  );
};

export default UserProfile;
