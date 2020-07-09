import _ from 'lodash'
import React, { Component } from 'react'
import { Table } from 'semantic-ui-react'



class ToastieDataTable extends Component {
  constructor(props) {
    super(props);


    this.state = {
      data: props.members,
      column: null,
      direction: null,

    };
  }

  componentDidMount() {
    console.log("ToastieDataTable componentDidMount");
  }

  handleSort = (clickedColumn) => () => {
    const { column, data, direction } = this.state

    if (column !== clickedColumn) {
      this.setState({
        column: clickedColumn,
        data: _.sortBy(data, [clickedColumn]),
        direction: 'ascending',
      })

      return
    }

    this.setState({
      data: data.reverse(),
      direction: direction === 'ascending' ? 'descending' : 'ascending',
    })
  }

  render() {
    const { column, data, direction } = this.state
   
    let showPostcode = this.props.showPostcode;
    console.log('dataA');
    console.log(this.state);
    console.log('dataB');

    let tbl = _.map(data, ({ full_name , es_id, meeting_count, role_count, speech_count}) => {
      
      
        
     return (
        <Table.Row key={es_id}>
          <Table.Cell textAlign="center" >{full_name}</Table.Cell>
          <Table.Cell textAlign="center" >{es_id}</Table.Cell>
          <Table.Cell textAlign="center" >{meeting_count}</Table.Cell>
          <Table.Cell textAlign="center" >{role_count}</Table.Cell>
          <Table.Cell textAlign="center" >{speech_count}</Table.Cell>
        </Table.Row>
      )
    
    })

    
    return (
      <Table sortable celled>
        <Table.Header>
          <Table.Row>
            <Table.HeaderCell
              sorted={column === 'full_name' ? direction : null}
              onClick={this.handleSort('full_name')}
              textAlign="center"
            >
              Name
            </Table.HeaderCell>
            <Table.HeaderCell
              sorted={column === 'es_id' ? direction : null}
              onClick={this.handleSort('es_id')}
              textAlign="center"
            >
              Easyspeak Id
            </Table.HeaderCell>
            <Table.HeaderCell
              sorted={column === 'meeting_count' ? direction : null}
              onClick={this.handleSort('meeting_count')}
              textAlign="center"
            >
              Meetings
            </Table.HeaderCell>
            <Table.HeaderCell
              sorted={column === 'role_count' ? direction : null}
              onClick={this.handleSort('role_count')}
              textAlign="center"
            >
              Roles
            </Table.HeaderCell>
            <Table.HeaderCell
              sorted={column === 'speech_count' ? direction : null}
              onClick={this.handleSort('speech_count')}
              textAlign="center"
            >
              Speeches
            </Table.HeaderCell>
          </Table.Row>
        </Table.Header>
        <Table.Body>
          {tbl}
        </Table.Body>
      </Table>
    )
  }
}

export default ToastieDataTable;
