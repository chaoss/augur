import React, {Component} from 'react';
import { Container, Table, Spinner } from 'react-bootstrap';
import { Link} from "react-router-dom";
class GopherRepoSubgroup extends Component{
    constructor(props){
        super(props);
        this.state = {
            items:[],
            isLoaded: false,
        }
    }
    componentDidMount(){
        fetch('http://goldengophers.sociallycompute.io:5110/api/unstable/repo-groups/'+ window.location.pathname.split('/')[2]+'/repos')
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
            return (<div>
                        <Spinner animation="border" role="status" >
                            
                        </Spinner>
                        <span >Loading...</span>
                    </div>);
        }
        else {
            return (
                <div className="GopherRepoSubgroup">
                    <h1>Repo Sub Groups:</h1>
                    <Container>
                    <Table responsive>
                        <thead>
                            <tr>
                                <th>Name</th> 
                                <th>Commits</th> 
                                <th>Issues</th> 
                                <th>Website URL</th>
                            </tr>
                        </thead>
                        <tbody>
                    {items.map(item=>(
                        <tr key={item.repo_name}>
                            <td><Link to={ window.location.pathname.split('/')[2]+'/graphs/' + item.repo_id}>{item.repo_name}</Link></td>
                            <td>{item.commits_all_time==null ? '-' : item.commits_all_time}</td>
                            <td>{item.issues_all_time==null ? '-' : item.issues_all_time}</td>
                            <td>{item.url}</td>
                        </tr>
                    ))}
                    </tbody>
                    </Table>
                    </Container>
                </div>
                
            );
        }
        
    }
    
}
export default GopherRepoSubgroup;