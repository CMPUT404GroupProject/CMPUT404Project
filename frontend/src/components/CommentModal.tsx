import React, {useContext, useState, useEffect} from 'react'
import CloseIcon from '@mui/icons-material/Close';
import IconButton from '@mui/material/IconButton';
import DragHandleIcon from '@mui/icons-material/DragHandle';
import GlobalContext from "./../context/GlobalContext";
import Dropdown from 'react-dropdown';
export default function CommentModal() {
    const {setShowCommentModal} = useContext(GlobalContext);
    const [contentType, setContentType] = useState("text/plain");
    const [comment, setComment] = useState("");
    const [errMsg, setErrMsg] = useState("");
    const [successMsg, setSuccessMsg] = useState("");
    function closeModal(){
        setShowCommentModal(false);
    }
    function onChangeContentType(event: any) {
        setContentType(event.target.value);
    }
    function handleSend(e: any) {
        e.preventDefault();
        if (comment === "") {
            setErrMsg("Comment cannot be empty");
            setSuccessMsg("");
        } else {
            setErrMsg("");
            console.log("comment", comment);
            console.log("contentType", contentType);
            setComment("");
            setSuccessMsg("Comment sent successfully");
        }
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
        <div style={{margin:"10px"}}>
            <div className="Comment">
                <input
                    type="text"
                    name="comment"
                    placeholder="Comment"
                    value={comment}
                    required
                    className="pt-3 border-0 
                    text-gray-600 text-l 
                    font-semibold pb-2 
                    w-full border-b-2 
                    border-gray-200 
                    focus:outline-none 
                    focus:ring-0
                    focus:border-blue-500"
                    style={{margin: "10px"}}
                    onChange={(e) => {setComment(e.target.value); setErrMsg(""); setSuccessMsg("");}} 
                >
                </input>
            </div>
            <div 
                onChange={onChangeContentType} 
                className="pt-3 border-0 
                    text-gray-600 text-l 
                    font-semibold pb-2 
                    w-full 
                    border-gray-200 
                    focus:outline-none 
                    focus:ring-0"
                    style={{margin: "10px"}}>
                <input type="radio" value="text/plain" name="contentType" checked/> text/plain
                <br></br>
                <input type="radio" value="text/markdown" name="contentType" /> text/markdown
                <button type="submit"
                    onClick={handleSend}
                    style={{margin: '10px', marginBottom: '5px', float: 'right'}}
                    className="bg-blue-500 hover:bg-blue-600 px-6 py-2 rounded text-white"    
                >
                    Send
                </button>
                <div style={{color: "red"}}>{errMsg}</div>
                <div style={{color: "green"}}>{successMsg}</div>
            </div>

        </div>
        </form>
    </div>
  );
}