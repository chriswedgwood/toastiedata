import React, { Component } from 'react';
import ReactDOM from 'react-dom';
/*import Meetings from 'Meetings-api';*/

import axios from 'axios';
import ToastieDataSearchForm from './components/ToastieDataSearchForm';
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
  
    this.onTableTypeChange = this.onTableTypeChange.bind(this);
    this.onStartChange = this.onStartChange.bind(this);
    this.onEndChange = this.onEndChange.bind(this);
    

    this.state = {
    tableType : 'Members', start : null , end : null , members : null

    };
  }



  


  getResults(tableType, start, end) {

    /*let timeBandSend = timeBand === 'all' ? '' : timeBand
    let daySend = day === 'all' ? '' : day
    let meetingTypeSend = meetingType === 'all' ? '' : meetingType
*/
    let queryString = `/api/members`;
    
   
   
    
    const memberQuery = axios.get(queryString);
    

    axios.all([memberQuery]).then(axios.spread((...responses) => {
   
      let members = responses[0].data;
      
     
    
      
        

        this.setState({ tableType : 'Members', start : null , end : null , members : members});
      

      
    }))




  }

  componentDidMount() {


    //let day = new Date().toLocaleString('en-us', { weekday: 'long' });

    //this.setState({ showPostcode: 1 })
    //day, search, timeBand, access, isSearchChange, covid
    this.getResults(this.state.tableType, this.state.start, this.state.end);



  }


 
  onTableTypeChange = data => {

    console.log('onTableTypeChangeA')
    console.log(data)
    console.log('onTableTypeChangeB')

    this.setState({ showSpinner: 1, tableType: data });
    //this.getResults(data, this.state.search, this.state.timeBand, this.state.access, 0, this.state.covid, this.state.meetingType);

  }

  
  onStartChange = data => {

    this.setState({ showSpinner: 1, timeBand: data });
    this.getResults(this.state.day, this.state.search, data, this.state.access, 0, this.state.covid, this.state.meetingType);

  }

  onEndChange = data => {

    this.setState({ showSpinner: 1, timeBand: data });
    this.getResults(this.state.day, this.state.search, data, this.state.access, 0, this.state.covid, this.state.meetingType);

  }
  


  render() {

    const { tableType , start  , end , members } = this.state;
    
    

    


    return (

      <div>
        <ToastieDataSearchForm onTableTypeChange={this.onTableTypeChange} onStartChange={this.onStartChange} onEndChange={this.onEndChange}
         start={start} end={end} reportOption={tableType} />
    
      </div>








    );

  }

}


ReactDOM.render(<ToastieData/>, window.react_mount);
