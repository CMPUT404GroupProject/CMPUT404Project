import ProfileOutline from "../components/ProfileOutline";

interface LocationState {
    userId: string;
}


const Profile = () => {
  return (
    <div className="w-full h-full">
      <ProfileOutline></ProfileOutline>
    </div>
  );
};

export default Profile;
