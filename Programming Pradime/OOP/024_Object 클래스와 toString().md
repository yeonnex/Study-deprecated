- Java 의 클래스는 모두 Object 로부터 상속을 받음
- 따라서 Object 에 있는 메서드들은 어떤 클래스에서도 오버라이딩 가능

## toString() 메서드

> public String toString()

- 사람이 읽기 편하게 해당 개체를 문자열로 표현

- Object 클래스 안의 기본 구현

  > getClass().getName() + '@' + Integer.toHexString(hashCode())

## toString() 메서드 오버라이딩 예

- Javav 공식 문서는 모든 클래스에서 이 메서드를 오버라이딩하라 권장
  - 근데 사실 잘 안함

```java
// Person 클래스
public String toString(){
    return String.format("Person: " + this.firstName, this.lastName);
}
```

```java
Person person = new Person("seoyeon", "Jang");
System.out.println(person.toString());

// Person : seoyeon Ja
```

