instanceof 연산자와 비슷한 역할을 하는 메서드가 있음

## getClass()

```
<변수명>.getClass();
```

```java
FullTimeTeacher teacher = new FullTimeTeacher("Lulu", "Choi", Department.MAGIC);
Class c = teacher.getClass();
```

- 실행 중에 개체의 클래스 정보를 얻어올 수 있음
- 반환된 개체(Class)에는 여러 유용한 메서드가 들어있음
  - 여기서는 딱 하나만 볼 것
  - 그 밖의 함수는 필요하면 천천히 찾아볼 것

## getClass().getName()

```java
System.out.println(teacher.getClass().getName());
```

- 클래스명을 반환하는 메서드
- 이때 클래스명은 패키지 경로까지 포함

## 언제 사용하는가?

- 주로 클래스 이름을 찾을 떄
- 클래스 안에 있는 메서드나 멤버 변수들을 볼 수 있음
- `getClass().getName()` 은 정말 많이 사용
  - 예 : 로그 메시지를 출력할 때

## 좋아보이는 RTTI 그러나...

- 매니지드 언어들은 보통 RTTI를 지원
- 단, 그만큼 실행중에 뭔가 더 해야 함
- 성능 또는 메모리가 중요한 경우에는 별로인 기능..
- C/C++ 등의 언어에서는 RTTI 지원이 없거나 사용을 안 함

근데, teacher.getClass() 를 아주 자연스럽게 썼다만, getClass() 는 분명 내가 구현하지 않았다. 내 클래스 안에 직접ㄱ ㅜ현안했는데 도대체 어디서 온 것임?

이렇게 내 클래스에 없어도 메서드를 사용할 수 있는 경우가 있었는데, 바로 **상속**!

## Object 클래스

- Java 의 **모든 클래스**는 Object 라는 클래스를 상속
- 즉 앞에서 Person[] 에 넣었던 개체를 Object[] 에도 넣을 수 있음

```java
Object[] people = new Person[2];
people[0] = new Student("Leon", "Kim");
people[1] = new PartTimeTeacher("Sally", "Choi", Department.COMPUTER_SCIENCE, 10);
```

 

- 모든 클래스는 Object 를 상속받으니 그 메서드들도 같이 딸려옴
- Object 에는 유용한 메서드들이 좀 있음
- RTTI 도 그 중 하나 (getClass() 같은)