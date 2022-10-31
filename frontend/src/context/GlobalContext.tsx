import React, {createContext, useContext, useEffect, useState} from 'react';

const GlobalContext = createContext({
    showCommentModal: false,
    setShowCommentModal: (value: boolean) => {},
});
export default GlobalContext;

export const GlobalContextProvider = ({children}: any) => {
    const [showCommentModal, setShowCommentModal] = useState(false);
    useEffect(() => {
        console.log("showCommentModal", showCommentModal);
    }, [showCommentModal]);
    return (
        <GlobalContext.Provider value={{showCommentModal, setShowCommentModal}}>
            {children}
        </GlobalContext.Provider>
    );
};
