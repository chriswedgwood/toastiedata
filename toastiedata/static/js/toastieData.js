import React, { Component } from 'react';
import ReactDOM from 'react-dom';
/*import Meetings from 'Meetings-api';*/

import axios from 'axios';
import ToastieDataSearchForm from './components/ToastieDataSearchForm';
import ToastieDataTable from './components/ToastieDataTable';
import Button from 'react-bootstrap/Button';
import Container from 'react-bootstrap/Container'
import Col from 'react-bootstrap/Col'
import Row from 'react-bootstrap/Row'
import * as geolib from 'geolib';
import Table from 'react-bootstrap/Table';
//import ToastieDataTable from './components/ToastieDataTable';
import Spinner from 'react-bootstrap/Spinner'
import _ from 'lodash'


class ToastieData extends Component {
  constructor(props) {
    super(props);

    this.onAreaChange = this.onAreaChange.bind(this);
    this.onStartChange = this.onStartChange.bind(this);
    this.onEndChange = this.onEndChange.bind(this);


    this.state = {
      area: 'Members', start: '', end: '', members: []

    };
  }






  getResults(area, start, end) {

    /*let timeBandSend = timeBand === 'all' ? '' : timeBand
    let daySend = day === 'all' ? '' : day
    let meetingTypeSend = meetingType === 'all' ? '' : meetingType
*/
    let queryString = `/api/members/?start=${start}&end=${end}`;
    console.log(queryString);
    const memberQuery = axios.get(queryString);
    axios.all([memberQuery]).then(axios.spread((...responses) => {
    let members = responses[0].data;
    this.setState({ area: 'Members', start: start, end: end, members: members, showSpinner: 0 });



    }))




  }

  componentDidMount() {


    //let day = new Date().toLocaleString('en-us', { weekday: 'long' });

    //this.setState({ showPostcode: 1 })
    //day, search, timeBand, access, isSearchChange, covid
    this.getResults(this.state.area, this.state.start, this.state.end);



  }



  onAreaChange = data => {



    this.setState({ showSpinner: 1, area: data });
    //this.getResults(data, this.state.search, this.state.timeBand, this.state.access, 0, this.state.covid, this.state.meetingType);

  }


  onStartChange = data => {


    this.setState({ showSpinner: 1, start: data });
    this.getResults(this.state.area, data, this.state.end);

  }

  onEndChange = data => {


    this.setState({ showSpinner: 1, end: data });
    this.getResults(this.state.area, this.state.start, data);

  }



  render() {

    let { area, start, end, members } = this.state;


   

    let firstCode = 0;
    if (members.length > 0) {
      let meetingCount = _.sumBy(members, 'meeting_count');
      firstCode = members[0].es_id + members.length + meetingCount;
    }


    return (

      <div>
        <ToastieDataSearchForm onAreaChange={this.onAreaChange} onStartChange={this.onStartChange} onEndChange={this.onEndChange}
          start={start} end={end} area={area} />
        <ToastieDataTable key={firstCode} members={members} />
      </div>








    );

  }

}


ReactDOM.render(<ToastieData />, window.react_mount);
