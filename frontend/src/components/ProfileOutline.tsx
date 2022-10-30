
import FriendSidebar from "./FriendSidebar";
import PostCard from "./PostCard";
import PostSingular from "./PostSingular";
import PostCardWithPhoto from "./PostCardWithPhoto";
import UserSidebar from "./UserSidebar";
import { useEffect, useState } from "react";
import PostPopup from "./PostPopup";
import axios from "axios";

import {UserResponse} from "../utils/types";
import {RootState} from "../store";
import {useSelector} from "react-redux";
import useSWR from 'swr';
import {fetcher} from "../utils/axios";
import '../css/ProfileOutline.scss'

const ProfileOutline = () => {
    // This is for the button that does the popup work
    const [postPopupClicked, setPostPopup] = useState(false);
    function handleChange(newValue: any) {
        setPostPopup(!postPopupClicked)
    }

    const [message, setMessage] = useState("");
    const [forceRender, setForceRender] = useState(false) 
    
    // This is for the button for seeing own posts
    const [allPosts, setAllPosts] = useState(true)
    function handlePostVisibility(newValue: any){
        setAllPosts(!allPosts)
    }

    // THIS IS TO GET CURRENT AUTHOR ID
    const account = useSelector((state: RootState) => state.auth.account);
    // @ts-ignore
    const userId = account?.id;

    interface PostState {
        posts: {type: string, title: string, id:string, source: string, origin: string, 
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

    // useEffect(() => {  
    //     console.log(postArray.posts[0].id)
    // },[postArray.posts])

    useEffect(()=>{
        let tempPostsArray: {type: string, title: string, id: string, source: string, origin: string, 
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

    return (
        <div className="page">
            {(postPopupClicked) ?
                <PostPopup />:
                null
            }

            
            <div className="content grid grid-cols-12 gap-2">
                <div className="user-sidebar-left col-span-3">
                    <UserSidebar onChange={handlePostVisibility} postVisibility={allPosts}/>
                </div>
                {(allPosts) ?
                    <div className="main-content-middle col-span-6">
                        {postArray.posts.map((item) =>
                            <PostSingular post_type={item.type} post_title={item.title} post_id={item.id} source={item.source} origin={item.origin} post_description={item.description} 
                            post_content_type={item.contentType} author={item.author} post_categories={item.categories} count={item.count} comments={item.comments} published={item.published} 
                            visibility={item.visibility} unlisted={item.unlisted} editSwitch={false}/>
                        )}
                    </div>:
                     <div className="main-content-middle col-span-6">
                        {postArray.posts.map((item) =>
                            {if(item.author === userId) {
                                return <div>
                                            <PostSingular post_type={item.type} post_title={item.title} post_id={item.id} source={item.source} origin={item.origin} post_description={item.description} 
                                            post_content_type={item.contentType} author={item.author} post_categories={item.categories} count={item.count} comments={item.comments} published={item.published} 
                                            visibility={item.visibility} unlisted={item.unlisted} editSwitch={true}/>
                                        </div>
                            }}
                        )}
                    </div>
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