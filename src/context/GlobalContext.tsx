import React, {createContext, useContext, useEffect, useState} from 'react';

const GlobalContext = createContext({
    showCommentModal: false,
    setShowCommentModal: (value: boolean) => {},
    showAddFriendModal: false,
    setShowAddFriendModal: (value: boolean) => {},
    showInboxModal: false,
    setShowInboxModal: (value: boolean) => {},
    currentPostLink: "",
    setCurrentPostLink: (value: string) => {}
});
export default GlobalContext;

export const GlobalContextProvider = ({children}: any) => {
    const [showCommentModal, setShowCommentModal] = useState(false);
    const [currentPostLink, setCurrentPostLink] = useState("");
    const [showInboxModal, setShowInboxModal] = useState(false);
    const [showAddFriendModal, setShowAddFriendModal] = useState(false);
    useEffect(() => {
        console.log("showCommentModal", showCommentModal);
    }, [showCommentModal]);
    return (
        <GlobalContext.Provider 
            value={{
                showCommentModal, 
                setShowCommentModal,
                currentPostLink,
                setCurrentPostLink,
                showInboxModal,
                setShowInboxModal,
                showAddFriendModal,
                setShowAddFriendModal
            }}>
            {children}
        </GlobalContext.Provider>
    );
};
