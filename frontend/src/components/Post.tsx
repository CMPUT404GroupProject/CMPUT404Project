import CardComponent from "./CardPost"

const Post = () => {

    return (
        <div className="max-w-xl rounded shadow-lg">
            <img className="w-full" src="https://images.unsplash.com/photo-1666373108681-b4964c59bf9b" alt=""></img>
            <div className="px-6 py-4">
                <div className="font-bold text-xl mb-2">Post title</div>
                <p className="text-gray-700 text-base">
                    Lorem ipsum dolor sit amet, consectetur adipisicing elit. Voluptatibus quia, nulla! Maiores et perferendis eaque, exercitationem praesentium nihil.
                </p>
            </div>
            <div className="px-6 py-4 flex space-x-4">
                <img className="rounded-full w-10 h-10" src="https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_1280.png" alt=""></img>
                <p>Author name</p>
            </div>
            <div className="px-6 pt-4 pb-2">
                <span className="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2">#photography</span>
                <span className="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2">#categories</span>
                <span className="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2">#winter</span>
            </div>
        </div>
    ) 
}

export default Post