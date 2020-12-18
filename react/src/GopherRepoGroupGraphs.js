import React, {Component} from 'react';
import {Container} from 'react-bootstrap';
import {ColumnChart, LineChart} from 'react-chartkick';
import 'chart.js';
class GopherRepoGroupGraphs extends Component{
    constructor(props){
        super(props);
        this.state = {
            items:[],
            isLoaded: false,
        }
        
    }
    getData(){
        var { items } = this.state;
        var dick = {};
        items.map(item=>
          dick[item.cmt_author_date] = item.additions
        )
        return dick;
      }
      getWeek(){
        var d = new Date();
     d.setDate(d.getDate()-2000);
     return d;
      }
    componentDidMount(){
        fetch('http://goldengophers.sociallycompute.io:5110/api/unstable/repo-groups/25156/repos/'+ window.location.pathname.split('/')[4]+'/lines-changed-by-author') //need more api calls
        .then(res =>res.json())                                                                                                                            //this is one of them
        .then(json=>{   
            this.setState({
                isLoaded: true,
                items: json,
            })
        });
        
    }

    render(){
        var { isLoaded, items } = this.state;
        if(!isLoaded){
            return (<div>Loading...</div>);
        }
        else {
            return (
                <div className="GopherRepoGroupGraphs">
                    <h1>Graphs:</h1>
                    <Container>
                    <LineChart library={{scales: {
            xAxes: [{
                type: 'time',
                time: {
                    unit: 'year'
                }
            }]
        }}} width="80%" xmin={this.getWeek()}  data={this.getData()} download={true} />
                    {items.map(item=>(
                        <tr key={item.cmt_author_email}>
                            
                        </tr>
                    ))}
                    </Container>
                </div>
                
            );



        //     <Card style={{ width: '18rem' }}>
        //     <Card.Body>
        //         <Card.Title>Repo Name</Card.Title>
        //         <Card.Img variant="top" src="holder.js/100px180" />
        //         <Card.Text>
        //             Repo info, pulled from API
        //         </Card.Text>
        //         <Button variant="primary">Go somewhere</Button>
        //     </Card.Body>
        // </Card>);
                    }
        
    }
    
}
export default GopherRepoGroupGraphs;