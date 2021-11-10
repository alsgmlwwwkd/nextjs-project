import "./FredSeriesValuesView.scss";

import { useEffect, useState } from "react";

import { FredSeriesValue } from "../blocs/FredSeriesValuesBloc";
import Plot from "react-plotly.js";
import { Spin } from 'antd';
import { useBlocsContext } from "../blocs/BlocsContext";

export default function FredSeriesValuesView() {
    const [isLoading, setIsLoading] = useState<boolean>(true);
    const [fredSeriesValues, setFredSeriesValues] = useState<FredSeriesValue[]>([]);

    const { fredSeriesValuesBloc } = useBlocsContext();

    // bloc에서 받아온 data를 state로 연결(state variable로 넘겨줌)
    useEffect(() => {
        const subs = [
            fredSeriesValuesBloc.loading$.subscribe(setIsLoading),
            fredSeriesValuesBloc.fredSeriesValues$.subscribe(setFredSeriesValues),
        ];

        return () => {
            subs.forEach((x) => x.unsubscribe());
        };
    }, [fredSeriesValuesBloc]);

    

    // loading 전에 동글이 icon 표시
    if (isLoading) {
        return (
            <div className="fred-series-values-view">
                <Spin />
            </div>
            
        );
    }

    // console.log(fredSeriesValues);
    const series = {
        x: fredSeriesValues.map(x => x.date),
        y: fredSeriesValues.map(x => x.value),
        mode: "line",
    }

    const layout = {
        title: "Fred Series Values",
    };
    
    return (
        <div className="fred-series-list-view">
            <Plot data={[series]} layout={layout} />
        </div>
    );    
}