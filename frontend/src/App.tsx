import React from "react";
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
import { LoginPage, Profile, UserProfile } from "./pages";
import store, { persistor } from "./store";
import { PersistGate } from "redux-persist/integration/react";
import { Provider } from "react-redux";
import ProtectedRoute from "./routes/ProtectedRoute";

export default function App() {
  return (
    <Provider store={store}>
      <PersistGate persistor={persistor} loading={null}>
        <Router>
          <div>
                <Route exact path="/login" component={LoginPage} />
                <ProtectedRoute exact path="/" component={Profile} />
                <ProtectedRoute exact path="/profile" component={UserProfile} />

          </div>
        </Router>

         {/* <div className="AppContainer">
          <div className="LogoContainer">
              INSERT IMAGE HERE
              <div className="AppName">
                NAME
              </div>
          </div>
          


          <div className="LoginBox">
            <Login />
          </div>
        </div> */}
      </PersistGate>
    </Provider>
  );
}
