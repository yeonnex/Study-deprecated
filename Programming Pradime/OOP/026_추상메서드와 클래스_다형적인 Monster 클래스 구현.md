## 오늘 할 모델링 : 맨날 싸우는 몬스터

- 몬스터를 만들어서 서로 공격하게 만들고 싶음
- 몬스터 종류는 현재 오우거, 유령, 트롤
- 공격하는 몬스터 종류에 따라 피해치 계산법이 다름
  - 본인과 상대방의 상태(예: 공격력, 방어력 등)를 피해치 계산에 사용
  - 그 상태들을 합치는 방법이 몬스터따라 다름
- 나중에 몬스터 종류를 더 추가할 수도 있음
  - 따라서 구조적 프로그래밍 방식(예: if 문 사용)보단 다형성이 적합!

## 몬스터의 상태와 동작

![image-20211222095755014](https://raw.githubusercontent.com/yeonnex/image-server/main/img/image-20211222095755014.png)

|                           Monster                            |
| :----------------------------------------------------------: |
|        -hp: int<br />-attack: int<br />-defense: int         |
| +Monster(int, int, int)<br />+getHp(): int<br />+getAttack():int<br />+getDefense(): int<br />+isAlive(): Boolean<br />+attack(Monster)<br />#inflictDamage(int) |

## 유일한 동작인 공격 : 어떻게 구현해야 할까?

> 때리는 몬스터 A , 맞는 몬스터 B

1. A에게 B를 공격하라 명령 : `monsterA.attack(monsterB);`
2. A는 B의 공격력(attack)과 방어력(defense)을 읽어옴
3. B로부터 읽어온 상태와 자신의 상태를 이용하여 피해량을 계산
4. B에게 피해량을 적용 : `monsterB.inflictDamage(damage);`

```java
public class Monster {
    ...
    public void attack(Monster target){
        
    }
    public void inflictDamage(int amount){
        this.hp = Math.max(0, this.hp - amount);
    }
}
```

## attack() 메서드가 비어있는 이유

```java
// Monster 클래스
public void attack(Monster monster){
    
}
```

- **각 종류의 몬스터가 다른 방법으로 공격하기 때문**
- 자식 클래스에서 해야할 일
  - 자식 클래스의 `attack()` 메서드 내부에서 알아서 피해량을 계산 후 적용
  - 즉, 자식 클래스의 `attack()` 메서드가 `inflictDamage()` 를 호출해 주어야 함

```java
// Ghost 클래스
public void attack(Monster target){
    // 여기서 피해량을 계산
    
    target.inflictDamage(피해량);
}

// Troll 클래스
public void attack(Monster target){
    // 여기서 피해량을 계산
    
    target.inflictDamage(피해량);
}
```

## inflictDamage() 메서드는 protected !

- public 이면 아무나 몬스터의 체력을 깎을 수 있음
- 즉 Program.java이런데서 갑자기 이 메서드를 쓸 수 있다는 것임

```java
Monster monster = new Troll(100, 10, 10);
monster.inflictDama
```

