import React from 'react';
import Nav from 'react-bootstrap/Nav'
import Col from 'react-bootstrap/Col'
import Row from 'react-bootstrap/Row'
import Form from 'react-bootstrap/Form'
import {
  DateInput,
} from 'semantic-ui-calendar-react';

import _ from 'lodash'

import { Dropdown, Input } from 'semantic-ui-react'

const ENTER_KEY = 13;

class ToastieDataSearchForm extends React.Component {
  constructor(props) {
    super(props);
    this.handleAreaChange = this.handleAreaChange.bind(this);
    this.handleStartChange = this.handleStartChange.bind(this);
    this.handleEndChange = this.handleEndChange.bind(this);
    this.state = {}

  }

  handleAreaChange(eventKey, e) {

    this.props.onAreaChange(e.target.innerText);

  }
  
  handleStartChange = (event, { name, value }) => {
    
    this.props.onStartChange(value);
  }

  handleEndChange = (event, { name, value }) => {
    /*if (this.state.hasOwnProperty(name)) {
      this.setState({ [name]: value });
    }*/
    this.props.onEndChange(value);
  }
  render() {
    //let day = this.props.day;
    let area = this.props.area;
    let start = this.props.start;
    let end  = this.props.end;




    const areas = ["Members", "Awards"]
    let activeIndex = areas.findIndex(element => element.includes(area));


    let reportNav = areas.map((value, index) =>
      <Nav.Item key={index}>
        <Nav.Link onSelect={this.handleAreaChange} eventKey={index}>{value}</Nav.Link>
      </Nav.Item>
    )





    return (

      <div className={'toastie-search-form'}>
        <Form autoComplete="off">
          <Row className="justify-content-center ">
            <Col className="days" xs={10}>
              <Nav fill variant="pills" activeKey={activeIndex} defaultActiveKey="0" >
                {reportNav}


              </Nav>
            </Col>
          </Row>
          <Row>
            <Col>
              <DateInput
                name="date"
                placeholder="From"
                value={start}
                iconPosition="right"
                onChange={this.handleStartChange}
                dateFormat="YYYY-MM-DD"

              />
            </Col>
            <Col>
              <DateInput
                name="date"
                placeholder="To"
                value={end}
                iconPosition="right"
                onChange={this.handleEndChange}
                dateFormat="YYYY-MM-DD"
              />
            </Col>
          </Row>
        </Form>
      </div>
    );
  }
}



export default ToastieDataSearchForm;
