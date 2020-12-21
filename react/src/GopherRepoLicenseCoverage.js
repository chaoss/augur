import React, {Component} from 'react';
import {Container, Table} from 'react-bootstrap';
import { LineChart } from 'react-chartkick';
import 'chart.js';
class GopherRepoLicenseCoverage extends Component{
    constructor(props){
        super(props);
        this.state = {
            items:[],
            isLoaded: false,
        }
        
    }

    componentDidMount(){
        fetch('http://goldengophers.sociallycompute.io:5110/api/unstable/repo-groups/'+window.location.pathname.split('/')[2]+'/repos/'+ window.location.pathname.split('/')[4]+'/license-coverage') //need more api calls
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
                    <h1></h1>
                    <Container>
                    <Table responsive>
                        <thead>
                            <tr>
                                <th>License Coverage</th> 
                                <th>Total Files</th> 
                                <th>Files with Declared Licenses</th> 
                                <th>Files without Declared Licenses</th> 
                            </tr>
                        </thead>
                        <tbody>
                    {items.map(item=>(
                        <tr key={item.name}>
                            <td>{item.coverage==null ? '-' : item.coverage * 100 + '%'}</td>
                            <td>{item.total_files==null ? '-' : item.total_files}</td>
                            <td>{item.license_declared_files==null ? '-' : item.license_declared_files}</td>
                            <td>{item.license_declared_files==null ? '-' : item.total_files - item.license_declared_files}</td>
                        </tr>
                    ))}
                    </tbody>
                    </Table>
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
export default GopherRepoLicenseCoverage;