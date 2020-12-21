import Nav from 'react-bootstrap/Nav';
import Col from 'react-bootstrap/Col';
import InputGroup from 'react-bootstrap/InputGroup';
import FormControl from 'react-bootstrap/FormControl';
import GopherRepoGroup from './GopherRepoGroup'
import GopherRepoSubgroup from './GopherRepoSubgroup'
import GopherRepoGroupGraphs from './GopherRepoGroupGraphs'
import './App.css';
import logo from './logo.png'
import 'bootstrap/dist/css/bootstrap.min.css';
import { Container, Row } from 'react-bootstrap';
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
        <Container id='search'>
        <InputGroup size="lg">
    <InputGroup.Prepend>
      <InputGroup.Text id="inputGroup-sizing-lg">Search:</InputGroup.Text>
    </InputGroup.Prepend>
    <FormControl aria-label="Large" aria-describedby="inputGroup-sizing-sm" />
  </InputGroup>
  </Container>
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
      </Col>
      </Router>
      </Row>
    </div>
  );
}

export default App;

function Home() {
  return <h2>Home</h2>;
}