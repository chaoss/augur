import React, {Component} from 'react';
import {Container} from 'react-bootstrap';
import { BarChart } from 'react-chartkick';
import 'chart.js';
class GopherRepoTopTen extends Component{
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
            var ins = item.additions
            if (!(item.cmt_author_email in d)) d[item.cmt_author_email]=0;
          d[item.cmt_author_email] += ins;
        })
        return d;
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
                    <BarChart width="80%"  data={this.getData()} download={true} />
                    </Container>
                </div>
                
            );
        }
        
    }
    
}
export default GopherRepoTopTen;