![image-20211218125830471](https://raw.githubusercontent.com/yeonnex/image-server/main/img/image-20211218125830471.png)

모든 `Student` 는 `Person`이다. 이를 `OOP에서는 is-a 관계`라고 한다.

상속 관계를 보통 is-a 관계라고 함

## is-a 관계

- 상속 관계
- 수학에서 부분집합 관계

![image-20211218130035354](https://raw.githubusercontent.com/yeonnex/image-server/main/img/image-20211218130035354.png)

## has-a 관계

![image-20211218130223183](https://raw.githubusercontent.com/yeonnex/image-server/main/img/image-20211218130223183.png)

- 컴포지션 관계라고도 함. 정확히 얘기하자면 집합(aggregation)인데, 퉁쳐서 그냥 composition이라고 부름
  - `WaterSpray` 가 `SprayHead` 를 가지고 있고, `SprayBottle` 도 가지고 있음

## 상속 vs 컴포지션

- 둘 다 재사용성을 위한 방법
- 상속으로 해결할 수 있는 문제를 컴포지션으로 해결 가능
  - 그 반대도 가능
  - 순전히 기술적인 관점
- 역사적으로 사람들의 선호는 왔다갔다
  - 초창기에는 상속을 과도하게 선호
  - 그 후 무조건 컴포지션이 답이라는 조언을 많이 따랐음 (현재 진행형)
- OO에서 큰 결정사항 중 하나 : 상속 vs 컴포지션을 고르는 것

## 상속 vs 컴포지션 (2)

- 일단 이 간단한 가이드라인을 따를 것
  - 실생활에서 개체들끼리의 관계를 기준으로 선택할 것
    - has-a 관계가 말이 된다면 : 컴포지션
    - is-a 관계가 말이 된다면 : 상속
- 물론 훌륭한 프로그래머들은 필요에 따라 이 규칙을 어김
- 나중에 상속 vs 컴포지션에 대해서는 좀 더 배울 것!
