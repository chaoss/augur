import React, {Component} from 'react';
import { Container, Table } from 'react-bootstrap';
class GopherRepoGroup extends Component{
    constructor(props){
        super(props);
        this.state = {
            items:[],
            isLoaded: false,
        }
    }
    componentDidMount(){
        fetch('http://goldengophers.sociallycompute.io:5110/api/unstable/repo-groups')
        .then(res =>res.json())
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
                <div className="GopherRepoGroup">
                    <h1>Repo Groups:</h1>
                    <Container>
                    <Table responsive>
                        <thead>
                            <tr>
                                <th>Name</th> 
                                <th>Description</th> 
                                <th>Website</th> 
                                <th>Last Modified</th>
                            </tr>
                        </thead>
                        <tbody>
                    {items.map(item=>(
                        <tr key={item.rg_name}>
                            <td>{item.rg_name}</td>
                            <td>{item.rg_description}</td>
                            <td>{item.rg_website}</td>
                            <td>{item.rg_last_modified}</td>
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
export default GopherRepoGroup;