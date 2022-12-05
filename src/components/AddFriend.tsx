import '../css/AddFriend.scss'
import GlobalContext from "./../context/GlobalContext";
import {useContext} from "react";

const AddFriend = () => {
    const {setShowAddFriendModal} = useContext(GlobalContext);
    function handleOpen(){
        setShowAddFriendModal(true)
    }
    return (
        <div>
            <button className="add-friend-button" onClick={handleOpen}>
                Add friends
            </button>
        </div>
    ) 
}

export default AddFriend