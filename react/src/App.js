// import logo from './logo.svg';
// import Card from 'react-bootstrap/Card';
// import Button from 'react-bootstrap/Button';
import Nav from 'react-bootstrap/Nav';
import Col from 'react-bootstrap/Col';
// import CardDeck from 'react-bootstrap/CardDeck';
import InputGroup from 'react-bootstrap/InputGroup';
import FormControl from 'react-bootstrap/FormControl';
import GopherRepoGroup from './GopherRepoGroup'
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import { Row } from 'react-bootstrap';
function App() {
  return (
    <div className="App">
      {/* <Container> */}
        <Row>
        <Col xs={3}>
          
        <Nav defaultActiveKey="/home" className="flex-column">
          <Nav.Link href="/home">Active</Nav.Link>
          <Nav.Link eventKey="link-1">Link</Nav.Link>
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
      <GopherRepoGroup></GopherRepoGroup>
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
      </Row>
    {/* </Container> */}
    </div>
  );
}

export default App;
