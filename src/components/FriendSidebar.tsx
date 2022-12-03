import AddFriend from "./AddFriend";
import 'reactjs-popup/dist/index.css';
import '../css/FriendSidebar.scss'
import Inbox from "./Inbox";

interface OwnProps {
    onChange: (newValue: any)=> void;
}



const FriendSidebar = ({onChange}: OwnProps) => {
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
            <div className="friend-list-card">
                <div className="friend-profile-picture">
                    <img src="https://cdn.webfactorysite.co.uk/sr_695374_largeish.jpg" alt="profile-picture"></img>
                </div>
                <div className="friend-username">Friend name</div>
            </div>
        </div>
    ) 
}

export default FriendSidebar