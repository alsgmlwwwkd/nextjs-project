// ts: typescript
// fred series를 가져오는 bloc
// subject: pipe

import { API } from "aws-amplify";
import { BehaviorSubject } from "rxjs";
import BlocBase from "./BlocBase";

export type FredSeriesInfo = {
    series_id: string;
    title: string;
    observation_start: string;
    observation_end: string;
};

// extends: 상속 - 3개 함수 구현 필요
export default class FredSeriesListBloc extends BlocBase {
    // class 내부에서만 쓰는 subject(data 밀어주는 pipe)
    private _loading$ = new BehaviorSubject<boolean>(true);
    private _fredSeriesList$ = new BehaviorSubject<FredSeriesInfo[]>([]);


    init() {
        // python: requests.get(url, ...) - synchronous call(요청 -> 대기 -> 처리)
        
        //asynchronous call: 비동기식 호출 -> 결과 안 기다림(결과가 돌아오면 함수 실행)
        API.get("ism", "/fred-series-list", {})
            .then((value) => {
                console.log(value);
                // loading 완료
                this._loading$.next(false);
                // 받아온 data 밀어넣어 주기
                this._fredSeriesList$.next(value);
            })
            .catch((error) => {
                console.log(error);
            }); 
    }

    clear() {
        // 다시 초기값으로 돌리기
        this._loading$.next(true);
        this._fredSeriesList$.next([]);
    }

    dispose() {
        this._loading$.complete();
        this._fredSeriesList$.complete();
    }
    // 외부에서 꺼내갈 수 있도록, 수정은 불가
    get loading$(): BehaviorSubject<boolean> {
        return this._loading$;
    }

    get fredSeriesList$(): BehaviorSubject<FredSeriesInfo[]> {
        return this._fredSeriesList$;
    }
}

