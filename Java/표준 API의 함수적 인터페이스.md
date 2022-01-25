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

### Supplier 함수적 인터페이스

Supplier 함수적 인터페이스의 특징은 매개변수가 없고 리턴값이 있는 getXXX() 메소드를 가지고 있다. 이들 메소드는 실행 후 호출한 곳으로 데이터를 리턴(공급)하는 역할을 한다.

![image-20220125175614190](https://raw.githubusercontent.com/yeonnex/image-server/main/img/image-20220125175614190.png)

리턴 타입에 따라서 아래와 같은 Supplier 함수적 인터페이스들이 있다.

| 인터페이스 명   | 추상 메소드            | 설명             |
| --------------- | ---------------------- | ---------------- |
| Supplier<T>     | T get()                | 객체를 리턴      |
| BooleanSupplier | boolean getAsBoolean() | boolean값을 리턴 |
| DoubleSupplier  | double getAsDouble()   | double값을 리턴  |
| IntSupplier     | int getAsInt()         | int 값을 리턴    |

등..

```java
IntSupplier intSupplier = () -> {
    int num = (int) (Math.random()*6) + 1;
    return num;
}

int num = intSupplier.getAsInt();
System.out.println("눈의 수: " + num);
```

### Function 함수적 인터페이스

Function 함수적 인터페이스의 특징은 매개변수와 리턴값이 있는 applyXXX() 메소드를 가지고 있다. 이들 메소드는 매개값을 리턴값으로 매핑(타입변환)하는 역할을 한다.

![image-20220125180740007](https://raw.githubusercontent.com/yeonnex/image-server/main/img/image-20220125180740007.png)

| 인터페이스명       | 추상 메소드             | 설명                       |
| ------------------ | ----------------------- | -------------------------- |
| Function <T, R>    | R apply(T t)            | 객체 T를 객체 R로 매핑     |
| BiFunction <T,U,R> | R apply(T t, U u)       | 객체 T와 U를 객체 R로 매핑 |
| ToIntFuntion<T>    | int applyAsInt(T value) | 객체 T를 int로 매핑        |

그외 등등...

- 연습

  ```java
  // Function <T, R>
  Funciton<Student, String> function = t -> { return t.getName(); }
  // <Student, String> 이므로 매개값 t 는 Student 타입이고 리턴값은 String 타입이다.
  // Student 객체를 String으로 매핑한 예제이다
  ```

