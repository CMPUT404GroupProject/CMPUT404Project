import axios from "axios";
import React, { useEffect, useState, useContext } from "react";
import ReactMarkdown from "react-markdown";
import { useFormik } from "formik";
import '../css/PostSingular.scss'
import {useDispatch, useSelector} from "react-redux";
import {RootState} from "../store";
import GlobalContext from "../context/GlobalContext";
import { string } from "yup";
import Snackbar from "@mui/material/Snackbar";
import MuiAlert from "@mui/material/Alert";

interface OwnProps {
    post_type: string,
    post_title: string,
    post_id: string,
    source: string,
    origin: string,
    post_description: string,
    post_content_type: string,
    post_content: string,
    author: string,
    post_categories: string,
    count: number,
    comments: string,
    published: string,
    visibility: string,
    unlisted: boolean,
    editSwitch: boolean,
}

const PostSingular = ({post_type, post_title, post_id, source, origin, post_description, post_content_type, post_content, author, post_categories, count, comments, published, visibility, unlisted, editSwitch}: OwnProps) => {

    // @ts-ignore
    const [profileImage, setProfileImage] = useState(author?.profileImage)
    // @ts-ignore
    const [authorDisplayName, setAuthorDisplayName] = useState(author.displayName);


    // @ts-ignore
    const [authorGithub, setAuthorGithub] = useState(author.github);
    const [message, setMessage] = useState("");
    const [editMode, setEditMode] = useState(false)
    const [loading, setLoading] = useState(false);
    const [deleted, setDeleted] = useState(false);
    const account = useSelector((state: RootState) => state.auth.account);
    const [likeAlert, setLikeAlert] = useState(false);
    const {
        showCommentModal, 
        setShowCommentModal,
        currentPostLink,
        setCurrentPostLink
    } = useContext(GlobalContext);

    var foreign = 0;

    if (post_id.includes("cmput404f22t17.herokuapp.com") == true){
        foreign = 1;
    }

    else if (post_id.includes("fallprojback.herokuapp.com") == true){
        foreign = 2;
    }

    else if (post_id.includes("c404-team8.herokuapp.com") == true){
        foreign = 3;
    }
    
    var postState = 'foreign' + foreign.toString()

    // @ts-ignore
    const userId = account?.id
    const handlePostSubmit = (type: string, title: string, source: string, origin: string, 
        description: string, contentType: string, content:string, author: string, categories: string, count: number,
        comments: string, published: string, visibility: string, unlisted: boolean) => {
        const post_link = post_id.toString() + '/'
        axios.post(post_link, {type:type, id:userId.toString(), title:title, source:source, origin:origin, description:description, categories: categories, content: content}, {auth: {username:'argho', password:'12345678!'}})

        .then((res) => {
            setMessage("Post edited successfully");
          })
          .catch((err) => {
            setMessage("Error editing post");
          });
        setLoading(false)
        setEditMode(false)
    }
    
    const formik = useFormik({
        initialValues: {
          post_type: "",
          post_title: "",
          source: source,
          origin: origin,
          post_description: "",
          post_content_type: "",
          post_content: "",
          author: author,
          post_categories: "",
          count: 0,
          comments: "",
          published: published,
          visibility: "",
          unlisted: false,
        },
        onSubmit: (values) => {
          setLoading(true);
        //   console.log("submitPressed");
          handlePostSubmit(values.post_type, values.post_title, values.source, values.origin, values.post_description, values.post_content_type, values.post_content, values.author, values.post_categories, values.count, values.comments, values.published, values.visibility, values.unlisted);
        },
      });

    function openCommentModal() {
        setCurrentPostLink(post_id);
        setShowCommentModal(true);
    }

    function likePost() {
        // Log id of current author
        let data = {
            "author": userId
        };
        axios.post(post_id + "/likes/", data, {auth: {username:'argho', password:'12345678!'}})
        .then((res) => {
            setLikeAlert(true);
        }
        );

    }

    function sharePost(){
        const post_link = `${process.env.REACT_APP_API_URL}/authors/` + userId.toString() + '/posts/'
        // BIG TEST
        

        // BIG TEST ENDS
        axios.post(post_link, {type: post_type, title: post_title, source: userId.toString(), origin: origin, description: post_description, 
            contentType: post_content_type, author: userId.toString(), categories: post_categories, 
            count: count, comments: comments, visibility: visibility, unlisted: unlisted}, {auth: {username:'argho', password:'12345678!'}})
        .then((res) => {
            setMessage("Post shared successfully");
          })
          .catch((err) => {
            setMessage("Error sharing post");
          });
        setLoading(false)
    }
    function deletePost(){
        // @ts-ignore
        const post_link = post_id
        // @ts-ignore
        axios.delete(post_link, {auth: {username:'argho', password:'12345678!'}})
        .then((res) => {
            if (res.status == 204){
                console.log("POST DELETED")
                setDeleted(true)
            }
        })
    }

    // We'll make a get request for the author id and get some stuff such as displayName and github URL that we will use for each of these posts
    useEffect(() =>{
        const required_link = `${process.env.REACT_APP_API_URL}/authors/` + author.toString() +'/'
        axios.get(required_link)
        .then((res) => {
            setAuthorDisplayName(res.data.displayName.toString())
            setAuthorGithub(res.data.github.toString())
        })
        .catch((err) => {
            setMessage("Error retrieving authors");
        });
    }, [author])

    return (
        <div>
            {(!deleted) ? 
                <div>
                    {!(editMode) ? 
                        <div className={"post-card" + " " + postState} >
                            <div className="author-profile-picture">
                                <img 
                                //Fit style
                                style={{width: "100%", height: "100%", objectFit: "cover"}}
                                src={profileImage} alt="profile-picture"></img>
                            </div>
                            <div className="post-header">
                                <div className="header-row-1">
                                    <div className="author-name">{authorDisplayName}</div>
                                    <div className="header-buttons">
                                        {editSwitch ? 
                                            <button onClick={deletePost} className="post-delete-button">Delete Post</button> : null
                                        }
                                        {editSwitch ? 
                                        <button onClick={() => setEditMode(true)} className="post-edit-button">Edit Post</button> : null
                                        }
                                    </div>
                                </div>
                                <div className="post-title"> - {post_title}</div>
                            </div>
                            
                            
                            <div className="post-description">
                                <p>
                                    - {post_description}
                                </p>
                            </div>
                            {(post_content_type == "commonmark") ?
                                <div className="post-commonmark">
                                    <p>
                                        <ReactMarkdown>
                                            {post_content}
                                        </ReactMarkdown>
                                    </p>
                                </div>:
                                null
                            }
                            {(post_content_type.includes("image")) ?
                                <div className="post-image">
                                    <p>
                                        <img src={post_content} />
                                    </p>
                                </div>:
                                null
                            }
                            {(post_content_type.includes("text")) ?
                                <div className="post-text">
                                    <p>
                                        {post_content}
                                    </p>
                                </div>:
                                null
                            }


                            
                            
                            <div className="post-interact">
                                <button onClick={likePost} className="post-like-button">Like</button>
                                <button onClick={openCommentModal} className="post-comment-button">Comment</button>
                                <button onClick={sharePost} className="post-share-button">Share</button>
                                <div className="post-comments">{count} Comments</div>
                            </div>
                        </div>:
                        <div className="formContainer">
                            <form onSubmit={formik.handleSubmit}>
                                {/* THIS IS FOR POST TYPE */}
                                <div className="InputField">
                                    <div className="InputHeader">
                                        Post Type:
                                    </div>
                                    <input
                                    id="post_type"
                                    type="text"
                                    placeholder="Enter Post Type"
                                    name="post_type"
                                    value={formik.values.post_type}
                                    onChange={formik.handleChange} 
                                    onBlur={formik.handleBlur} 
                                    />
                                </div>
                                {/* THIS IS FOR POST TITLE */}
                                <div className="InputField">
                                    <div className="InputHeader">
                                        Post Title:
                                    </div>
                                    <input 
                                        id="post_title"
                                        type="text"
                                        placeholder="Enter Post Title"
                                        name="post_title"
                                        value={formik.values.post_title}
                                        onChange={formik.handleChange}
                                        onBlur={formik.handleBlur}   
                                    />
                                </div>
        
                                {/* THIS IS FOR POST DESCRIPTION */}
                                <div className="InputField">
                                    <div className="InputHeader">
                                        Post Description:
                                    </div>
                                    <textarea 
                                        id="post_description"
                                        placeholder="Enter Post Description"
                                        name="post_description"
                                        value={formik.values.post_description}
                                        onChange={formik.handleChange}
                                        onBlur={formik.handleBlur}   
                                    />
                                </div>
        
                                {/* THIS IS FOR POST CONTENT TYPE */}
                                <div className="InputField">
                                    <div className="InputHeader">
                                        Content-type
                                    </div>
                                    <select 
                                        id="post_content_type"
                                        placeholder="Enter Post Content Type"
                                        name="post_content_type"
                                        value={formik.values.post_content_type}
                                        onChange={formik.handleChange}
                                        onBlur={formik.handleBlur} 
                                    >
                                        <option value="commonmark">Markdown</option>
                                        <option value="image">Image</option>
                                        <option value="text/plain">Text</option>
                                    </select>
                                </div>
        
                                {/* THIS IS FOR POST CATEGORIES */}
                                <div className="InputField">
                                    <div className="InputHeader">
                                        Categories
                                    </div>
                                    <input 
                                        id="post_categories"
                                        type="text"
                                        placeholder="Enter Post Categories"
                                        name="post_categories"
                                        value={formik.values.post_categories}
                                        onChange={formik.handleChange}
                                        onBlur={formik.handleBlur} 
                                    />
                                </div>
                                <div className="InputField">
                                    <div className="InputHeader">
                                        Visibility
                                    </div>
                                    <select 
                                        id="visibility"
                                        placeholder="Enter visibility: PUBLIC or PRIVATE"
                                        name="visibility"
                                        value={formik.values.visibility}
                                        onChange={formik.handleChange}
                                        onBlur={formik.handleBlur} 
                                    >
                                        <option value="public">Public</option>
                                        <option value="private">Private</option>
                                    </select>
                                </div>
                                <div className="submitPost">
                                    <button
                                        className="edit-post-button-save"
                                        type="submit"
                                        disabled={loading}
                                    >
                                        Edit Post
                                    </button>
                                    <button
                                        className="cancel-button"
                                        type="button"
                                        onClick={() => setEditMode(false)}
                                    >
                                        Cancel
                                    </button>
                                </div>
                            </form>
        
        
                        </div>
                        
                    }
                </div>:
                null
            }
        <Snackbar open={likeAlert} onClose={() => setLikeAlert(false)} autoHideDuration={3000} anchorOrigin={{ vertical: "bottom", horizontal: "center" }}>
          <MuiAlert variant="filled" severity="success" sx={{ width: '100%' }} onClose={() => setLikeAlert(false)}>
            Liked!
          </MuiAlert>
        </Snackbar>
        </div>
    ) 
}

export default PostSingular