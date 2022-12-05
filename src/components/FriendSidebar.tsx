import AddFriend from "./AddFriend";
import 'reactjs-popup/dist/index.css';
import '../css/FriendSidebar.scss'
import Inbox from "./Inbox";
import Cookies from "universal-cookie/es6/Cookies";
import axios from 'axios';
import {useEffect, useState} from "react";

interface OwnProps {
    onChange: (newValue: any)=> void;
}



const FriendSidebar = ({onChange}: OwnProps) => {
    // Get followers
    const cookies = new Cookies();
    const [friends, setFriends] = useState<any[]>([]);
    useEffect(() => {
        let currentUserUrl = cookies.get("currentUserUrl");
        let url = currentUserUrl + '/followers/';
        axios.get(url)
            .then((res) => {
                setFriends(res.data.items);
                console.log(res.data.items)
            }
        )
    }, [])
        
    return (
        <div className="friend-card">
            <button className="create-post-button" onClick={onChange}>
                Create post
            </button>
            <br></br>
            <div className="inbox-button">
                <Inbox />
            </div>
            <div className="friend-button">
                <AddFriend></AddFriend>
            </div>
            <div className="friend-list">
                {friends.map((friend) => {
                    return (
                        <div className="friend-list-card">
                            <div className="friend-profile-picture">
                                <img src="https://cdn.webfactorysite.co.uk/sr_695374_largeish.jpg" alt="profile-picture"></img>
                            </div>
                        <div className="friend-username">{friend.displayName}</div>
                        </div>
                    )
                })}
            </div>
        </div>
    ) 
}

export default FriendSidebar