import './App.css';

// import Home from "./containers/Home"
import Navbar from "react-bootstrap/Navbar";
import Routes from "./Routes";

// import logo from './logo.svg';

function App() {
  return (
    <div className="App container py-3">
      <Navbar collapseOnSelect bg="light" expand="md" className="mb-3">
        <Navbar.Brand className="font-weight-bold text-muted">이생망</Navbar.Brand>
        <Navbar.Toggle />
      </Navbar>
      <Routes />
    </div>
  );
}

export default App;
