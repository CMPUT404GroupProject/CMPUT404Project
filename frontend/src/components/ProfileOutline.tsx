
import FriendSidebar from "./FriendSidebar";
import PostCard from "./PostCard";
import PostCardWithPhoto from "./PostCardWithPhoto";
import UserSidebar from "./UserSidebar";
import React, { useState } from "react";
import PostPopup from "./PostPopup";


const ProfileOutline = () => {
    const [postPopupClicked, setPostPopup] = useState(false);
    function handleChange(newValue: any) {
        setPostPopup(!postPopupClicked)
    }
    console.log(postPopupClicked)

    return (
        <div className="page">
            {(postPopupClicked) ?
                <PostPopup />:
                null
            }

            
            <div className="content grid grid-cols-12 gap-2">
                <div className="user-sidebar-left col-span-3">
                    <UserSidebar></UserSidebar>
                </div>
                <div className="main-content-middle col-span-6">
                    <PostCard></PostCard> 
                    <PostCardWithPhoto></PostCardWithPhoto>
                </div>
                <div className="friend-sidebar-right col-span-3">
                    <FriendSidebar
                        onChange={handleChange}
                    />
                </div>
            </div>
        </div>





    ) 
}

export default ProfileOutline