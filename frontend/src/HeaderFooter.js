import React from "react";

import "./App.css";

export const Navbar = class Navbar extends React.Component {
  toggleSidebar() {
    document.getElementById("sidebar").classList.toggle("toggled");
  }

  toggleLogoChanger() {
    const display = document.getElementById("logo-changer").style.display;
    if (display == "block") {
      document.getElementById("logo-changer").style.display = "none";
    } else {
      document.getElementById("logo-changer").style.display = "block";
    }
  }

  render() {
    return (
      <nav className="navbar navbar-expand navbar-theme">
        <a
          className="sidebar-toggle d-flex me-2"
          href={void 0}
          onClick={() => {
            this.toggleSidebar();
          }}
        >
          <i className="hamburger align-self-center"></i>
        </a>
        <form id="search-form" className="d-none d-sm-inline-block">
          <input
            id="search-input"
            className="form-control form-control-lite"
            type="text"
            placeholder="Search..."
          />
        </form>
        <div className="navbar-collapse collapse">
          <ul className="navbar-nav ms-auto">
            <li className="nav-item dropdown">
              <a
                id="messagesDropdown"
                className="nav-link dropdown-toggle position-relative"
                href="#"
                data-bs-toggle="dropdown"
              >
                Integrations
              </a>
            </li>
            <li className="nav-item dropdown">
              <a
                id="messagesDropdown"
                className="nav-link dropdown-toggle position-relative"
                href="#"
                data-bs-toggle="dropdown"
              >
                Switch Accounts
              </a>
            </li>
            <li className="nav-item dropdown">
              <a
                id="settingsDropdown"
                className="nav-link dropdown-toggle position-relative"
                href="#"
                onClick={() => {
                  this.toggleLogoChanger();
                }}
                data-bs-toggle="dropdown"
              >
                Settings
              </a>
            </li>
            <li className="nav-item dropdown">
              <a
                id="settingsDropdown"
                className="nav-link dropdown-toggle position-relative"
                href="#"
                data-bs-toggle="dropdown"
              >
                Logout
              </a>
            </li>
          </ul>
        </div>
      </nav>
    );
  }
};
export const Footer = class Footer extends React.Component {
  render() {
    return (
      <footer className="footer">
        <div className="container-fluid">
          <div className="row text-muted">
            <div className="col-8 text-start">
              <ul className="list-inline">
                {/* Left-side footer items go here */}
              </ul>
            </div>
            <div className="col-4 text-end">
              <p className="mb-0">
                © 2021 -{" "}
                <a
                  className="text-muted"
                  href="https://www.linkedin.com/in/matt-hupy/"
                  target="_blank"
                >
                  Matt Hupy
                </a>
              </p>
            </div>
          </div>
        </div>
      </footer>
    );
  }
};
