import React from 'react';
import Nav from 'react-bootstrap/Nav'
import Col from 'react-bootstrap/Col'
import Row from 'react-bootstrap/Row'

import _ from 'lodash'

import { Dropdown, Input } from 'semantic-ui-react'

const ENTER_KEY = 13;

class ToastieDataSearchForm extends React.Component {
  constructor(props) {
    super(props);
    this.handleTableTypeChange = this.handleTableTypeChange.bind(this);
    this.handleStartChange = this.handleStartChange.bind(this);
    this.handleEndChange = this.handleEndChange.bind(this);
    this.state = {}

  }

  handleTableTypeChange(eventKey,e) {
    console.log(e)
    this.props.onTableTypeChange(e.target.innerText);

  }
  handleStartChange(e) {
    this.props.onStartChange(e.target.value);
  }

  handleEndChange(e) {
    this.props.onEndChange(e.target.value);
  }
  render() {
    //let day = this.props.day;
    let reportOption = this.props.reportOption;
    

    const reportOptions = ["Members","Awards"]
    let activeIndex = reportOptions.findIndex(element => element.includes(reportOption));
    

    let reportNav =  reportOptions.map((value, index) => 
    <Nav.Item key={index}>
    <Nav.Link onSelect={this.handleTableTypeChange} eventKey={index}>{value}</Nav.Link>
  </Nav.Item>
  )

    
      
     

    return (

      <div className={'toastie-search-form'}>
        <Row className="justify-content-center ">
          <Col className="days" xs={10}>
          <Row><Nav fill variant="pills" activeKey={activeIndex} defaultActiveKey="0" >
         {reportNav} 
          

</Nav></Row></Col></Row>
        <Row>  
        <Col>
       
        </Col> 
        </Row>
        
      </div>
    );
  }
}



export default ToastieDataSearchForm;
