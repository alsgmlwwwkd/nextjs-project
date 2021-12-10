import ReactWordcloud from 'react-wordcloud';
import { useLocation } from "react-router-dom";

const words = [
    {
      text: 'told',
      value: 64,
    },
    {
      text: 'mistake',
      value: 11,
    },
    {
      text: 'thought',
      value: 16,
    },
    {
      text: 'bad',
      value: 17,
    },
  ]
  
export default function Home() {
    return (
        <div>
            <ReactWordcloud words={words} />
        </div>
    );
        
}

