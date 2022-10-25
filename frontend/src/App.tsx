import React from "react";
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
import { Login, Profile } from "./pages";
import store, { persistor } from "./store";
import { PersistGate } from "redux-persist/integration/react";
import { Provider } from "react-redux";
import ProtectedRoute from "./routes/ProtectedRoute";
import Navbar from "./components/UserSidebar";

export default function App() {
  return (
    <Provider store={store}>
      <PersistGate persistor={persistor} loading={null}>
        <Router>
          <div className="bg-gray-900 w-full h-full">
            <Switch>
              <Route exact path="/login" component={Login} />
              <ProtectedRoute exact path="/" component={Profile} />
            </Switch>
          </div>
        </Router>
      </PersistGate>
    </Provider>
  );
}
