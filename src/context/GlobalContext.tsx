import React, {createContext, useContext, useEffect, useState} from 'react';

const GlobalContext = createContext({
    showCommentModal: false,
    setShowCommentModal: (value: boolean) => {},
    currentPostLink: "",
    setCurrentPostLink: (value: string) => {}
});
export default GlobalContext;

export const GlobalContextProvider = ({children}: any) => {
    const [showCommentModal, setShowCommentModal] = useState(false);
    const [currentPostLink, setCurrentPostLink] = useState("");
    useEffect(() => {
        console.log("showCommentModal", showCommentModal);
    }, [showCommentModal]);
    return (
        <GlobalContext.Provider 
            value={{
                showCommentModal, 
                setShowCommentModal,
                currentPostLink,
                setCurrentPostLink
            }}>
            {children}
        </GlobalContext.Provider>
    );
};
