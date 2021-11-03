import logo from './logo.svg';
import './App.css';

import Navbar from "react-bootstrap/Navbar";
import Home from "./containers/Home"

function App() {
  return (
    <div className="App container py-3">
      <Navbar collapseOnSelect bg="light" expand="md" className="mb-3">
          <Navbar.Brand className="font-weight-bold text-muted">이생망</Navbar.Brand>
          <Navbar.Toggle />
      </Navbar>
      <Home/>
    </div>
  );
}

export default App;
