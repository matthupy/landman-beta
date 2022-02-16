import React from "react";
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Redirect,
  Link,
} from "react-router-dom";

import AgreementTypes from "./components/AgreementTypes";
import "./style/App.css";

import axios from "axios";

axios.defaults.xsrfCookieName = "csrftoken";
axios.defaults.xsrfHeaderName = "X-CSRFToken";

export default function LandmanRouter() {
  return (
    <Router>
      <Switch>
        <Route exact path="/">
          <Redirect to="/test" />
        </Route>
        <Route path="/test">
          <AgreementTypes />
        </Route>
      </Switch>
    </Router>
  );
}
