// typescript로 만든 component

import "./FredSeriesListView.scss";

import { Menu, Spin } from 'antd';
import { useEffect, useState } from "react";

import { FredSeriesInfo } from "../blocs/FredSeriesListBloc";
import { useBlocsContext } from "../blocs/BlocsContext";

export default function FredSeriesListView() {
    // state variable에 값이 들어가면 화면에 표시됨
    const [isLoading, setIsLoading] = useState<boolean>(true);
    const [fredSeriesList, setFredSeriesList] = useState<FredSeriesInfo[]>([]);

    // api 요청해서 server에서 가져오는 애
    const { fredSeriesListBloc, fredSeriesValuesBloc } = useBlocsContext();

    // bloc에서 받아온 data를 state로 연결(state variable로 넘겨줌)
    useEffect(() => {
        const subs = [
            fredSeriesListBloc.loading$.subscribe(setIsLoading),
            fredSeriesListBloc.fredSeriesList$.subscribe(setFredSeriesList),
        ];

        return () => {
            subs.forEach((x) => x.unsubscribe());
        };
    }, [fredSeriesListBloc]);

    // click -> query로 해당하는 value 불러옴
    const handleClick = (e: any) => {
        fredSeriesValuesBloc.query(e.key);
      };

    // loading 전에 동글이 icon 표시
    if (isLoading) {
        return <Spin />;
    }
    
    return (
        <div className="fred-series-list-view">
            <Menu
                onClick={handleClick}
                style={{ width: 320 }}
                defaultSelectedKeys={['1']}
                defaultOpenKeys={['sub1']}
                mode="inline"
            >
                {
                    fredSeriesList.map((x) => (
                        <Menu.Item key={x.series_id}>{x.title}</Menu.Item>
                    ))
                }
            </Menu>
        </div>
    );    
}