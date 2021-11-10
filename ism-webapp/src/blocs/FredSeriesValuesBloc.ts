import { API } from "aws-amplify";
import { BehaviorSubject } from "rxjs";
import BlocBase from "./BlocBase";

export type FredSeriesValue = {
    date: string,
    value: number;
};


export default class FredSeriesValuesBloc extends BlocBase {
    private _loading$ = new BehaviorSubject<boolean>(true);
    private _fredSeriesValues$ = new BehaviorSubject<FredSeriesValue[]>([]);

    init() {}

    // 값 요청 보내기
    query(series_id: string) {
        const query = `/fred-series-values?series_id=${series_id}`
        
        // 다른 메뉴 누를 때 기존 값 지워주기
        this._loading$.next(true);
        this._fredSeriesValues$.next([]);

        API.get("ism", query, {})
            .then((value) => {
                this._loading$.next(false);
                this._fredSeriesValues$.next(value);
            })
            .catch((error) => {
                console.error(error);
            }); 
    }

    clear() {
        this._loading$.next(true);
        this._fredSeriesValues$.next([]);
    }

    dispose() {
        this._loading$.complete();
        this._fredSeriesValues$.complete();
    }
    get loading$(): BehaviorSubject<boolean> {
        return this._loading$;
    }

    get fredSeriesValues$(): BehaviorSubject<FredSeriesValue[]> {
        return this._fredSeriesValues$;
    }
}

