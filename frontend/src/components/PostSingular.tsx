import axios from "axios";
import React, { useEffect, useState, useContext } from "react";
import ReactMarkdown from "react-markdown";
import { useFormik } from "formik";
import '../css/PostSingular.scss'
import {useDispatch, useSelector} from "react-redux";
import {RootState} from "../store";
import GlobalContext from "../context/GlobalContext";


interface OwnProps {
    post_type: string,
    post_title: string,
    post_id: string,
    source: string,
    origin: string,
    post_description: string,
    post_content_type: string,
    author: string,
    post_categories: string,
    count: number,
    comments: string,
    published: string,
    visibility: string,
    unlisted: boolean,
    editSwitch: boolean,
}

const PostSingular = ({post_type, post_title, post_id, source, origin, post_description, post_content_type, author, post_categories, count, comments, published, visibility, unlisted, editSwitch}: OwnProps) => {
    
    const [authorDisplayName, setAuthorDisplayName] = useState('None')
    const [authorGithub, setAuthorGithub] = useState('None')
    const [message, setMessage] = useState("");
    const [editMode, setEditMode] = useState(false)
    const [loading, setLoading] = useState(false);
    const [deleted, setDeleted] = useState(false);
    const account = useSelector((state: RootState) => state.auth.account);
    const {showCommentModal, setShowCommentModal} = useContext(GlobalContext);
    
    // @ts-ignore
    const userId = account?.id
    
    const handlePostSubmit = (type: string, title: string, source: string, origin: string, 
        description: string, contentType: string, author: string, categories: string, count: number,
        comments: string, published: string, visibility: string, unlisted: boolean) => {
        const post_link = `${process.env.REACT_APP_API_URL}/authors/` + author.toString() + '/posts/' + post_id.toString() + '/'

        axios.post(post_link, {type, title, source, origin, description, contentType, author, categories, count, comments, published, visibility, unlisted})
        .then((res) => {
            console.log(res)
            setMessage("Account created successfully");
          })
          .catch((err) => {
            setMessage("Error creating account");
          });
        setLoading(false)
    }
    
    const formik = useFormik({
        initialValues: {
          post_type: "",
          post_title: "",
          source: source,
          origin: origin,
          post_description: "",
          post_content_type: "",
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
          handlePostSubmit(values.post_type, values.post_title, values.source, values.origin, values.post_description, values.post_content_type, values.author, values.post_categories, values.count, values.comments, values.published, values.visibility, values.unlisted);
        },
      });

    function openCommentModal() {
        setShowCommentModal(true);
    }
    function sharePost(){
        const post_link = `${process.env.REACT_APP_API_URL}/authors/` + userId.toString() + '/posts/'
        axios.post(post_link, {type: post_type, title: post_title, source: userId.toString(), origin: origin, description: post_description, 
            contentType: post_content_type, author: userId.toString(), categories: post_categories, 
            count: count, comments: comments, published: published, visibility: visibility, unlisted: unlisted})
        .then((res) => {
            console.log(res)
            setMessage("Post shared successfully");
          })
          .catch((err) => {
            setMessage("Error sharing post");
          });
        setLoading(false)
    }
    function deletePost(){
        const post_link = `${process.env.REACT_APP_API_URL}/authors/` + author.toString() + '/posts/' + post_id + '/'
        axios.delete(post_link)
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
                        <div className="post-card">
                            <div className="author-profile-picture">
                                <img src="https://cdn.webfactorysite.co.uk/sr_695374_largeish.jpg" alt="profile-picture"></img>
                            </div>
                            <div className="post-header">
                                <div className="author-name">{authorDisplayName}</div>
                                <div className="post-title">{post_title}</div>
                                {editSwitch ? 
                                    <button onClick={deletePost} className="post-delete-button">Delete Post</button> : null
                                }
                            </div>
                            
                            {(post_content_type == "commonmark") ?
                                <div className="post-description">
                                    <p>
                                        <ReactMarkdown>
                                            {post_description}
                                        </ReactMarkdown>
                                    </p>
                                </div>:
                                null
                            }
                            {(post_content_type == "image") ?
                                <div className="post-image">
                                    <p>
                                        <img src={post_description} />
                                    </p>
                                </div>:
                                null
                            }
                            {(post_content_type == "text/plain") ?
                                <div className="post-description">
                                    <p>
                                        {post_description}
                                    </p>
                                </div>:
                                null
                            }
                            <div onClick={openCommentModal} className="post-comments">{count} Comments...</div>
                            <div className="post-interact">
                                {editSwitch ? 
                                    <button onClick={() => setEditMode(true)} className="post-edit-button">Edit Post</button> : null
                                }
                                <button className="post-like-button">0 Likes</button>
                                <button className="post-comment-button">Comment</button>
                                <button onClick={sharePost} className="post-share-button">Share</button>
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
        </div>
    ) 
}

export default PostSingular