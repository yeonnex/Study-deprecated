## 모든 것이 개체 속에 있는 불편함 1

#### 이런 단순한 계산도 개체를 만들어서 해야하나?

- 절대값 구하기
- 공백 문자 개수 구하기

## 정적 멤버함수 예

```java
//Math.java
public class Math{
    public static int abs(int n){
        return n<0 ? -n : n;
    }
    public static int min(int a, int b){
        return a < b ? a : b;
    }
    public static int max(int a, int b){
        return a > b ? a : b;
    }
}
```

```java
// 메인함수
int absValue = Math.abs(-2);
int minValue = Math.min(3,8);
```

- 멤버 함수 시그내쳐에 static 만 붙여주면 됨
- 이 멤버함수의 소유주는 인스턴스가 아니라 클래스
- 정적 멤버 함수를 호출할 때는, `<클래스명>.<함수명>`
- new를 이용해서 Math 개체를 만들지 않아도 됨!
- 정적 멤버 함수는 클래스 다이어그램으로 그릴 때 밑줄 그음

![image-20211204115048214](https://raw.githubusercontent.com/yeonnex/image-server/main/img/image-20211204115048214.png)

자바에서는 생성자를 만들지 않아도 자동으로 기본 생성자를 스스로 생성한다. 현재 Math 클래스에는 객체에 속할 필드나 메서드가 없고, 단지 클래스 소속인 정적 메서드만 존재하고 있다.

이 상황에서, 개체를 생성할 수 있긴 함.

```java
// 메인 함수
Math math = new Math();
int absValue = math.abs(-3);
int minValue = math.min(-4, 6);
```

## static 메서드와 Math 개체들

![image-20211204121327942](https://raw.githubusercontent.com/yeonnex/image-server/main/img/image-20211204121327942.png)

근데, static 은 전역처럼 쓰려고 만든건데, 굳이 객체를 만들 필요가 있나? new 해서 개체를 만들 때마다 메모리가 잡히는데 그냥 개체 생성을 못하게 막으면 안되나?

그렇다. 이런 경우는 개체생성을 못하게 막으면 좋다.

어떻게 하면 되지?

생성자를 `private` 으로 만들면 된다!

## Math 개체 생성 금지 예

```java
//Math.java
public class Math{
    private Math(){
        
    }
    public static int abs(int n){
        return n<0 ? -n : n;
    }
    public static int min(int a, int b){
        return a < b ? a : b;
    }
    public static int max(int a, int b){
        return a > b ? a : b;
    }
}
```

```java
// 메인 함수
int absValue = Math.abs(-3); // OK
Math math = new Math(); // 컴파일 에러
```

- 단 `static` 메서드는 `public` 이기 때문에 호출 가능

### 근데 참고로, private 생성자는 꼼수에 가깝다. 전문용어로 hack,,,

생각해보자. 나는 abs, min 같은 것들을 속에 아무것도 없는 전역 함수처럼 사용하고 싶다. 근데 개체지향 프로그래밍 언어에서는 클래스를 무조건 만들어야 하니,, 이건 `static` 클래스를 지원하는 언어에서는 필요없는 방법이다.

안타깝게도 Java 와 C++은 static 클래스를 지원하지 않아서 private 생성자를 써야만 한다... (C#에서는 제공)

## 모든 것이 개체 속에 있는 불편함 2

#### 개체 단위가 아니라 클래스 단위에서 뭔가를 하고 싶을 때는?

- 이 클래스에서 총 몇개의 개체가 찍혔나?

```java
public class ColaCan{
    private int remainingMl;
    private static int numCreated;
    public ColaCan(int initialMl){
        this.remainingMl = initialMl;
        ++numCreated;
    }
}
```

 콜라캔이 총 몇 개 만들었는지 확인하려면?

## 정적 멤버 변수에 접근하는 정적 메서드

|                         ColaCan                         |
| :-----------------------------------------------------: |
| - remainingInMl :int<br /> - <u>numCreated: int = 0</u> |
|         +ColaCan(int)<br /><u>+printStats()</u>         |



```java
package staticstudy;

public class ColaCan {
    private int remainingInMl;
    private static int numCreated = 0;
    public ColaCan(int initialInMl){
        this.remainingInMl = initialInMl;
        ++numCreated;
    }
    public static int printStats(){
        return numCreated;
    }
}
```

```java
package staticstudy;

public class Program {
    public static void main(String[] args) {
        ColaCan cola_1 = new ColaCan(200);
        ColaCan cola_2 = new ColaCan(100);
        System.out.println(ColaCan.printStats()); // 2
        
        cola_1.printStats(); // 역시 개체를 통해서도 정적 메서드에 접근 가능
    }
}
```

- 개체를 통해서도 정적 메서드에 접근가능하지만, 클래스를 통해 접근하는게 좀 더 보기 좋음!

## static 정리

1. `static` 멤버 변수 및 멤버 함수는 클래스에 속함 (딱 하나만 존재)
2. `static` 아닌 것은 개체에 속함 (따라서 개체 수만큼 존재)
3. 비정적 -> 정적 : 접근 가능
4. 정적 -> 비정적 : 접근 불가능 (당연)

자바에서 C의 전역변수/함수와 비슷한 걸 만들고 싶다면, `static`을 사용하자!

근데 `static`이 C의 전역변수/함수보다 좋은 점이 있다.

- 접근 범위를 제어할 수 있고

```java
public class ColaCan{
    private static int numCreated; // 클래스 내부에서만 접근 가능
    public static void printStats(){
        System.out.println(numCreated); // 클래스 내부 및 외부에서 접근 가능
    }
}
```

- 클래스 내부에 위치하기 때문에 이름 충돌이 적다

```java
public class ColaCan{
    private static int numCreated; 
    public static void printStats(){
        System.out.println(numCreated); 
    }
}

public class BeerCan{
    private static int numCreated; 
    public static void printStats(){
        System.out.println(numCreated); 
    }
}
```

```java
ColaCan.printStats();
BeerCan.printStats(); 
// 서로 충돌 날 일이 없음!
```

