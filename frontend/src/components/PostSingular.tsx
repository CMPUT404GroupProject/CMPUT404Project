import axios from "axios";
import React, { useEffect, useState } from "react";
import ReactMarkdown from "react-markdown";


interface OwnProps {
    post_type: string,
    post_title: string,
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

const PostSingular = ({post_type, post_title, source, origin, post_description, post_content_type, author, post_categories, count, comments, published, visibility, unlisted, editSwitch}: OwnProps) => {
    
    const [authorDisplayName, setAuthorDisplayName] = useState('None')
    const [authorGithub, setAuthorGithub] = useState('None')
    const [message, setMessage] = useState("");




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
                <button className="edit-button row-start-5 col-start-11 text-md rounded-lg text-white bg-yellow-600 place-self-center m-5 p-3">Edit Post</button>:
                null
            }
        </div>
    ) 
}

export default PostSingular