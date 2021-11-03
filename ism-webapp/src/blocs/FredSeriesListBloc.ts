// ts: typescript
// fred series를 가져오는 bloc

import BlocBase from "./BlocBase";

// extends: 상속 - 3개 함수 구현 필요
export default class FredSeriesListBloc extends BlocBase {
    init() {
        console.log("FredSeriesListBloc is initialized");
    }

    clear() {}

    dispose() {}
}

