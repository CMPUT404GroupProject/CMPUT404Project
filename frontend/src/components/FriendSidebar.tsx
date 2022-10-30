import AddFriend from "./AddFriend";
import 'reactjs-popup/dist/index.css';
import React from "react";

interface OwnProps {
    onChange: (newValue: any)=> void;
}



const FriendSidebar = ({onChange}: OwnProps) => {
    return (
        <div className="friend-sidebar-card rounded-lg grid grid-rows-12 grid-cols-12 sticky top-0 bg-gray-800 p-5">
            <button className="create-post-button row-start-1 col-start-3 col-span-8 text-white text-lg rounded-lg self-start justify-self-center  bg-blue-600 p-3 m-3" onClick={onChange}>
                Create post
            </button>
            <div className="friend-button self-start justify-self-center row-start-2 col-start-3 col-span-8 m-3">
                <AddFriend></AddFriend>
            </div>
            <div className="friend-author-card row-start-3 col-start-3 col-span-8 grid grid-rows-12 grid-cols-12 bg-gray-900 rounded-full m-5">
                <div className="profile-picture row-start-1 col-start-2 col-span-2 m-2 self-center justify-self-center">
                    <div className="picture bg-black rounded-full h-16 w-16"></div>
                </div>
                <div className="user-name row-start-1 col-start-4 col-span-8 text-center text-lg self-center justify-self-center text-white p-4">Friend</div>
            </div>
        </div>
    ) 
}

export default FriendSidebar