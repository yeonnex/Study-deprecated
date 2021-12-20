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

상속으로 할 수 있는거 컴포지션으로도 가능, 컴포지션으로 할 수 있는 거 상속으로도 가능

- 둘 다 **재사용성**을 위한 방법
- 상속으로 해결할 수 있는 많은 문제를 컴포지션으로도 가능
  - 그 반대도 가능
  - 순전히 기술적인 관점
- 역사적으로 사람들의 선호는 왔다 갔다
  - 초창기에는 상속을 과도하게 선호
  - 이후 상속의 문제점들이 보이기 시작
  - 그후 무조건 컴포지션으로 만들어야 한다는 조언들이 나왔으나 상속이 더 나을 때도 있음
  - OO에서 큰 결정사항 중 하나 : 상속 vs 컴포지션 중 하나를 고르는 것
    - 상속으로 클래스를 만들지, 컴포지션 관계를 취할지...

## 상속 vs 컴포지션 (2)

- 일단 이 간단한 가이드 라인을 따르자
  - *실생활에서* 개체들끼리간의 관계를 기준으로 선택할 것
    - has-a 관계 : 컴포지션 - "~로 이루어져있다" 처럼 집합관계가 말이 된다면
    - is-a 관계 : 상속 - "~는 ~ 이다" 라는게 말이 된다면

- 물론 훌륭한 프로그래머들은 필요에 따라 이 규칙을 어김
- 나중에 상속 vs 컴포지션에 대해서는 좀 더 배울 것!

<hr>

Student는 Person을 상속받는다. 학생 is 사람 이기 때문. 그렇기에 아래와 같은 코드가 가능하다.

```java
Student student = new Student("Seoyeon", "Jang");
Person person = student; // 일단 컴파일은 됨 😊 (실행중은 모르겠고)
```

그럼 시간 강사는 어떨까?

```java
PartTimeTeacher partTime = new PartTimeTeacher("Sandy", "Kim", Department.COMPUTER_SCIENCE, 10);
Teacher teacher = partTime;
Person person = parTime; // 컴파일 됨 😊 Person은 PartTimeTeacher 의 조부모
```

그럼 Person 배열에 학생과 시간 강사를 모두 넣는 건?

```java
Person[] people = new Person[2];

people[0] = new Student("Seoyeon", "Jang");
people[1] = new PartTimeTeacher("Sandy", "Kim", Department.COMPUTER_SCIENCE, 10); // 역시 컴파일 됨 😊
```

이 모든 게 가능한 이유는?

두 클래스 관계가 is-a 이기 때문

학생은 여전히 사람이며, 
시간강사는 여전히 선생, 
시간강사는 여전히 사람.

그 반대는 불가

사람은 학생?
선생은 시간강사?
사람은 시간강사?

말이 안됨

```java
Person person = new Person("Seoyeon", "Jang");
Student student = person // 컴파일 에러
```

그럼 이 코드는 어떨까? **(실체는 학생)**

```java
Student student = new Student("Seoyeon", "Jang");
Person person = student;
Student actuallyStudent = person; // ?? (부모를 자식에게 대입)
```

컴파일이 되지 않는다. 실체는 Student이긴 하지만, 타입은 Person이기 때문이다.

바로 이러한 경우 때문이다.

```java
public static Student convertToStudent(Person person){
    Student student = person;
    return student;
}
```

`convertToStudent` 라는 static 메서드는 Person 타입을 인자로 받아서 얘를 Student 로 타입변환한 다음에 그것을 리턴한다. 실체가 학생이라면 허용해주고, 실체가 학생이 아니라면 허용 안해주고 이거를 컴파일때는 명확히 알 수가 없다. 실행중이라면 가능하지만... 컴파일때는 이 함수를 누가 호출하는지 어떻게 알아! 이런걸 허용하지 않기 위해 모든걸 통합적으로 한가지 규칙을 만드려고 허용하지 않음. 즉 아래와 같은 꼴이 나게 되기 때문

부모를 자식에게 대입할 수 있게 되면 ...

```java
// 다른 함수 어딘가
convertToStudent(student); // Student student
convertToStudent(teacher); // Teacher teacher
convertToStudent(partTime); // 
```





