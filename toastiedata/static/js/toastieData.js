import React, { Component } from 'react';
import ReactDOM from 'react-dom';
/*import Meetings from 'Meetings-api';*/
import axios from 'axios';



class ToastieData extends Component {
    render() {
      return (
        <div className="shopping-list">
          <h1>Shopping List for {this.props.name}</h1>
          <ul>
            <li>Instagram</li>
            <li>WhatsApp</li>
            <li>Oculus</li>
          </ul>
        </div>
      );
    }
  }
  


ReactDOM.render(<ToastieData name="chris" />, window.react_mount);
