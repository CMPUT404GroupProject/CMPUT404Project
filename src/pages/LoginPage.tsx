import { Login, Register } from "./";
import '../css/LoginPage.css';
import { useState } from "react";


export const LoginPage = () => {
    const [loginTrue, handleLogin] = useState(true)

    return (
        
        <div className="AppContainer">            
          {/* <div className="LogoContainer">
              INSERT LOGO HERE
              <div className="AppName">
                NAME
              </div>
          </div> */}
          <div className="LoginBox">
            <button className="OptionButton LoginSwitchButton" onClick={() => {handleLogin(true)}}>
                Login
            </button>
            <button className="OptionButton RegisterSwitchButton" onClick={() => {handleLogin(false)}}>
                Register
            </button>

            {(loginTrue) ?
                <Login />:
                <Register />
            }
          </div>
        </div> 
    );
  }
  
  export default LoginPage;
  