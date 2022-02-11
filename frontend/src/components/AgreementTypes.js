import React from "react";
import { Link } from "react-router-dom";
import axios from "axios";

import { Navbar, Footer } from "./HeaderFooter";
import { Sidebar } from "./Sidebar";

import "../style/App.css";

export default function AgreementTypes() {
  class Breadcrumbs extends React.Component {
    render() {
      return (
        <div className="header">
          <h1 className="header-title">Agreement Types</h1>
          <nav aria-label="breadcrumb">
            <ol className="breadcrumb">
              <li className="breadcrumb-item">
                <a href="#">Main</a>
              </li>
              <li className="breadcrumb-item">
                <a href="#">Code Table</a>
              </li>
              <li className="breadcrumb-item">
                <Link exact="true" to="/">
                  Agreement Types
                </Link>
              </li>
            </ol>
          </nav>
        </div>
      );
    }
  }

  class CardActions extends React.Component {
    render() {
      return (
        <div className="card-actions float-end">
          <a className="me-1" href="#">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              width="24"
              height="24"
              viewBox="0 0 24 24"
              fill="none"
              stroke="currentColor"
              strokeWidth="2"
              strokeLinecap="round"
              strokeLinejoin="round"
              className="feather feather-refresh-cw align-middle"
            >
              <polyline points="23 4 23 10 17 10"></polyline>
              <polyline points="1 20 1 14 7 14"></polyline>
              <path d="M3.51 9a9 9 0 0 1 14.85-3.36L23 10M1 14l4.64 4.36A9 9 0 0 0 20.49 15"></path>
            </svg>
          </a>
          <div className="d-inline-block dropdown show">
            <a href="#" data-bs-toggle="dropdown" data-bs-display="static">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                width="24"
                height="24"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                strokeWidth="2"
                strokeLinecap="round"
                strokeLinejoin="round"
                className="feather feather-more-vertical align-middle"
              >
                <circle cx="12" cy="12" r="1"></circle>
                <circle cx="12" cy="5" r="1"></circle>
                <circle cx="12" cy="19" r="1"></circle>
              </svg>
            </a>
            <div className="dropdown-menu dropdown-menu-end">
              <a className="dropdown-item" href="#">
                Action
              </a>
              <a className="dropdown-item" href="#">
                Another action
              </a>
              <a className="dropdown-item" href="#">
                Something else here
              </a>
            </div>
          </div>
        </div>
      );
    }
  }

  class CardHeader extends React.Component {
    render() {
      return (
        <div className="row">
          <div className="col-sm-12 col-md-6">
            <div
              className="dataTables_length"
              id="datatables-expensepayments_length"
            >
              <label>
                <span>Show </span>
                <select
                  name="datatables-expensepayments_length"
                  aria-controls="datatables-expensepayments"
                  className="custom-select custom-select-sm form-control form-control-sm"
                >
                  <option value="10">10</option>
                  <option value="25">25</option>
                  <option value="50">50</option>
                  <option value="100">100</option>
                </select>
                <span> entries</span>
              </label>
            </div>
          </div>
          <div className="col-sm-12 col-md-6">
            <div
              id="datatables-expensepayments_filter"
              className="dataTables_filter"
            >
              <label>
                Search:
                <input
                  type="search"
                  className="form-control form-control-sm"
                  placeholder=""
                  aria-controls="datatables-expensepayments"
                />
              </label>
            </div>
          </div>
        </div>
      );
    }
  }

  class CardFooter extends React.Component {
    render() {
      return (
        <div className="row">
          <div className="col-sm-12 col-md-5">
            <div
              className="dataTables_info"
              id="datatables-expensepayments_info"
              role="status"
              aria-live="polite"
            >
              Showing 1 to 10 of 20 entries
            </div>
          </div>
          <div className="col-sm-12 col-md-7">
            <div
              className="dataTables_paginate paging_simple_numbers float-end"
              id="datatables-expensepayments_paginate"
            >
              <ul className="pagination">
                <li
                  className="paginate_button page-item previous disabled"
                  id="datatables-expensepayments_previous"
                >
                  <a
                    href="#"
                    aria-controls="datatables-expensepayments"
                    data-dt-idx="0"
                    tabIndex="0"
                    className="page-link"
                  >
                    Previous
                  </a>
                </li>
                <li className="paginate_button page-item active">
                  <a
                    href="#"
                    aria-controls="datatables-expensepayments"
                    data-dt-idx="1"
                    tabIndex="0"
                    className="page-link"
                  >
                    1
                  </a>
                </li>
                <li className="paginate_button page-item ">
                  <a
                    href="#"
                    aria-controls="datatables-expensepayments"
                    data-dt-idx="2"
                    tabIndex="0"
                    className="page-link"
                  >
                    2
                  </a>
                </li>
                <li
                  className="paginate_button page-item next"
                  id="datatables-expensepayments_next"
                >
                  <a
                    href="#"
                    aria-controls="datatables-expensepayments"
                    data-dt-idx="3"
                    tabIndex="0"
                    className="page-link"
                  >
                    Next
                  </a>
                </li>
              </ul>
            </div>
          </div>
        </div>
      );
    }
  }

  class AgreementTypes_Table extends React.Component {
    constructor(props) {
      super(props);
      this.state = {
        agreementTypeList: [],
        modal: false,
        activeItem: {
          code: "",
          description: "",
        },
      };
    }

    componentDidMount() {
      this.refreshList();
    }

    refreshList = () => {
      axios
        .get("/api/agreement/types")
        .then((res) => this.setState({ agreementTypeList: res.data }))
        .catch((err) => console.log(err));
    };

    toggle = () => {
      this.setState({ modal: !this.state.modal });
    };

    handleDelete = (item) => {
      alert(
        "Deletes are not supported through the front end. Please use the Django Admin portal."
      );

      /*axios
              .delete(`/api/agreement/types/${item.code}/`)
              .then((res) => this.refreshList());*/
    };

    renderBody = () => {
      const items = this.state.agreementTypeList;

      return (
        items &&
        items.map(({ code, description }) => {
          return (
            <tr key={code}>
              <td>{code}</td>
              <td>{description}</td>
            </tr>
          );
        })
      );
    };

    render() {
      const items = this.state.agreementTypeList;

      return (
        <div className="row">
          <div className="col-sm-12">
            <table
              id="datatables-agreementtypes"
              className="table table-striped table-scrollable dataTable no-footer dtr-inline"
              role="grid"
              aria-describedby="datatables-expensepayments_info"
            >
              <thead>
                <tr role="row">
                  <th
                    className="sorting"
                    tabIndex="0"
                    aria-controls="datatables-expensepayments"
                    rowSpan="1"
                    colSpan="1"
                  >
                    Code
                  </th>
                  <th
                    className="sorting sorting_asc"
                    tabIndex="0"
                    aria-controls="datatables-expensepayments"
                    rowSpan="1"
                    colSpan="1"
                    aria-sort="ascending"
                  >
                    Description
                  </th>
                </tr>
              </thead>
              <tbody>{this.renderBody()}</tbody>
            </table>
          </div>
        </div>
      );
    }
  }

  class Page extends React.Component {
    render() {
      return (
        <div className="col-xxl-12">
          <div className="row">
            <div className="card">
              <div className="card-header">
                <CardActions />
                <h5 className="card-title mb-0">Agreement Types</h5>
              </div>
              <div className="card-body">
                <div
                  id="datatables-agreementtypes_wrapper"
                  className="dataTables_wrapper dt-bootstrap4 no-footer"
                >
                  <AgreementTypes_Table />
                </div>
              </div>
            </div>
          </div>
          <div className="row">
            <div className="card">
              <div className="card-header">
                <CardActions />
                <h5 className="card-title mb-0">Subject Types</h5>
              </div>
              <div className="card-body">
                <div
                  id="datatables-subjecttypes_wrapper"
                  className="dataTables_wrapper dt-bootstrap4 no-footer"
                >
                  <SubjectTypes_Table />
                </div>
              </div>
            </div>
          </div>
        </div>
      );
    }
  }

  class SubjectTypes_Table extends React.Component {
    constructor(props) {
      super(props);
      this.state = {
        subjectTypeList: [],
        modal: false,
        activeItem: {
          code: "",
          description: "",
        },
      };
    }

    componentDidMount() {
      this.refreshList();
    }

    refreshList = () => {
      axios
        .get("/api/subjecttypes/")
        .then((res) => this.setState({ subjectTypeList: res.data }))
        .catch((err) => console.log(err));
    };

    toggle = () => {
      this.setState({ modal: !this.state.modal });
    };

    handleDelete = (item) => {
      alert(
        "Deletes are not supported through the front end. Please use the Django Admin portal."
      );
    };

    renderBody = () => {
      const items = this.state.subjectTypeList;

      return (
        items &&
        items.map(({ code, description }) => {
          return (
            <tr key={code}>
              <td>{code}</td>
              <td>{description}</td>
            </tr>
          );
        })
      );
    };

    render() {
      const items = this.state.agreementTypeList;

      return (
        <div className="row">
          <div className="col-sm-12">
            <table
              id="datatables-agreementtypes"
              className="table table-striped table-scrollable dataTable no-footer dtr-inline"
              role="grid"
              aria-describedby="datatables-expensepayments_info"
            >
              <thead>
                <tr role="row">
                  <th
                    className="sorting"
                    tabIndex="0"
                    aria-controls="datatables-expensepayments"
                    rowSpan="1"
                    colSpan="1"
                  >
                    Code
                  </th>
                  <th
                    className="sorting sorting_asc"
                    tabIndex="0"
                    aria-controls="datatables-expensepayments"
                    rowSpan="1"
                    colSpan="1"
                    aria-sort="ascending"
                  >
                    Description
                  </th>
                </tr>
              </thead>
              <tbody>{this.renderBody()}</tbody>
            </table>
          </div>
        </div>
      );
    }
  }

  class Content extends React.Component {
    render() {
      return (
        <main className="content">
          <div className="container-fluid">
            <Breadcrumbs />
            <div className="row">
              <Page />
            </div>
          </div>
        </main>
      );
    }
  }

  class Main extends React.Component {
    render() {
      return (
        <div className="main">
          <Navbar />
          <Content />
          <Footer />
        </div>
      );
    }
  }

  return (
    <div className="wrapper" className="wrapper">
      <Sidebar />
      <Main />
    </div>
  );
}
