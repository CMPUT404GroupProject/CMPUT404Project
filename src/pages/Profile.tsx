import FriendSidebar from "../components/FriendSidebar";
import PostCard from "../components/PostCard";
import PostSingular from "../components/PostSingular";
import UserSidebar from "../components/UserSidebar";
import { useEffect, useState, useContext } from "react";
import PostPopup from "../components/PostPopup";
import axios from "axios";
import GlobalContext from "./../context/GlobalContext";
import CommentModal from "./../components/CommentModal";
import InboxModal from "./../components/InboxModal";
import AddFriendModal from "./../components/AddFriendModal";
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
  const {showCommentModal, showInboxModal, showAddFriendModal} = useContext(GlobalContext);

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
  const token = useSelector((state: RootState) => state.auth.token)
  // @ts-ignore
  const userId = account?.id;
  interface PostState {
      posts: {type: string, title: string, id:string, source: string, origin: string, 
          description: string, contentType: string, content: string, author: string, categories: string, count: number,
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
      const authors_link_2 = `https://cmput404f22t17.herokuapp.com/authors/`    //These are authors from team 17
      const authors_link_3 = `https://fallprojback.herokuapp.com/authors/`      //These are authors from team 5
      const authors_link_4 = `https://c404-team8.herokuapp.com/api/authors/`

      axios.all([axios.get(authors_link),
                axios.get(authors_link_2, {auth: {username:'argho', password:'12345678!'}}),    //These are from team 17, the good team
                axios.get(authors_link_3, {auth: {username:'admin', password:'admin'}}),    //These are from team 5, the bad team
                axios.get(authors_link_4, {auth: {username:'node', password:'cmput404'}})])      
      .then(axios.spread((res, res2, res3, res4) => {
          var required_list = res.data.items;   //These are my authors
          var required_list_2 = res2.data.items;    //These are Team 17's authors
          var required_list_3 = res3.data.items;    //These are Team 5's authors
          var required_list_4 = res4.data.items;

          required_list.forEach((item: any) => {
            var posts_link = item.url + '/posts/';
            postLinks.push(posts_link);
          })
          required_list_2.forEach((item: any) => {
            var posts_link_2 = item.url + 'posts/';
            postLinks.push(posts_link_2);
          })
          required_list_3.forEach((item: any) => {
            var posts_link_3 = item.url + '/posts/';
            postLinks.push(posts_link_3);
          })
          required_list_4.forEach((item: any) => {
            var posts_link_4 = item.url + 'posts/';
            postLinks.push(posts_link_4);
          })


          if (JSON.stringify(postLinks) != JSON.stringify(authorPostLink.myArray)){
              setPostLinks({myArray: [...postLinks]})
          }
          else {
              return;
          }
          setMessage("Retrieved authors successfully");
      }))
      .catch((err) => {
          setMessage("Error retrieving authors");
      });
  })

  useEffect(()=>{
      let tempPostsArray: {type: string, title: string, id: string, source: string, origin: string, 
          description: string, contentType: string, content: string, author: string, categories: string, count: number,
          comments: string, published: string, visibility: string, unlisted: boolean}[] = [];
      authorPostLink.myArray.forEach((item) =>{
                if (item.includes('socialdistribution-cmput404.herokuapp.com') || item.includes('cmput404f22t17.herokuapp.com') || item.includes('c404-team8.herokuapp.com')){
            axios.get(item, {auth: {username:'argho', password:'12345678!'}})
            .then((res)=>{
                console.log(item)
                res.data.items.forEach((post: any)=>{
                    tempPostsArray.push(post);
                    //console.log(post);
                })
                setPostArray({posts: tempPostsArray});
            })
          }
          else if(item.includes('fallprojback.herokuapp.com')){
            axios.get(item, {auth: {username:'admin', password:'admin'}})
            .then((res)=>{
                res.data.forEach((post: any)=>{
                    tempPostsArray.push(post);
                    // console.log(post);
                })
                setPostArray({posts: tempPostsArray});
            })
          }
      })
      
  }, [authorPostLink])

  return (
    <div className="content">
        {showCommentModal && <CommentModal/>}
        {showInboxModal && <InboxModal/>}
        {showAddFriendModal && <AddFriendModal/>}
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
                    post_content_type={item.contentType} post_content={item.content} author={item.author} post_categories={item.categories} count={item.count} comments={item.comments} published={item.published} 
                    visibility={item.visibility} unlisted={item.unlisted} editSwitch={false} />
                )}
            </div>:
              <div className="main-content-middle">
                {postArray.posts.map((item) =>
                    // @ts-ignore
                    {if(item.author.id) {
                        // @ts-ignore
                        {if(item.author.id.split('/')[4] === userId){
                            return <div>
                                <PostSingular post_type={item.type} post_title={item.title} post_id={item.id} source={item.source} origin={item.origin} post_description={item.description} 
                                    post_content_type={item.contentType} post_content={item.content} author={item.author} post_categories={item.categories} count={item.count} comments={item.comments} published={item.published} 
                                    visibility={item.visibility} unlisted={item.unlisted} editSwitch={true}/>
                                </div>
                        }}
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