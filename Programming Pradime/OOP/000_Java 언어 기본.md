```java
public class HelloWorld {
    public static void main(String[] args){
        System.out.println("Hello WOrld!!!");
    }
}
```

- **Java**에서는 "hello world" 같은 간단한 걸 하더라도 언제나 **클래스 필요**

## 한 파일에서 최고 레벨의 public 클래스는 딱 하나만!

- 한 .java 파일에는 최고 레벨 public 클래스가 하나만 있어야 함
- 둘 이상일 경우 컴파일 안됨

```java
public class Student { // 컴파일 오류
    // 코드 생략
}
public class HelloWorld {
    // 코드 생략
}
```

- 파일 하나 당, public 달린 클래스는 하나만 들어간다! 자바의 특이한 점!

## 내포 클래스

```java
public class HelloWorld {
    class Teacher { // OK
        // 코드 생략
    }
    public class Student { // OK
        // 코드 생략
    }
}
```

- 클래스 안에 다른 클래스를 넣을 수 있음
  - 안에 있는 클래스를 내포(nested)클래스라 부름
  - 중첩 클래스, 내부 클래스라고도 부름
- 이때 내포 클래스는 public 이어도 상관 없음

## main 함수

```java
public static void main(String args[]){
    ...
}
```

- 프로그램의 시작점(entry point)
- 반드시 이 시그내쳐(signature) 대로 main 함수를 만들어야 함
- 매개변수 : `String[] args` 
  - 문자열 배열
  - 커맨드 라인으로부터 받은 인자

이건 Java Virtual Machine과의 약속이다. "main 이라는 함수가 무조건 내 프로그램의 시작점이다"
그렇기 때문에 반드시 이 시그내쳐를 지켜야 한다.

## 올바른 개행 방법

> public static String lineSeparator();

```java
String name = "mumu";
int score = 98;
System.out.printf("%s's score = %d%s", name, score, System.lineSeparator());
```

- 플랫폼에 알맞은 개행 문자를 반환하는 메서드
  - Linux : `\n` 반환
  - Windows : `\r\n` 반환

## 가변 인자

방금 `printf()` 함수 사용시, 인자가 계속 바뀌는 걸 볼 수 있었다. 어떤 건 인자가 3개고, 4개고... 함수 오버로딩인가? 근데 그건 아닌게 인자 100개를 넣으면 어떡할거? 변수 타입도 매번 다를텐데.

함수오버로딩한게 아니라, 가변인자를 쓴 것임.

> public PrintStream printf(String format, Object... args);

- ... 앞에 자료형을 반드시 넣어야 함
- 해당 자료형의 데이터만 인자로 전달 가능

```java
public void printNames(String... name) {...} // String 형만 인자로 전달 가능
public void printScores(int... score) {...} // int 형만 인자로 전달 가능
```

- Object 라는 자료형을 쓸 경우 모든 자료형을 넣을 수 있음

> 생각해보니, println 같은 함수를 그냥 호출했는데, 내가 만든 함수도 아니고 System 에서 사용한다는데 그 시스템은 어디에 있는줄 알고 마음대로 사용할 수 있나? C#에서는 using같은 걸 써서 쓰고 싶은 라이브러리 경로를 명시해줬었는데.

## package

> package <패키지 경로>;

- C# 의 네임스페이스와 비슷한 개념
- 라이브러리처럼 생각해도 좋고, 네임스페이스처럼 생각해도 좋음
- **연관된 클래스들끼리 묶는 기법**

## 패키지 종류

- 자바 기본(built-in) 패키지 (자바가 제공해줌)
  - 이름이 java 로 시작하는 패키지들
  - 예 ) `java.lang`, `java.util` ...
- 프로그래머가 직접 만든 (user-defined) 패키지

## 패키지의 목적

- 이름 충돌 문제를 피할 수 있게 해줌

Java 에 기본적으로 내장된 `Math` 클래스 : **java.lang.Math**
내가 만든 `Math` 클래스 : **academy.seoyeon.Math**

## 패키지 이름 짓기

- 패키지 이름의 중복을 최소화 해야함
- 그래서 보통 회사의 도메인명을 패키지 이름에 사용 (단, 역순으로)
  - 예 : 삼성(Samsung.com) 이라는 회사에서 패키지를 만들 경우
    - package com.samsung.<패키지이름>
  - 예: : POCU아카데미 (pocu.academy) 에서 패키지를 만들 경우
    - package academy.pocu.<패키지이름>

