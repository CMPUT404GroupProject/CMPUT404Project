import React, {useContext, useState, useEffect} from 'react'
import CloseIcon from '@mui/icons-material/Close';
import IconButton from '@mui/material/IconButton';
import DragHandleIcon from '@mui/icons-material/DragHandle';
import GlobalContext from "./../context/GlobalContext";

export default function CommentModal() {
    const {setShowCommentModal} = useContext(GlobalContext);
    function closeModal(){
        setShowCommentModal(false);
    }
  return (
    <div className="h-screen w-full fixed left-0 top-0 flex justify-center items-center"
        data-testid="class-modal-1"
        style={{zIndex: 3}}>
        <form className="bg-white rounded-lg shadow-2xl w-1/3" >
        <header className="bg-gray-100 px-4 py-2 flex justify-between items-center">
                <span className="material-icons-outlined text-gray-400">
                    <IconButton>
                        <DragHandleIcon />
                    </IconButton>
                </span>
                <div>
                    <span className="material-icons-outlined text-gray-400">
                        <IconButton onClick={closeModal}>
                            <CloseIcon />
                        </IconButton>
                    </span>
                </div>
        </header>
        </form>
    </div>
  );
}