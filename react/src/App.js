// import logo from './logo.svg';
// import Card from 'react-bootstrap/Card';
// import Button from 'react-bootstrap/Button';
import Nav from 'react-bootstrap/Nav';
import Col from 'react-bootstrap/Col';
// import CardDeck from 'react-bootstrap/CardDeck';
import InputGroup from 'react-bootstrap/InputGroup';
import FormControl from 'react-bootstrap/FormControl';
import GopherRepoGroup from './GopherRepoGroup'
import GopherRepoSubgroup from './GopherRepoSubgroup'
import GopherRepoGroupGraphs from './GopherRepoGroupGraphs'
import './App.css';
import logo from './logo.png'
import 'bootstrap/dist/css/bootstrap.min.css';
import { Image, Row } from 'react-bootstrap';
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link
} from "react-router-dom";
function App() {
  return (
    <div className="App">
      {/* <Container> */}
        <Row>
        <Router>
        <Col xs={2}>
        <img src={logo} width='100%'></img>
        <Nav defaultActiveKey="/home" className="flex-column">

          <Link to="/home">Home</Link>
          <Link to='/groups'>Groups</Link>
          <Nav.Link eventKey="link-2">Link</Nav.Link>
          <Nav.Link eventKey="disabled" disabled>
            Disabled
          </Nav.Link>
        </Nav>
        
        </Col>
        <Col>
        <InputGroup size="lg">
    <InputGroup.Prepend>
      <InputGroup.Text id="inputGroup-sizing-lg">Search:</InputGroup.Text>
    </InputGroup.Prepend>
    <FormControl aria-label="Large" aria-describedby="inputGroup-sizing-sm" />
  </InputGroup>

        {/* A <Switch> looks through its children <Route>s and
            renders the first one that matches the current URL. */}
        <Switch>
        <Route path="/groups/*/graphs/*">
        <GopherRepoGroupGraphs />
            </Route>
        <Route path="/groups/*">
        <GopherRepoSubgroup />
            </Route>
          <Route path="/groups">
            <GopherRepoGroup />
          </Route>
          <Route path="/">
            <Home />
          </Route>
        </Switch>
    
      {/* <GopherRepoGroup></GopherRepoGroup> */}
        {/* <CardDeck>
        <Card style={{ width: '18rem' }}>
          <Card.Body>
            <Card.Title>Repo Name</Card.Title>
            <Card.Img variant="top" src="holder.js/100px180" />
            <Card.Text>
              Repo info, pulled from API
            </Card.Text>
            <Button variant="primary">Go somewhere</Button>
          </Card.Body>
      </Card>
      </CardDeck> */}
      </Col>
      </Router>
      </Row>
    {/* </Container> */}
    </div>
  );
}

export default App;


function Home() {
  return <h2>Home</h2>;
}