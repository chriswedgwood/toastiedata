import React, { Component } from 'react';
import ReactDOM from 'react-dom';
/*import Meetings from 'Meetings-api';*/

import axios from 'axios';
import ToastieDataSearchForm from './components/ToastieDataSearchForm';
import ToastieDataTable from './components/ToastieDataTable';
import AwardsDataTable  from './components/AwardsDataTable';
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
      area: 'Members', start: '', end: '', members: [],bestSpeakers: [],bestEvaluators: [],bestTableTopicSpeakers: []

    };
  }






  getResults(area, start, end) {

    /*let timeBandSend = timeBand === 'all' ? '' : timeBand
    let daySend = day === 'all' ? '' : day
    let meetingTypeSend = meetingType === 'all' ? '' : meetingType
*/  
if (area === 'Members'){

    let queryString = `/api/members/?start=${start}&end=${end}`;
    console.log(queryString);
    const memberQuery = axios.get(queryString);
    axios.all([memberQuery]).then(axios.spread((...responses) => {
      let members = responses[0].data;
      this.setState({ area: area, start: start, end: end, members: members, showSpinner: 0 });
    }))
  }else
  {
    let bestSpeakersQueryString = `/api/bestspeakers/?start=${start}&end=${end}`;
    let bestEvaluatorsSpeakersQueryString = `/api/bestevaluators/?start=${start}&end=${end}`;
    let bestTableTopicsSpeakersQueryString = `/api/besttabletopicspeakers/?start=${start}&end=${end}`;
    console.log(bestSpeakersQueryString)
    const bestSpeakersQuery = axios.get(bestSpeakersQueryString);
    const bestEvaluatorsQuery = axios.get(bestEvaluatorsSpeakersQueryString);
    const bestTableTopicSpeakersQuery = axios.get(bestTableTopicsSpeakersQueryString);
    axios.all([bestSpeakersQuery, bestEvaluatorsQuery, bestTableTopicSpeakersQuery ]).then(axios.spread((...responses) => {
      console.log(responses)
      
      let bestSpeakers = responses[0].data;
      let bestEvaluators = responses[1].data;
      let bestTableTopicSpeakers = responses[2].data;
      console.log('XXXXXXX')
      console.log(bestSpeakers)
      console.log('XXXXXXX')

      this.setState({ area: area, start: start, end: end, bestSpeakers:bestSpeakers ,bestEvaluators: bestEvaluators,
        bestTableTopicSpeakers: bestTableTopicSpeakers, showSpinner: 0 });
    }))
    
  }



  }

  componentDidMount() {

    this.getResults(this.state.area, this.state.start, this.state.end);

  }



  onAreaChange = data => {
    this.setState({ showSpinner: 1, area: data });
    this.getResults(data, this.state.start, this.state.end);

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

    let { area, start, end, members,bestSpeakers, bestEvaluators ,bestTableTopicSpeakers } = this.state;

    

    let firstCode = 0;
    if (members.length > 0) {
      let meetingCount = _.sumBy(members, 'meeting_count');
      firstCode = members[0].es_id + members.length + meetingCount;
    }

    

    let areaDisplay
    if (area === 'Members' && members.length > 0 ) 
    {
      areaDisplay = <ToastieDataTable key={firstCode} members={members} />
    }
    else{
      areaDisplay = <div><AwardsDataTable title='Best Speakers' data={bestSpeakers} />
      <AwardsDataTable title='Best Evaluators' data={bestEvaluators} />
      <AwardsDataTable title='Best Table Topics Speakers' data={bestTableTopicSpeakers} /> 
      </div>
    }

    return (

      <div>
        <ToastieDataSearchForm onAreaChange={this.onAreaChange} onStartChange={this.onStartChange} onEndChange={this.onEndChange}
          start={start} end={end} area={area} />
          {areaDisplay}
        
      </div>








    );

  }

}


ReactDOM.render(<ToastieData />, window.react_mount);
