import _ from 'lodash'
import React, { Component } from 'react'
import { Table } from 'semantic-ui-react'



class AwardsDataTable extends Component {
  constructor(props) {
    super(props);


    this.state = {
      data: props.data,
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
    const { column, direction } = this.state
    let title = this.props.title;
    let data = this.props.data;
   
 
    let tbl = _.map(data, ({ full_name , wins}) => {
      
      
        
     return (
        <Table.Row key={full_name}>
          <Table.Cell textAlign="center" >{full_name}</Table.Cell>
          
          <Table.Cell textAlign="center" >{wins}</Table.Cell>
         
        </Table.Row>
      )
    
    })

    
    return (
      <div>
        <h2>{title}</h2>
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
              sorted={column === 'wins' ? direction : null}
              onClick={this.handleSort('wins')}
              textAlign="center"
            >
              Wins
              </Table.HeaderCell>
          </Table.Row>
        </Table.Header>
        <Table.Body>
          {tbl}
        </Table.Body>
      </Table>
      </div>
    )
  }
}

export default AwardsDataTable;
