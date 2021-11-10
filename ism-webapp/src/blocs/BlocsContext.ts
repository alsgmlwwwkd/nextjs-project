import { createContext, useContext } from "react";

import BlocBase from "./BlocBase";
import FredSeriesListBloc from "./FredSeriesListBloc";
import FredSeriesValuesBloc from "./FredSeriesValuesBloc";

// block들의 집합 -> context로 wrapping해서 넘기기
export class Blocs {
    initialized = false;

    // 변수 선언
    fredSeriesListBloc = new FredSeriesListBloc();
    fredSeriesValuesBloc = new FredSeriesValuesBloc();

    // blocQueue = blockbase의 목록(type) : 값으로는 fredser -- 가 들어감
    blocQueue: BlocBase[] = [this.fredSeriesListBloc, this.fredSeriesValuesBloc];

    init() {
        if (this.initialized) return;

        console.log("[blocsContext.ts] Initializing all blocs");

        // for x in blocQueue:
        //  x.init() 과 동일
        this.blocQueue.forEach(x => x.init());

        this.initialized = true;
    }
}

// instance 생성 -> context를 만듦(route에서 만든걸 말단까지 보내기 위한)
export const blocs = new Blocs();

export const BlocsContext = createContext(new Blocs());

export function useBlocsContext() {
    return useContext(BlocsContext);
}