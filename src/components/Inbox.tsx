import '../css/AddFriend.scss'
import GlobalContext from "./../context/GlobalContext";
import {useContext} from "react";

const Inbox = () => {
    const {setShowInboxModal} = useContext(GlobalContext);

    return (
        <div>
            <button className="add-friend-button"
                onClick={() => setShowInboxModal(true)}>
                Inbox
            </button>
        </div>
    ) 
}

export default Inbox