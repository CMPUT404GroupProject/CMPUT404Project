import { Login, Register } from "./";
import '../css/LoginPage.css';
import { useState } from "react";


export const LoginPage = () => {
    const [loginTrue, handleLogin] = useState(true)

    return (
        
        <div className="AppContainer">            
          <div className="LogoContainer">
          </div>
          <div className="ButtonBar">
            <div className="AppName">
              social distribution
            </div>
            <button className="OptionButton" id="RegisterSwitchButton" onClick={() => {handleLogin(false)}}>
              Register
            </button>
            <button className="OptionButton" id="LoginSwitchButton" onClick={() => {handleLogin(true)}}>
              Login
            </button>
          </div>
          <div className="LoginBox">
            {(loginTrue) ?
                <Login />:
                <Register />
            }
          </div>
        </div> 
    );
  }
  
  export default LoginPage;
  