import React from "react";
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Redirect,
  Link,
} from "react-router-dom";

import AgreementTypes from "./AgreementTypes";
import "./App.css";

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
