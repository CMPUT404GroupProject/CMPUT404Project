import ProfileOutline from "../components/ProfileOutline";
import GlobalContext from "./../context/GlobalContext";
import CommentModal from "./../components/CommentModal";
import { useContext, useEffect} from "react";

interface LocationState {
    userId: string;
}


const Profile = () => {
  const {showCommentModal} = useContext(GlobalContext);
  useEffect (() => {
  }, [showCommentModal]);
  return (
    <div className="w-full h-full">
      {showCommentModal && <CommentModal/>}
      <ProfileOutline></ProfileOutline>
    </div>
  );
};

export default Profile;
