
import FriendSidebar from "./FriendSidebar";
import PostCard from "./PostCard";
import PostSingular from "./PostSingular";
import PostCardWithPhoto from "./PostCardWithPhoto";
import UserSidebar from "./UserSidebar";
import React, { useEffect, useState } from "react";
import PostPopup from "./PostPopup";
import axios from "axios";
import {useHistory, useLocation} from "react-router";
import { withRouter } from 'react-router-dom';

const ProfileOutline = () => {
    const [postPopupClicked, setPostPopup] = useState(false);
    const [message, setMessage] = useState("");
    const [forceRender, setForceRender] = useState(false) 
    interface PostState {
        posts: {type: string, title: string, source: string, origin: string, 
            description: string, contentType: string, author: string, categories: string, count: number,
            comments: string, published: string, visibility: string, unlisted: boolean}[];
    }

    const [postArray, setPostArray] = useState<PostState>({
        posts: []
    })

    interface IState {
        myArray: string[];
    }

    const [authorPostLink, setPostLinks] = useState<IState>({
        myArray: []    
    })
    const postLinks: string[] = []

    function handleChange(newValue: any) {
        setPostPopup(!postPopupClicked)
    }    
    // THIS WILL GET ALL THE POSTS FROM EACH AUTHOR
    useEffect(()=>{
        // THIS PART GETS THE POST LINK FOR EACH AUTHOR
        const authors_link = `${process.env.REACT_APP_API_URL}/authors/`
        axios.get(authors_link)
        .then((res) => {
            var required_list = res.data.items;
            required_list.forEach((item: any) => {
                var posts_link = item.url + '/posts/';
                postLinks.push(posts_link);
            })
            if (JSON.stringify(postLinks) != JSON.stringify(authorPostLink.myArray)){
                setPostLinks({myArray: [...postLinks]})
            }
            else {
                return;
            }
            setMessage("Retrieved authors successfully");
        })
        .catch((err) => {
            setMessage("Error retrieving authors");
        });
    })

    useEffect(()=>{
        let tempPostsArray: {type: string, title: string, source: string, origin: string, 
            description: string, contentType: string, author: string, categories: string, count: number,
            comments: string, published: string, visibility: string, unlisted: boolean}[] = [];
        authorPostLink.myArray.forEach((item) =>{
            axios.get(item)
            .then((res)=>{
                res.data.forEach((post: any)=>{
                    tempPostsArray.push(post);
                })
                setPostArray({posts: tempPostsArray});
            })
        })
        
    }, [authorPostLink])

    useEffect(()=> {
        console.log(postArray.posts)
        console.log("I AM RERENDERING NOW")
        setForceRender(true)
    }, [postArray.posts])



    function returnPost(item: any) {
        return <PostSingular post_type={item.type} post_title={item.title} source={item.source} origin={item.origin} post_description={item.description} 
        post_content_type={item.contentType} author={item.author} post_categories={item.categories} count={item.count} comments={item.comments} published={item.published} 
        visibility={item.visibility} unlisted={item.unlisted}/>
    }
    return (
        <div className="page">
            {(postPopupClicked) ?
                <PostPopup />:
                null
            }

            
            <div className="content grid grid-cols-12 gap-2">
                <div className="user-sidebar-left col-span-3">
                    <UserSidebar></UserSidebar>
                </div>
                {(postArray.posts) ?
                    <div className="main-content-middle col-span-6">
                    
                    {postArray.posts.map((item) =>
                        <PostSingular post_type={item.type} post_title={item.title} source={item.source} origin={item.origin} post_description={item.description} 
                        post_content_type={item.contentType} author={item.author} post_categories={item.categories} count={item.count} comments={item.comments} published={item.published} 
                        visibility={item.visibility} unlisted={item.unlisted}/>
                    )}

                    </div>:
                    null 
                }
                
                <div className="friend-sidebar-right col-span-3">
                    <FriendSidebar
                        onChange={handleChange}
                    />
                </div>
            </div>
        </div>
    ) 
}

export default ProfileOutline