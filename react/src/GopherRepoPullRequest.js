import React, {Component} from 'react';
import {Container} from 'react-bootstrap';
import { ColumnChart } from 'react-chartkick';
import 'chart.js';
class GopherRepoPullRequest extends Component{
    constructor(props){
        super(props);
        this.state = {
            items:[],
            isLoaded: false,
        }
        
    }
    getData(){
        var { items } = this.state;
        var d = {};
        items.map((item)=>{
            d[item.date] = item.pull_requests;
        })
        return d;
      }
      getWeek(){
        var d = new Date();
     d.setDate(d.getDate()-2000);
     return d;
      }
    componentDidMount(){
        fetch('http://goldengophers.sociallycompute.io:5110/api/unstable/repo-groups/25156/repos/'+ window.location.pathname.split('/')[4]+'/reviews') //need more api calls
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
                    <ColumnChart width="80%" library={{scales: {
                    xAxes: [{
                        type: 'time',
                        time: {
                            unit: 'year'
                        }
                    }]
                    }}} data={this.getData()} download={true} />
                    </Container>
                </div>
            );
        }
        
    }
    
}
export default GopherRepoPullRequest;