// 최상단
import './App.css';

import { BlocsContext, blocs } from './blocs/BlocsContext';

// import Home from "./containers/Home"
import Navbar from "react-bootstrap/Navbar";
import Routes from "./Routes";
import { useEffect } from "react";

// import logo from './logo.svg';

function App() {
  // python: lambda x: x * 2
  useEffect(() => {
    // 호출이 될 함수, 처음에 한 번만 실행(app component 생성이 될 때 1번)
    blocs.init();
  }, [])

  return (
    <div className="App container py-3">
      <BlocsContext.Provider value={blocs}>
        <Navbar collapseOnSelect bg="light" expand="md" className="mb-3">
          <Navbar.Brand className="font-weight-bold text-muted">이생망</Navbar.Brand>
          <Navbar.Toggle />
        </Navbar>
        <Routes />
      </BlocsContext.Provider>
    </div>
  );
}

export default App;
