import FriendSidebar from "../components/FriendSidebar";
import PostCard from "../components/PostCard";
import PostSingular from "../components/PostSingular";
import UserSidebar from "../components/UserSidebar";
import { useEffect, useState, useContext } from "react";
import PostPopup from "../components/PostPopup";
import axios from "axios";
import GlobalContext from "./../context/GlobalContext";
import CommentModal from "./../components/CommentModal";
import {UserResponse} from "../utils/types";
import {RootState} from "../store";
import {useSelector} from "react-redux";
import useSWR from 'swr';
import {fetcher} from "../utils/axios";
import '../css/Profile.scss'

interface LocationState {
    userId: string;
}


const Profile = () => {
  const {showCommentModal} = useContext(GlobalContext);

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
  console.log(userId)
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

  useEffect(()=>{
      let tempPostsArray: {type: string, title: string, id: string, source: string, origin: string, 
          description: string, contentType: string, author: string, categories: string, count: number,
          comments: string, published: string, visibility: string, unlisted: boolean}[] = [];
      authorPostLink.myArray.forEach((item) =>{
          axios.get(item)
          .then((res)=>{
              res.data.items.forEach((post: any)=>{
                  tempPostsArray.push(post);
                  console.log(post);
              })
              setPostArray({posts: tempPostsArray});
          })
      })
      
  }, [authorPostLink])

  return (
    <div className="content">
        {showCommentModal && <CommentModal/>}
      {(postPopupClicked) ? <PostPopup onChange={handleChange}/> : null}

        <div className="sidebar-left">
            <div className="user-sidebar-card">
                <UserSidebar onChange={handlePostVisibility} postVisibility={allPosts}/>
            </div>
        </div>
        {(allPosts) ?
            <div className="main-content-middle">
                {postArray.posts.map((item) =>
                    <PostSingular post_type={item.type} post_title={item.title} post_id={item.id} source={item.source} origin={item.origin} post_description={item.description} 
                    post_content_type={item.contentType} author={item.author} post_categories={item.categories} count={item.count} comments={item.comments} published={item.published} 
                    visibility={item.visibility} unlisted={item.unlisted} editSwitch={false} />
                )}
            </div>:
              <div className="main-content-middle">
                {postArray.posts.map((item) =>
                    // @ts-ignore
                    {if(item.author.id.split('/')[4] === userId) {
                        return <div>
                                <PostSingular post_type={item.type} post_title={item.title} post_id={item.id} source={item.source} origin={item.origin} post_description={item.description} 
                                    post_content_type={item.contentType} author={item.author} post_categories={item.categories} count={item.count} comments={item.comments} published={item.published} 
                                    visibility={item.visibility} unlisted={item.unlisted} editSwitch={true}/>
                                </div>
                    }}
                )}
            </div>
        }        
        <div className="sidebar-right">
            <div className="friend-sidebar-card">
                <FriendSidebar onChange={handleChange}/>
            </div>
        </div>
    </div>
  );
};

export default Profile;