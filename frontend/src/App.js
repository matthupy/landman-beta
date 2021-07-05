import React from "react";
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link
} from "react-router-dom";

import AgreementTypes from './AgreementTypes';
import './App.css';

export default function LandmanRouter() {
  return (
    <Router>
      <Switch>
        <Route exact path="/">
          <AgreementTypes />
        </Route>
      </Switch>
    </Router>
  );
}
