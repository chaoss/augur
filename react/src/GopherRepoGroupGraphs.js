import React, {Component} from 'react';
import {Container} from 'react-bootstrap';
import {ColumnChart} from 'react-chartkick';
import 'chart.js';
class GopherRepoGroupGraphs extends Component{
    constructor(props){
        super(props);
        this.state = {
            items:[],
            isLoaded: false,
        }
        
    }
    componentDidMount(){
        fetch('http://goldengophers.sociallycompute.io:5110/api/unstable/repo-groups/'+ window.location.pathname.split('/')[3]+'/lines-changed-by-author') //need more api calls
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
                    <ColumnChart data={[["exampleEmail1", 32], ["exampleEmail2", 46], ["exampleEmail3", 28]]} //example chart doesn't take values from api calls yet
                    xtitle = "EMAILS" ytitle = "ADDITIONS" />
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