const PostCardWithPhoto = () => {

    return (
        <div className="post-card-with-photo grid grid-rows-12 grid-cols-12 bg-gray-800 rounded-lg mb-2">
            <div className="author-profile-picture row-start-1 col-start-1 col-span-2 bg-black rounded-full h-20 w-20 place-self-center m-5"></div>
            <div className="author-name row-start-1 col-start-3 col-span-2 text-white text-lg justify-self-start self-center">Author Name</div>
            <div className="author-handle row-start-1 col-start-5 col-span-2 text-white text-md justify-self-start self-center">@author_handle</div>
            <div className="post-title row-start-2 col-start-3 col-span-8 text-white text-2xl mb-5">Post title</div>
            
            <div className="post-image row-start-3 col-start-3 col-span-9 text-white text-md mb-5">
                <img src="https://images.unsplash.com/photo-1470252649378-9c29740c9fa8"></img>
            </div>
            <div className="post-comments row-start-4 col-start-9 col-span-3 text-white text-center text-sm place-content-start bg-gray-900 rounded-lg p-2 mb-5">45 Comments...</div>
            <div className="like-count row-start-5 col-start-3 col-span-2 justify-self-start self-center text-white text-xs bg-indigo-500 rounded-lg p-2">327 Likes</div>
            <button className="post-like-button row-start-5 col-start-5 text-md rounded-lg text-white bg-green-600 place-self-center p-3">Like</button>
            <button className="post-comment-button row-start-5 col-start-7 text-md rounded-lg text-white bg-gray-700 place-self-center m-5 p-3">Comment</button>
            <button className="post-share-button row-start-5 col-start-9 text-md rounded-lg text-white bg-yellow-600 place-self-center m-5 p-3">Share</button>
        </div> 
    ) 
}

export default PostCardWithPhoto