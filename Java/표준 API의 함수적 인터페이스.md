## 자바 8부터 표준 API로 제공되는 함수적 인터페이스

- java.util.function 패키지에 있다
- **매개타입으로 사용되어 람다식을 매개값으로 대입할 수 있도록 해준다**

### 종류

- Consumer 함수적 인터페이스 류 :
  - 매개값만 있고 리턴값이 없는 추상메서드를 가지고 있다
- Supplier 함수적 인터페이스 류 :
  - 매개값은 없고 리턴값만 있는 추상메서드를 가지고 있다
- Function 함수적 인터페이스 류 :
  - 매개값과 리턴값이 모두 있는 추상메서드를 가지고 있다
  - 주로 매개값을 리턴값으로 매핑(타입변환)할 경우에 사용
- Operator 함수적 인터페이스 류 :
  - 매개값과 리턴값이 모두 있는 추상메서드를 가지고 있다
  - 주로 매개값을 연산하고 그 결과를 리턴할 경우에 사용
- Predicate 함수적 인터페이스 류 :
  - 매개값을 조사해서 true 또는 false를 리턴할 때 사용

### Consumer 함수적 인터페이스

Consumer 함수적 인터페이스의 특징은 리턴값이 없는 accept() 메소드를 가지고 있다. accept() 메소드는 단지 매개값을 소비하는 역할만을 한다. 즉 리턴값이 없음!

![image-20220125173131667](https://raw.githubusercontent.com/yeonnex/image-server/main/img/image-20220125173131667.png)

매개변수의 타입과 수에 따라서 아래와 같은 Consumer 들이 있다.

| 인터페이스명     | 추상 메서드                 | 설명                       |
| ---------------- | --------------------------- | -------------------------- |
| Consumer<T>      | void accept(T t)            | 객체 T를 받아 소비         |
| BiConsumer<T, U> | void accept(T t, U u)       | 객체 T와 U를 받아 소비     |
| DoubleConsumer   | void accept(double value)   | double 값을 받아 소비      |
| ObjIntConsumer   | void accept(T t, int value) | 객체 T와 int값을 받아 소비 |

그 외 등등..

```java
Consumer<String> consumer = t -> {... t를 소비하는 실행문;}

BiConsumer<String, String> comsumer = (t,u) -> {t와 u를 소비하는 실행문;}
```

```java
Consumer<String> consumer = t -> System.out.println(t + "8");
consumer.accept("java ");

// java 8 출력됨
```

```java
BiConsumer<String, int> biconsumer = (t, u) -> System.out.println("안녕!" + t + u);
biconsumer.accept("java", 8);
```

