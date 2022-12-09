import '../css/PostCard.scss'

const PostCard = () => {

    return (
        <div className="post-card">
            <div className="author-profile-picture">
                <img src="https://images.unsplash.com/photo-1505628346881-b72b27e84530" alt="profile-picture"></img>
            </div>
            <div className="post-header">
                <div className="post-title">Post title</div>
                <div className="author-name">Author Name</div>
            </div>
            <div className="post-description">
                <p>
                    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris fringilla gravida auctor. 
                    Duis fermentum, risus vitae congue vulputate, dolor turpis tristique ex, vel blandit eros massa vel tortor. 
                    Praesent vitae ligula at quam iaculis bibendum eget quis lorem. Praesent feugiat orci vel neque auctor. 
                </p>
            </div>
            <div className="post-image">
                {/*<img src="https://images.unsplash.com/photo-1666949220096-27ef15cb96cd" alt="lambo"></img>*/}
                <img src="https://images.unsplash.com/photo-1666904428342-6975acc1735d" alt="desert"></img>
            </div>
            <div className="post-comments">0 Comments...</div>
            <div className="post-interact">
                <div className="like-count">0 Likes</div>
                <button className="post-like-button">Like</button>
                <button className="post-comment-button">Comment</button>
                <button className="post-share-button">Share</button>
            </div>
        </div>
    ) 
}

export default PostCard