![image-20211224124718559](https://raw.githubusercontent.com/yeonnex/image-server/main/img/image-20211224124718559.png)

## 자, 그럼 이제 컴파일을 해볼까?

C에서는 커맨드라인에 직접 명령어를 입력해서 컴파일을 했었다. 자바에서도 원래 **기본은** `커맨드라인 컴파일`이다.

![image-20211224125951271](https://raw.githubusercontent.com/yeonnex/image-server/main/img/image-20211224125951271.png)

src 에 내가 만든 소스코드가 그대로 있고, class 라는 폴더를 하나 만들어주었다. 이 class 폴더 밑에는 컴파일 된 결과물이 들어갈 것이다.

## 커맨드 라인에서 컴파일하기

> hellopocu$ javac -d class\ src\academy\pocu\\*.java

위 명령으로 컴파일을 하면, 컴파일한 java 클래스의 패키지 이름과 동일한 폴더들이 class 폴더 밑에 생성된다.

![image-20211224144731743](https://raw.githubusercontent.com/yeonnex/image-server/main/img/image-20211224144731743.png)

그리고, 그 안에 HelloPocu.class 라는 파일이 생기게 된다.

## javac 명령어

- .java 파일이 무사히 컴파일되면 class 파일이 나옴
  - 이름은 .java 파일과 동일
  - 이 .class 파일에는 바이트코드가 들어있음
- 옵션: -d
  - .class 파일을 저장할 경로
- <컴파일 결과물을 자장할 경로> 안에 .java 파일의 패키지 구조와 동일한 폴더가 생김

## 폴더 구조

![image-20211225080118950](https://raw.githubusercontent.com/yeonnex/image-server/main/img/image-20211225080118950.png)

## 프로그램 실행하기

아래처럼 명령하면 어떤 경로에서든 실행이 가능하다.

> $ java -classpath D:\hellopocu\class\ academy.pocu.HelloPocu

## java 명령어

> java -classpath <class 파일 위치> <클래스 이름>

- C나 C#처럼 컴파일하면 OS가 알고있는 실행파일(예:exe)이 나오지 않음
  - 대신 바이트코드(*.class) 가 나옴
- 이 .class 파일을 실행하는 명령어임
- <클래스 이름>
  - 실행할 .class 파일 이름
  - 이 .class 파일에는 **반드시 main 함수가 들어있어야 함**

## java 명령어 : -classpath 옵션

- .class 파일의 위치를 알려주는 옵션
- .class 파일의 가장 위, 즉 루트 폴더까지만 넣어준다.
- ![image-20211225082236575](https://raw.githubusercontent.com/yeonnex/image-server/main/img/image-20211225082236575.png)

## 흔히 하는 실수 : 클래스명 앞에 패키지 누락

- 실행하고자 하는 클래스의 패키지 이름을 누락하면?

  - 오류 발생
  - 클래스 이름 앞에 반드시 패키지 이름 붙여야 함

  ![image-20211225082345222](https://raw.githubusercontent.com/yeonnex/image-server/main/img/image-20211225082345222.png)

## 배포하기

- 내가 만든 라이브러리나 프로그램을 배포하는 방법
- C#의 경우
  - 라이브러리: .dll 파일을 만듦
  - 프로그램: .exe 파일을 만듦
- Java의 경우
  - 라이브러리와 프로그램 모두 .jar 파일을 만듦

## 새로운 폴더 추가

배포용 만들 때는 lib 폴더에 만드는 것이 일반적. jar 파일만 만들어 주면 되기 때문에 굳이 어떤 특정 폴더일 필요는 없지만 일반적으로 아래와 같은 구조를 따름.

![image-20211225082642980](https://raw.githubusercontent.com/yeonnex/image-server/main/img/image-20211225082642980.png)

## jar 명령어

클래스 파일 다 모아서 뭉쳐 .jar 파일로 만드는 명령어이다.

> jar <옵션> <jar 파일이름> <최상위 패키지 경로>

`hellopocu\class$ jar -cf ..\lib\hellopocu.jar academy`

- .jar 파일을 만드는 명령어
- 옵션 : -cf
  - c: create(생성)
  - f: 만들어질 .jar 파일의 이름을 지정. f 뒤에 파일명이 와야 함

## .jar 파일 만들기

- 정상적으로 명령어가 실행되면, 아래와 같이 .jar 파일이 생성됨

  ![image-20211225083309371](https://raw.githubusercontent.com/yeonnex/image-server/main/img/image-20211225083309371.png)

## .jar 파일 실행

![image-20211225083419159](https://raw.githubusercontent.com/yeonnex/image-server/main/img/image-20211225083419159.png)

실행을 해보면, 실행이 안된다... main manifest attribute 가 없다는 말과 함께...

## .jar 은 사실 .zip 파일

- .jar 은 사실 단순히 .zip 파일에 지나지 않음
  - 실체로 압축 프로그램으로 압축을 풀 수도 있음.

![image-20211225083641915](https://raw.githubusercontent.com/yeonnex/image-server/main/img/image-20211225083641915.png)

## META-INF 폴더

- .jar 파일 내부를 보면 META-INF\MANIFEST.MF 라는 파일이 있음
- .jar 를 만들 때 같이 생성되는 파일

## MANIFEST 파일

- 자바 애플리케이션의 정보를 담고 있는 **메타데이터 파일**
- .jar 파일을 만들 때 이 파일을 같이 넣어줄 수 있음
- **.jar 파일의 시작점(메인함수)에 대한 정보를 넣어야 함** 이게 제일 중요
- 그 밖에도 여러 정보를 담을 수 있음
  - 궁금하면 찾아보자

## MANIFEST 파일 만들기

![image-20211225084241784](https://raw.githubusercontent.com/yeonnex/image-server/main/img/image-20211225084241784.png)

## 다시 .jar 파일 만들기

`hellopocu\class$ jar -cfm ..\lib\hellopocu.jar ..\src\Manifest.txt academy`

- 추가된 옵션 -m
  - .jar 파일을 만들때 manifest 파일도 함께 넣겠다는 의미

## 다시 .jar 파일 실행하기

`hellopocu$ java -jar lib\hellopocu.jar`

## java.lang

- java.lang 의 모든 클래스는 import 없이도 그냥 디폴트로 사용가능
- 기본 패키지
- 모든 .java  파일에 자동으로 임포트되는 패키지
- 사실상 아래 코드가 모든 파일에 자동으로 들어간다고 보면 됨
  - import java.lang.*
- System 은 java.lang 안에 들어있는 클래스 중 하나
- 이제 왜 임포트 없이 println() 을 사용할 수 있는지 알게 되었다!

## java는 크로스 플랫폼인가?

- 자바의 장점으로 항상 언급되는 부분
- 크로스 플랫폼(cross-platform)이란?
  - 특정 언어로 작성한 코드를 여러 플랫폼에서 실행할 수 있다는 의미
  - 즉, 여러 디바이스와 운영체제에서 실행가능한 소프트웨어

정답은 **네** 그리고 **아니오** 이다.

왜 그런지는 컴파일 및 실행과정을 조금 더 알아볼 필요가 있다.

## 전통적인 컴파일 방식(예: C)

![image-20211225090116661](https://raw.githubusercontent.com/yeonnex/image-server/main/img/image-20211225090116661.png)

초록색 박스의 과정을 하나로 퉁쳐서 컴파일이라 한다. 오브젝트 코드는 각 파일마다 하나씩 나오기 때문에, 링커로 오브젝트 코드를 합쳐 하나의 .exe파일(기계어, 머신코드 실행파일)을 만들어낸다.

## 전통적인 컴파일 및 실행

- 컴파일을 하면 실행파일이 나옴
- 실행파일은 기계어이며 운영체제가 직접 실행하는 파일
- 이렇게 해서 나온 파일은 특정 운영체제, 특정 플랫폼에서만 돌아감
- 각 운영체제/디바이스마다 실행파일을 **따로 만들어야** 함
  - 컴파일러가 소스코드를 각 운영체제/디바이스에 맞는 기계어로 바꿔줌
  - 소스코드는 안바꿔도 됨
  - C 는 이런 관점에서 크로스 플랫폼

- C로 작성한 소스코드는 진정한 크로스 플랫폼
  - C가 컴파일 안되는 환경은 굉장히 적기 때문
  - 소스코드는 크로스 플랫폼이지만, 실행파일은 따로 그 환경에서 컴파일해주어야 함

## 자바의 컴파일 모델

- 코드를 컴파일 한 결과는 바이트코드
  - 실행파일이 아님
- 바이트코드(byte code)란?
  - 어떤 운영체제/디바이스가 이해하는 명령어가 아님
  - JVM 이라는 특수한 프로그램이 이해하는 명령어
  - JVM이 실행중에 최종 플랫폼(윈도우나 리눅스 등)에 맞는 명령어로 바꿔서 실행해줌
  - JVM에 맞게 최적화됐지만 당연히 기계어보다는 느림

## 자바 가상 머신(Java Virtual Machine, JVM)

![image-20211225090949559](https://raw.githubusercontent.com/yeonnex/image-server/main/img/image-20211225090949559.png)

- 각 운영체제에 설치하는 별도의 프로그램
  - 각 운영체제/디바이스마다 다른 버전을 설치 (윈도우용 JVM, Mac용 JVM...)
- Java 의 바이트코드를 실행함
- 따라서 운영체제나 디바이스의 영향을 받지 않음
  - 이런 개념에서 크로스 플랫폼! 윈도우용 실행파일, 맥용 실행파일을 안만들어도 되니까.

## Java의 플랫폼은 JVM ?

- JVM이 설치 안되어있다면?
  - Java 프로그램 실행불가
  - 따라서 Java의 플랫폼은 JVM이라 볼 수 있음
  - 이런 관점에서는 크로스 플랫폼이라 하기엔 어폐가 있음
- JVM이 바이트코드를 실제 디바이스에서 실행하는 방식은 다양
  - 과거 JVM은 인터프리터 방식으로 동작
  - 최신 JVM은 JIT(just-in-time) 컴파일을 추가
  - 여러가지 컴파일 방식이 공존하는 형태

## Java가 인기를 끈 진짜 이유?

크로스플랫폼... 이라는 측면 자체는 위에서 봤듯이 아닐 수도 있음. 그것보다는 메모리 관리적인 측면이 훨씬 강함. 그외의 이유로는 좀 더 역사적인 이유인데, 닷컴 버블과 관련이 있음.

## 자바 애플릿(Java applet)

닷컴 버블 하면서 웹브라우저가 인기가 많아졌을 때, 그때 웹 자체에서 실행할 수 있는 프로그램이 없었음. 워낙 초창기였기 때문에...

- 지금은 쓰이지 않음
- 웹 브라우저 안에서 실행가능한 작은 Java 프로그램
- 코드를 컴파일하여 바이트 코드를 웹에 업로드
- 웹 브라우저에서 java applet 을 지원한다면, 실행 가능
- 배포 및 실행 절차
  - 1. 프로그래머가 코드 패키지를 웹에 업로드해둠
    2. 사용자가 웹 브라우저에서 이 페이지를 방문
    3. 웹 브라우저가 이 패키지를 다운로드 후 실행
- 웹 브라우저 안에 JVM이 들어가 있던 것!

## 자바 애플릿의 장점

- 데스크탑 수준의 기능을 웹에서 실행 가능했던 거의 유일한 플랫폼
  - 이 당시는 인터넷이 대중화되기 시작하던 시점
  - 이 당시 웹 브라우저의 기능은 정적인 문서를 보여주는 정도
- 미래에 새로운 플랫폼이 나오더라도 다시 컴파일 안해도됨! 바이트 코드가 올라가 있으니까!

## 자바 애플릿의 현 모습

- 최신 웹 브라우저들은 자바 애플릿을 지원하지 않음
  - 이제는 웹표준만으로 그런 기능들을 구현할 수 있기 때문
  - 자바스크립트, 웹 어셈블리 등으로 작성한 웹앱이 자바 애플릿을 대체
- 참고로 서버에서 실행되는 비슷한 개념의 프로그램은 아직 유효
  - 서블릿(servlet)

## 모듈

자바는 패키지 시스템이었다. 처음에는 패키지 구조로 만족했지만 시간이 지나면서 패키지 구조의 제약점이 보이기 시작했다. 물론 아직 패키지 시스템은 유효! 그런데 좀 더 효율적으로 배포를 하고 싶거나 그럴때 모듈 시스템을 이용하면 좋다. 자바 최신 버전(9)부터 모듈을 지원하기 시작했다.

## 기본 방식은 패키지

![image-20211225094811078](https://raw.githubusercontent.com/yeonnex/image-server/main/img/image-20211225094811078.png)

(src 폴더가 academy 폴더 위에 있음) 하늘색박스까지가 패키지 경로!

## 기존 패키지 시스템의 한계 1

어떤 자바 앱을 실행하고 있는데, 정확히 어떤 클래스들을 사용하고 있는지 한번에 찾을 쉬울 방법이 없었다. 실행해야지만 뭔가 누락되었다는 것을 알 수 있음...

- 컴파일중이 아니라 **실행중에** 애플리케이션이 사용하는 클래스 목록을 찾는 공식적인 방법이 없음 
  - 누락된 클래스가 있다면 실행 중에 그것을 사용하려 할 때 오류 발생
  - 따라서 사용중인 패키지 있는 모든 클래스를 같이 배포하는게 일반적이었음
  - 문제점
    - Java 버전이 증가함에 따라 Java 자체 제공 라이브러리의 크기가 커짐
    - 사용하지 않는 클래스까지 같이 배포할 경우 쓸데없이 용량이 커짐

## 기존 패키지 시스템의 한계 2

- 패키지 안에 있는 모든 public 클래스를 아무나 사용할 수 있음
- 때로는 그 중 일부만 외부에 노출하고 싶은데 그럴 수 없음

## 새로운 방식 : 모듈

기존 패키지 방식의 문제를 해결하기 위해 모듈 구조로!

![image-20211225095755252](https://raw.githubusercontent.com/yeonnex/image-server/main/img/image-20211225095755252.png)

(src 폴더가 초록박스 위에 있고,) 각각이 모듈화되었다.

즉, 패키지 위에 또 다른 개념(모듈)이 추가되었다고 볼 수 있다.

## 모듈

![image-20211225100203462](https://raw.githubusercontent.com/yeonnex/image-server/main/img/image-20211225100203462.png)

- Java9 부터 지원
- 패키지보다 상위개념
  - 패키지를 내포함
- 장점
  - 정말 필요한 패키지만 포함할 수 있음(경량화)
  - 프로그램 시작 시 누락된 모듈을 확인가능
  - 어떤 모듈이 사용하는 다른 모듈 목록을 확인 가능
  - 모듈 사용자에게 공개할 클래스를 특정할 수 있음
  - 현재 자바 SDK나 런타임 등의 배포는 모두 모듈로 이루어지고 있음
- 옛날 코드중에는 모듈 사용안하고 패키지로 그냥 하는 경우 있음
- 반드시 모듈로 할 필요는 없음

## 모듈의 이름

- 패키지와 마찬가지로 중복을 피해야 함
- 여러 단어로 이루어진 경우, 점(.)을 찍음
  -  단어별로 폴더롤 만들지 않음

## module-info.java

![image-20211225100739151](https://raw.githubusercontent.com/yeonnex/image-server/main/img/image-20211225100739151.png)

- 모듈간의 의존관계를 정의한 파일
- 컴파일 과정에서 .class 파일로 바뀜
- 모든 모듈에 반드시 존재해야 함
- 이 파일 안에 들어가는 내용
  - 1. 본 모듈 안에서 사용하는 외부 모듈 목록
    2. 본 모듈 사용자에게 공개할 패키지 목록

## module-info.java 예

![image-20211225100904061](https://raw.githubusercontent.com/yeonnex/image-server/main/img/image-20211225100904061.png)

![image-20211225101256911](https://raw.githubusercontent.com/yeonnex/image-server/main/img/image-20211225101256911.png)

`exports pocu.academy.core.math` 라는 말은, 본 모듈 사용자가 pocu.academy.core.math 라는 모듈을 사용할 수 있게 하겠다는 뜻이다. 만약 아무것도 노출하고 싶지 않다면 exports 를 생략하면된다.

`requires java.sql` 이라는 말은, 이 모듈에서 java.sql이라는 외부 모듈을 필요로 한다는, 즉 의존하고 있다는 말이다. 이렇게 하는 것의 장점이 뭐냐면, 이 모듈이 java.sql 을 사용하고 다른 것은 사용안한다는 것! 그러면 JVM이 이것을 실행할 때 java.sql 만 사용하는 것을 알고, 이것만 가져와서 로딩!!

- 모듈은 좀 더 효율적으로 패키지를 관리 및 배포하는 방법
- 실제로 프로그래밍하는 방법은 크게 바뀌지 않음

