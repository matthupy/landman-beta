import React, { useState } from "react";
import { NavLink } from "react-router-dom";

import ondemand_logo from "../style/static/ondemand-logo.png";
import logo from "../style/static/landdox-logo.png";
import logo_blue from "../style/static/landdox-logo-blue.png";
import avatar from "../style/static/avatar.jpg";
import "../style/App.css";

class Sidebar_Nav extends React.Component {
  render() {
    return (
      <ul className="sidebar-nav">
        <li className="sidebar-header">Main</li>
        <li className="sidebar-item">
          <a className="sidebar-link">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              width="24"
              height="24"
              viewBox="0 0 26 26"
              fill="none"
              stroke="currentColor"
              strokeWidth="2"
              strokeLinecap="round"
              strokeLinejoin="round"
              className="feather feather-map align-middle me-2"
            >
              <polygon points="1 6 1 22 8 18 16 22 23 18 23 2 16 6 8 2 1 6"></polygon>
              <line x1="8" y1="2" x2="8" y2="18"></line>
              <line x1="16" y1="6" x2="16" y2="22"></line>
            </svg>
            <span>Map</span>
          </a>
          <a className="sidebar-link">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              width="24"
              height="24"
              viewBox="0 0 26 26"
              fill="none"
              stroke="currentColor"
              strokeWidth="2"
              strokeLinecap="round"
              strokeLinejoin="round"
              className="feather feather-calendar align-middle me-2"
            >
              <rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect>
              <line x1="16" y1="2" x2="16" y2="6"></line>
              <line x1="8" y1="2" x2="8" y2="6"></line>
              <line x1="3" y1="10" x2="21" y2="10"></line>
            </svg>
            <span>Calendar</span>
          </a>
          <a
            className="sidebar-link"
            data-bs-target="#payments"
            data-bs-toggle="collapse"
            aria-expanded="true"
          >
            <svg
              xmlns="http://www.w3.org/2000/svg"
              width="24"
              height="24"
              viewBox="0 0 24 24"
              fill="none"
              stroke="currentColor"
              stroke-width="2"
              stroke-linecap="round"
              stroke-linejoin="round"
              class="feather feather-code align-middle me-2"
            >
              <polyline points="16 18 22 12 16 6"></polyline>
              <polyline points="8 6 2 12 8 18"></polyline>
            </svg>
            <span className="align-middle">Code Tables</span>
          </a>
          <ul
            id="code-tables"
            className="sidebar-dropdown list-unstyled collapse show"
            data-bs-parent="#sidebar"
          >
            <li className="sidebar-item">
              <NavLink
                className="sidebar-link"
                exact
                to="/"
                activeStyle={{ background: "#e9ecef", color: "#212529" }}
              >
                <span>Agreement Types</span>
              </NavLink>
            </li>
          </ul>
          <a className="sidebar-link">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              width="24"
              height="24"
              viewBox="0 0 26 26"
              fill="none"
              stroke="currentColor"
              strokeWidth="2"
              strokeLinecap="round"
              strokeLinejoin="round"
              className="feather feather-bar-chart-2 align-middle me-2"
            >
              <line x1="18" y1="20" x2="18" y2="10"></line>
              <line x1="12" y1="20" x2="12" y2="4"></line>
              <line x1="6" y1="20" x2="6" y2="14"></line>
            </svg>
            <span>Reports</span>
          </a>
          <a className="sidebar-link">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              width="24"
              height="24"
              viewBox="0 0 26 26"
              fill="none"
              stroke="currentColor"
              strokeWidth="2"
              strokeLinecap="round"
              strokeLinejoin="round"
              className="feather feather-folder align-middle me-2"
            >
              <path d="M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z"></path>
            </svg>
            <span>Documents</span>
          </a>
          <a
            className="sidebar-link"
            data-bs-target="#forms"
            data-bs-toggle="collapse"
            aria-expanded="false"
          >
            <svg
              xmlns="http://www.w3.org/2000/svg"
              width="24"
              height="24"
              viewBox="0 0 26 26"
              fill="none"
              stroke="currentColor"
              strokeWidth="2"
              strokeLinecap="round"
              strokeLinejoin="round"
              className="feather feather-file-text align-middle me-2"
            >
              <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path>
              <polyline points="14 2 14 8 20 8"></polyline>
              <line x1="16" y1="13" x2="8" y2="13"></line>
              <line x1="16" y1="17" x2="8" y2="17"></line>
              <polyline points="10 9 9 9 8 9"></polyline>
            </svg>
            <span className="align-middle">Forms</span>
          </a>
          <ul
            id="forms"
            className="sidebar-dropdown list-unstyled collapse show"
            data-bs-parent="#sidebar"
          >
            <li className="sidebar-item">
              <a className="sidebar-link">Abstract</a>
            </li>
            <li className="sidebar-item">
              <a className="sidebar-link">AFE</a>
            </li>
            <li className="sidebar-item">
              <a className="sidebar-link">Contacts</a>
            </li>
            <li className="sidebar-item">
              <NavLink
                className="sidebar-link"
                to="/lease"
                activeStyle={{ background: "#e9ecef", color: "#212529" }}
              >
                Lease
              </NavLink>
            </li>
            <li className="sidebar-item">
              <a className="sidebar-link">Tract</a>
            </li>
          </ul>
        </li>
        <li className="sidebar-header">Admin</li>
        <li className="sidebar-item">
          <a
            className="sidebar-link collapsed"
            data-bs-target="#import"
            data-bs-toggle="collapse"
            aria-expanded="false"
          >
            <svg
              xmlns="http://www.w3.org/2000/svg"
              width="24"
              height="24"
              viewBox="0 0 26 26"
              fill="none"
              stroke="currentColor"
              strokeWidth="2"
              strokeLinecap="round"
              strokeLinejoin="round"
              className="feather feather-arrow-down-circle align-middle me-2"
            >
              <circle cx="12" cy="12" r="10"></circle>
              <polyline points="8 12 12 16 16 12"></polyline>
              <line x1="12" y1="8" x2="12" y2="16"></line>
            </svg>
            <span className="align-middle">Import</span>
          </a>
          <ul
            id="import"
            className="sidebar-dropdown list-unstyled collapse"
            data-bs-parent="#sidebar"
          >
            <li className="sidebar-item">
              <a className="sidebar-link">Data</a>
            </li>
            <li className="sidebar-item">
              <a className="sidebar-link">Maps</a>
            </li>
            <li className="sidebar-item">
              <a className="sidebar-link">Payments</a>
            </li>
          </ul>
          <a
            className="sidebar-link collapsed"
            data-bs-target="#settings"
            data-bs-toggle="collapse"
            aria-expanded="false"
          >
            <svg
              xmlns="http://www.w3.org/2000/svg"
              width="24"
              height="24"
              viewBox="0 0 26 26"
              fill="none"
              stroke="currentColor"
              strokeWidth="2"
              strokeLinecap="round"
              strokeLinejoin="round"
              className="feather feather-settings align-middle me-2"
            >
              <circle cx="12" cy="12" r="3"></circle>
              <path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z"></path>
            </svg>
            <span className="align-middle">Settings</span>
          </a>
          <ul
            id="settings"
            className="sidebar-dropdown list-unstyled collapse"
            data-bs-parent="#sidebar"
          >
            <li className="sidebar-item">
              <a className="sidebar-link">Forms</a>
            </li>
            <li className="sidebar-item">
              <a className="sidebar-link">Labels</a>
            </li>
            <li className="sidebar-item">
              <a className="sidebar-link">Company Settings</a>
            </li>
          </ul>
        </li>
        <li className="sidebar-header">Audit</li>
        <li className="sidebar-item">
          <a className="sidebar-link">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              width="24"
              height="24"
              viewBox="0 0 26 26"
              fill="none"
              stroke="currentColor"
              strokeWidth="2"
              strokeLinecap="round"
              strokeLinejoin="round"
              className="feather feather-activity align-middle me-2"
            >
              <polyline points="22 12 18 12 15 21 9 3 6 12 2 12"></polyline>
            </svg>
            <span>Company History</span>
          </a>
        </li>
        <li className="sidebar-header">Super Admin</li>
        <li className="sidebar-item">
          <a className="sidebar-link">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              width="24"
              height="24"
              viewBox="0 0 26 26"
              fill="none"
              stroke="currentColor"
              strokeWidth="2"
              strokeLinecap="round"
              strokeLinejoin="round"
              className="feather feather-bar-chart-2 align-middle me-2"
            >
              <line x1="18" y1="20" x2="18" y2="10"></line>
              <line x1="12" y1="20" x2="12" y2="4"></line>
              <line x1="6" y1="20" x2="6" y2="14"></line>
            </svg>
            <span>*NEW* Reports</span>
          </a>
        </li>
      </ul>
    );
  }
}

