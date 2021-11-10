import "./Home.css";

import FredSeriesListView from "../components/FredSeriesListView";

export default function Home() {
    return (
        <div className='Home'>
            <FredSeriesListView />
            <div className="lander">
                <h1>이생망</h1>
                <p>이번 생은 망했습니다</p>
            </div>
        </div>
    );
}