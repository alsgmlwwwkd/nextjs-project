// class 생성 - 상속을 위한 3개의 함수
abstract class BlocBase {
    // void: return x
    abstract init(): void;

    abstract clear(): void;

    abstract dispose(): void;
}

// 외부에서 쓰기 위해 export 필수
export default BlocBase;