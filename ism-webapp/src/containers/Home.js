import "./Home.css";

import { useLocation } from "react-router-dom";

// import FredSeriesListView from "../components/FredSeriesListView";
// import FredSeriesValuesView from "../components/FredSeriesValuesView";

export default function Home() {
    const { search } = useLocation();

    console.log("search", search);

    const params = new URLSearchParams(search);
    const name = params.get("name");

    return (
        <div className='Home'>
            {/* <FredSeriesListView />
            <FredSeriesValuesView /> */}
            <div className="lander">
                <h1>이생망</h1>
                <p>이번 생은 망했습니다</p>
            </div>
        </div>
    );
}