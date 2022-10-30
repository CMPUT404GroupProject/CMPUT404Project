const PostCard = () => {

    return (
        <div className="post-card grid grid-rows-12 grid-cols-12 bg-gray-800 rounded-lg mb-2">
            <div className="author-profile-picture row-start-1 col-start-1 col-span-2 bg-black rounded-full h-20 w-20 place-self-center m-5"></div>
            <div className="author-name row-start-1 col-start-3 col-span-2 text-white text-lg justify-self-start self-center">Author Name</div>
            <div className="author-handle row-start-1 col-start-5 col-span-2 text-white text-md justify-self-start self-center">@author_handle</div>
            <div className="post-title row-start-2 col-start-3 col-span-8 text-white text-2xl mb-5">Post title</div>
            
            <div className="post-description row-start-3 col-start-3 col-span-9 text-white text-md mb-5">
                <p>
                    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris fringilla gravida auctor. 
                    Duis fermentum, risus vitae congue vulputate, dolor turpis tristique ex, vel blandit eros massa vel tortor. 
                    Praesent vitae ligula at quam iaculis bibendum eget quis lorem. Praesent feugiat orci vel neque auctor. 
                </p>
            </div>
            <div className="post-comments row-start-4 col-start-9 col-span-3 text-white text-center text-sm place-content-start bg-gray-900 rounded-lg p-2 mb-5">45 Comments...</div>
            <div className="like-count row-start-5 col-start-3 col-span-2 justify-self-start self-center text-white text-sm bg-indigo-500 rounded-lg m-5 p-2">327 Likes</div>
            <button className="post-like-button row-start-5 col-start-5 text-md rounded-lg text-white bg-green-600 place-self-center m-5 p-3">Like</button>
            <button className="post-comment-button row-start-5 col-start-7 text-md rounded-lg text-white bg-gray-700 place-self-center m-5 p-3">Comment</button>
            <button className="post-share-button row-start-5 col-start-9 text-md rounded-lg text-white bg-yellow-600 place-self-center m-5 p-3">Share</button>
        </div>
    ) 
}

export default PostCard