export const Sidebar = class Sidebar extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      ondemand: 1,
      landdox: 0,
      landdox_blue: 0,
    };
  }

  changeLogo() {
    console.info("onclick...");
    console.info("ondemand_logo: " + this.state.ondemand);
    console.info("landdox_logo: " + this.state.landdox);
    console.info("landdox_blue_logo: " + this.state.landdox_blue);
    if (
      this.state.ondemand == 1 &&
      this.state.landdox == 0 &&
      this.state.landdox_blue == 0
    ) {
      document.getElementById("ondemand_logo").style.display = "none";
      document.getElementById("landdox_logo").style.display = "block";
      this.setState({ ondemand: 0, landdox: 1 });
    } else if (
      this.state.ondemand == 0 &&
      this.state.landdox == 1 &&
      this.state.landdox_blue == 0
    ) {
      document.getElementById("landdox_logo").style.display = "none";
      document.getElementById("landdox_blue_logo").style.display = "block";
      this.setState({ landdox: 0, landdox_blue: 1 });
    } else if (
      this.state.ondemand == 0 &&
      this.state.landdox == 0 &&
      this.state.landdox_blue == 1
    ) {
      document.getElementById("landdox_blue_logo").style.display = "none";
      document.getElementById("ondemand_logo").style.display = "block";
      this.setState({ landdox_blue: 0, ondemand: 1 });
    }
  }

  render() {
    return (
      <nav ref={this.sidebarRef} id="sidebar" className="sidebar">
        <a
          style={{ display: "block" }}
          id="ondemand_logo"
          className="sidebar-brand"
          href="index.html"
        >
          <img
            id="ion-ios-pulse-strong"
            src={ondemand_logo}
            className="App-logo"
            alt="logo"
          />
        </a>
        <a
          style={{ display: "none" }}
          id="landdox_logo"
          className="sidebar-brand"
          href="index.html"
        >
          <img
            id="ion-ios-pulse-strong"
            src={logo}
            className="App-logo"
            alt="logo"
          />
        </a>
        <a
          style={{ display: "none" }}
          id="landdox_blue_logo"
          className="sidebar-brand"
          href="index.html"
        >
          <img
            id="ion-ios-pulse-strong"
            src={logo_blue}
            className="App-logo"
            alt="logo"
          />
        </a>
        <div className="sidebar-content">
          <div className="sidebar-user">
            <img
              src={avatar}
              className="img-fluid rounded-circle mb-2"
              alt="Matt Hupy"
            />
            <div className="fw-bold">Matt Hupy</div>
            <small>Landdox</small>
          </div>
          <div style={{ display: "none" }} id="logo-changer">
            <hr />
            <button
              className="btn btn-primary"
              onClick={() => {
                this.changeLogo();
              }}
            >
              Change Logo
            </button>
            <hr />
          </div>
          <ul className="sidebar-nav">
            <Sidebar_Nav />
          </ul>
        </div>
      </nav>
    );
  }
};
