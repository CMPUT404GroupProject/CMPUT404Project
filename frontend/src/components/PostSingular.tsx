import axios from "axios";
import React, { useEffect, useState } from "react";
import ReactMarkdown from "react-markdown";
import { useFormik } from "formik";
import '../css/PostSingular.scss'

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
            {!(editMode) ? 
                <div className="post-card grid grid-rows-12 grid-cols-12 bg-gray-800 rounded-lg mb-2">
                    <div className="author-profile-picture row-start-1 col-start-1 col-span-2 bg-black rounded-full h-20 w-20 place-self-center m-5"></div>
                    <div className="author-name row-start-1 col-start-3 col-span-2 text-white text-lg justify-self-start self-center">Posted by: {authorDisplayName}</div>
                    <div className="author-handle row-start-1 col-start-5 col-span-2 text-white text-md justify-self-start self-center">{authorGithub}</div>
                    <div className="post-title row-start-2 col-start-3 col-span-8 text-white text-2xl mb-5">{post_title}</div>
                    
                    {(post_content_type == "commonmark") ?
                        <div className="post-description row-start-3 col-start-3 col-span-9 text-white text-md mb-5">
                            <p>
                                <ReactMarkdown>
                                    {post_description}
                                </ReactMarkdown>
                            </p>
                        </div>:
                        null
                    }
                    {(post_content_type == "image") ?
                        <div className="post-description row-start-3 col-start-3 col-span-9 text-white text-md mb-5">
                            <p>
                                <img src={post_description} />
                            </p>
                        </div>:
                        null
                    }
                    {(post_content_type == "text/plain") ?
                        <div className="post-description row-start-3 col-start-3 col-span-9 text-white text-md mb-5">
                            <p>
                                {post_description}
                            </p>
                        </div>:
                        null
                    }
                    
                    <div className="post-comments row-start-4 col-start-9 col-span-3 text-white text-center text-sm place-content-start bg-gray-900 rounded-lg p-2 mb-5">{count} Comments...</div>
                    <div className="like-count row-start-5 col-start-3 col-span-2 justify-self-start self-center text-white text-sm bg-indigo-500 rounded-lg m-5 p-2">327 Likes</div>
                    <button className="post-like-button row-start-5 col-start-5 text-md rounded-lg text-white bg-green-600 place-self-center m-5 p-3">Like</button>
                    <button className="post-comment-button row-start-5 col-start-7 text-md rounded-lg text-white bg-gray-700 place-self-center m-5 p-3">Comment</button>
                    <button className="post-share-button row-start-5 col-start-9 text-md rounded-lg text-white bg-yellow-600 place-self-center m-5 p-3">Share</button>
                    {editSwitch ? 
                        <button onClick={() => setEditMode(true)} className="edit-button row-start-5 col-start-11 text-md rounded-lg text-white bg-yellow-600 place-self-center m-5 p-3">Edit Post</button>:
                        null
                    }
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
                            <input 
                                id="post_description"
                                type="text"
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
                            <input 
                                id="post_content_type"
                                type="text"
                                placeholder="Enter Post Content Type"
                                name="post_content_type"
                                value={formik.values.post_content_type}
                                onChange={formik.handleChange}
                                onBlur={formik.handleBlur} 
                            />
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
                            <input 
                                id="visibility"
                                type="text"
                                placeholder="Enter visibility: PUBLIC or PRIVATE"
                                name="visibility"
                                value={formik.values.visibility}
                                onChange={formik.handleChange}
                                onBlur={formik.handleBlur} 
                            />
                        </div>
                        <div className="submitPost">
                            <button
                                className="submitCancel"
                                type="submit"
                                disabled={loading}
                            >
                                Edit Post
                            </button>
                            <button
                                className="submitCancel"
                                type="button"
                                onClick={() => setEditMode(false)}
                            >
                                Cancel
                            </button>
                        </div>
                    </form>


                </div>
                
            }
        </div>
        
    ) 
}

export default PostSingular