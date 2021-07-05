import './App.css';

import React, { Component } from 'react';
import axios from "axios";

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      agreementTypeList: [],
      modal: false,
      activeItem: {
        code: "",
        description: ""
      }
    }
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
  }

  handleDelete = (item) => {
    axios
      .delete(`/api/agreement/types/${item.code}/`)
      .then((res) => this.refreshList());
  };

  renderItems = () => {
    const items = this.state.agreementTypeList;

    return items.map((item) => (
      <li
        key={item.id}
        className="list-group-item d-flex justify-content-between align-items-center"
      >
        <span
          className={`todo-title mr-2`}
          title={item.description}
        >
          {item.description}
        </span>
        <span>
          <button
            className="btn btn-danger"
            onClick={() => this.handleDelete(item)}
          >
            Delete
          </button>
        </span>
      </li>
    ));
  };

  render() {
    return (
      <main className="container">
        <h1 className="text text-uppercase text-center my-4">Landman</h1>
        <div className="row">
          <div className="col-md-6 col-sm-10 mx-auto p-0">
            <div className="card p-3">
              <div className="mb-4">
              </div>
              <ul className="list-group list-group-flush border-top-0">
                {this.renderItems()}
              </ul>
            </div>
          </div>
        </div>
      </main>
    );
  }
}

export default App;
