## 정적 Logger 클래스

- Logger.java
- Logger 는 파일에 로그를 남길 수 있게 해주는 간단한 클래스
- 그냥 `System.out.println()` 을 사용하면 안되나?
- 하지만 제대로 된 프로그램을 만들어서 배포한다면 최종 사용자가 있을 터
- 프로그램은 그 사용자의 PC에서 실행되니, 우린 그 컴퓨터의 콘솔창을 볼 수 없음
- **따라서 프로그램에서 예외나 버그가 발생했는데 그 내용을 콘솔창에 출력했다면, 우리에게 전혀 도움 안됨!**
- 그러므로 로그를 <u>파일에 남기는 게</u> 더 좋은 방법. 사용자에게 그 로그 파일을 보내달라고 하면 되기 때문
- 이것보다 뛰어난 로깅 시스템은 곧바로 클라우드 저장소에 로그를 남긴다던가 해서 사용자에게 로그 파일을 보내달라고 부탁할 필요도 없게 만드는 방법

쩄든, Logger 클래스의 구현으로 돌아와보자. 정적(static) 메서드만 사용해서 구현해볼 것이다.

[링크는 여기에](https://github.com/yeonnex/java-OO/tree/master/src/staticlogger)

