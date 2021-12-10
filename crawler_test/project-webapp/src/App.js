import './App.css';
import Navbar from "react-bootstrap/Navbar";

// import ReactWordcloud from 'react-wordcloud';
import 'tippy.js/dist/tippy.css';
import 'tippy.js/animations/scale.css';
// import Home from "./containers/Home";
import Routes from "./Routes";


// const words = [
//   {
//     text: 'told',
//     value: 64,
//   },
//   {
//     text: 'mistake',
//     value: 11,
//   },
//   {
//     text: 'thought',
//     value: 16,
//   },
//   {
//     text: 'bad',
//     value: 17,
//   },
// ]

function App() {
  return (
    // <ReactWordcloud words={words} />
    <div className="App container py-3">
      <Navbar collapseOnSelect bg="light" expand="md" className="mb-3">
        WordCloud
      </Navbar>
      {/* <Home /> */}
      <Routes />
    </div>
  );
}



export default App;
