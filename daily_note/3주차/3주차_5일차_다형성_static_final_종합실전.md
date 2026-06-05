# 3주차 5일차 - 다형성, static, final, 접근제어, Java 종합 실전

## 오늘의 목표

오늘은 Java 주간 마무리다. 실기에서 가장 자주 헷갈리는 “참조 변수 타입과 실제 객체 타입이 다를 때 어떤 메서드가 실행되는가?”를 집중적으로 훈련한다. 또한 `static`, `final`, 접근제어자를 정리하고 종합 문제를 푼다.

- 다형성에서 오버라이딩 메서드는 실제 객체 기준으로 실행된다는 것을 설명할 수 있다.
- 필드는 참조 변수 타입 기준으로 접근된다는 점을 구분할 수 있다.
- `static` 필드와 인스턴스 필드의 차이를 추적할 수 있다.
- `final`과 접근제어자의 시험 포인트를 정리할 수 있다.
- Java 실기형 종합 코드를 손으로 추적할 수 있다.

## 3시간 수업 구성

| 시간 | 내용 |
|---|---|
| 0:00 ~ 0:30 | 다형성 기본 |
| 0:30 ~ 1:00 | 오버라이딩 메서드와 필드 접근 차이 |
| 1:00 ~ 1:20 | 형변환과 instanceof |
| 1:20 ~ 1:30 | 쉬는 시간 |
| 1:30 ~ 2:00 | static, final, 접근제어 |
| 2:00 ~ 2:40 | Java 종합 실기형 문제 |
| 2:40 ~ 3:00 | 주간 마무리 체크 |

---

## 1. 다형성 기본

다형성은 부모 타입 변수로 자식 객체를 가리킬 수 있는 성질이다.

```java
class Animal {
    void sound() {
        System.out.println("Animal");
    }
}

class Dog extends Animal {
    void sound() {
        System.out.println("Dog");
    }
}

class Main {
    public static void main(String[] args) {
        Animal a = new Dog();
        a.sound();
    }
}
```

출력:

```text
Dog
```

`a`의 타입은 `Animal`이지만 실제 객체는 `Dog`다. 오버라이딩된 메서드는 실제 객체 기준으로 실행된다.

```text
Animal a = new Dog();
   |          |
   |          +-- 실제 객체 타입
   +------------- 참조 변수 타입

오버라이딩 메서드 호출: 실제 객체 Dog 기준
```

---

## 2. 메서드는 실제 객체, 필드는 참조 타입

이 부분이 실기에서 매우 중요하다.

```java
class Parent {
    int x = 10;

    void print() {
        System.out.println("Parent");
    }
}

class Child extends Parent {
    int x = 20;

    void print() {
        System.out.println("Child");
    }
}

class Main {
    public static void main(String[] args) {
        Parent p = new Child();

        System.out.println(p.x);
        p.print();
    }
}
```

출력:

```text
10
Child
```

왜 이렇게 나올까?

| 코드 | 기준 | 결과 |
|---|---|---|
| `p.x` | 참조 변수 타입 `Parent` | `Parent`의 `x`, 즉 10 |
| `p.print()` | 실제 객체 `Child` | `Child`의 `print()` |

정리:

```text
필드 접근: 참조 변수 타입 기준
오버라이딩 메서드 호출: 실제 객체 타입 기준
```

---

## 3. 다형성 그림

```text
Parent p = new Child();

p ----> Child 객체
       +------------------+
       | Parent 부분       |
       | x = 10           |
       | print() 원본      |
       +------------------+
       | Child 부분        |
       | x = 20           |
       | print() 재정의    |
       +------------------+

p.x       -> Parent 타입으로 보므로 Parent 부분 x
p.print() -> 실제 객체 Child가 재정의한 print()
```

Java 참조는 C 포인터처럼 주소를 직접 계산하지 못한다. 하지만 `p`가 실제 객체를 가리킨다는 구조는 여전히 참조 기반이다. 그래서 “무엇을 가리키는가?”를 그릴 수 있어야 한다.

---

## 4. 형변환

부모 타입 변수로는 자식만 가진 메서드를 바로 호출할 수 없다.

```java
class Parent {
    void a() {
        System.out.println("a");
    }
}

class Child extends Parent {
    void b() {
        System.out.println("b");
    }
}

class Main {
    public static void main(String[] args) {
        Parent p = new Child();
        p.a();
        // p.b(); // 컴파일 오류

        Child c = (Child) p;
        c.b();
    }
}
```

출력:

```text
a
b
```

`p`의 실제 객체가 `Child`이므로 `Child`로 형변환할 수 있다.

### 잘못된 형변환

```java
Parent p = new Parent();
Child c = (Child) p; // 실행 중 오류
```

실제 객체가 `Parent`인데 `Child`인 척할 수는 없다.

---

## 5. instanceof

`instanceof`는 실제 객체가 특정 타입인지 검사한다.

```java
if (p instanceof Child) {
    Child c = (Child) p;
    c.b();
}
```

실기에서는 복잡한 문법보다 다음 뜻만 기억하면 된다.

```text
p instanceof Child
=> p가 가리키는 실제 객체를 Child로 볼 수 있는가?
```

---

## 6. static

`static`은 객체마다 따로 있는 것이 아니라 클래스가 공유한다.

```java
class Counter {
    static int total = 0;
    int count = 0;

    Counter() {
        total++;
        count++;
    }
}

class Main {
    public static void main(String[] args) {
        Counter a = new Counter();
        Counter b = new Counter();
        Counter c = new Counter();

        System.out.println(a.total);
        System.out.println(a.count);
        System.out.println(b.count);
    }
}
```

출력:

```text
3
1
1
```

그림:

```text
Counter 클래스 공유 공간
+-------------+
| total = 3   |
+-------------+

a 객체: count = 1
b 객체: count = 1
c 객체: count = 1
```

`total`은 모든 객체가 공유한다. `count`는 객체마다 따로 있다.

권장 표기:

```java
System.out.println(Counter.total);
```

`static` 필드는 클래스 이름으로 접근하는 것이 명확하다.

---

## 7. static 메서드

```java
class MathUtil {
    static int doubleValue(int n) {
        return n * 2;
    }
}

class Main {
    public static void main(String[] args) {
        System.out.println(MathUtil.doubleValue(5));
    }
}
```

출력:

```text
10
```

`static` 메서드는 객체를 만들지 않고 클래스 이름으로 호출할 수 있다.

주의:

```java
class Test {
    int x = 10;

    static void print() {
        // System.out.println(x); // 오류
    }
}
```

`static` 메서드는 특정 객체 없이 실행되므로 객체 필드 `x`를 바로 사용할 수 없다.

---

## 8. final

`final`은 바꿀 수 없다는 뜻이다.

| 위치 | 의미 |
|---|---|
| `final int x = 10;` | 변수 값을 다시 대입할 수 없음 |
| `final void f()` | 자식이 오버라이딩할 수 없음 |
| `final class A` | 상속할 수 없음 |

시험에서는 주로 상수처럼 쓰이는 변수와 오버라이딩 금지 의미를 묻는다.

```java
final int MAX = 100;
// MAX = 200; // 오류
```

참조형 `final`은 더 주의해야 한다.

```java
class Box {
    int value;
}

class Main {
    public static void main(String[] args) {
        final Box b = new Box();
        b.value = 10;
        b.value = 20;
        // b = new Box(); // 오류
    }
}
```

`final Box b`는 `b`가 다른 객체를 가리키게 할 수 없다는 뜻이다. 객체 내부 필드 변경까지 막는 것은 아니다.

---

## 9. 접근제어자

| 접근제어자 | 같은 클래스 | 같은 패키지 | 자식 클래스 | 외부 |
|--       -|-         --|        ---|-        --|   ---|
| `public` | 가능        | 가능      | 가능       | 가능 |
| `protected` | 가능     | 가능      | 가능       | 제한 |
| `private` | 가능       | 불가      | 불가       | 불가 |

실기 코드 추적 문제에서는 `private` 필드가 직접 접근되지 않고 메서드를 통해 접근되는 형태가 자주 나온다.

```java
class Account {
    private int balance;

    void deposit(int money) {
        balance += money;
    }

    int getBalance() {
        return balance;
    }
}
```

---

## 10. 종합 실기형 예제 1

다음 코드의 출력 결과를 쓰시오.

```java
class A {
    int x = 1;

    void f() {
        System.out.println("A");
    }
}

class B extends A {
    int x = 2;

    void f() {
        System.out.println("B");
    }
}

class Main {
    public static void main(String[] args) {
        A obj = new B();
        System.out.println(obj.x);
        obj.f();
    }
}
```

정답:

```text
1
B
```

필드 `x`는 참조 타입 `A` 기준, 메서드 `f()`는 실제 객체 `B` 기준이다.

---

## 11. 종합 실기형 예제 2

다음 코드의 출력 결과를 쓰시오.

```java
class Count {
    static int total = 0;
    int num = 0;

    Count() {
        total++;
        num++;
    }

    void add() {
        total++;
        num++;
    }
}

class Main {
    public static void main(String[] args) {
        Count a = new Count();
        Count b = new Count();

        a.add();
        b.add();
        b.add();

        System.out.println(Count.total);
        System.out.println(a.num);
        System.out.println(b.num);
    }
}
```

상태표:

| 실행 | total | a.num | b.num |
|---|---:|---:|---:|
| `new Count()` a | 1 | 1 | - |
| `new Count()` b | 2 | 1 | 1 |
| `a.add()` | 3 | 2 | 1 |
| `b.add()` | 4 | 2 | 2 |
| `b.add()` | 5 | 2 | 3 |

정답:

```text
5
2
3
```

---

## 12. 종합 실기형 예제 3

다음 코드의 출력 결과를 쓰시오.

```java
class Parent {
    Parent() {
        System.out.println("P");
    }

    void print() {
        System.out.println("Parent");
    }
}

class Child extends Parent {
    Child() {
        System.out.println("C");
    }

    void print() {
        System.out.println("Child");
    }

    void call() {
        print();
        super.print();
    }
}

class Main {
    public static void main(String[] args) {
        Child c = new Child();
        c.call();
    }
}
```

정답:

```text
P
C
Child
Parent
```

생성자는 부모 먼저, 메서드 호출은 `call()` 안에서 자식 `print()` 후 부모 `print()` 순서다.

---

## 13. 오늘의 혼자 연습 문제

### 문제 1

다음 코드의 출력 결과를 쓰시오.

```java
class P {
    int n = 10;

    void show() {
        System.out.println("P");
    }
}

class C extends P {
    int n = 20;

    void show() {
        System.out.println("C");
    }
}

class Main {
    public static void main(String[] args) {
        P p = new C();
        System.out.println(p.n);
        p.show();
    }
}
```

### 문제 2

다음 코드의 출력 결과를 쓰시오.

```java
class A {
    static int s = 0;
    int n = 0;

    A() {
        s++;
        n++;
    }
}

class Main {
    public static void main(String[] args) {
        A a1 = new A();
        A a2 = new A();

        a1.n++;
        A.s++;

        System.out.println(A.s);
        System.out.println(a1.n);
        System.out.println(a2.n);
    }
}
```

### 문제 3

다음 코드의 출력 결과를 쓰시오.

```java
class Box {
    int value;
}

class Main {
    public static void main(String[] args) {
        final Box b = new Box();
        b.value = 3;
        b.value += 7;

        System.out.println(b.value);
    }
}
```

### 문제 4

다음 코드의 출력 결과를 쓰시오.

```java
class A {
    void f() {
        System.out.println("A");
    }
}

class B extends A {
    void f() {
        System.out.println("B");
    }

    void g() {
        System.out.println("G");
    }
}

class Main {
    public static void main(String[] args) {
        A a = new B();
        a.f();

        B b = (B) a;
        b.g();
    }
}
```

### 문제 5

다음 조건을 만족하는 코드를 작성하시오.

- `Employee` 클래스는 `name`, `pay` 필드를 가진다.
- 생성자로 두 필드를 초기화한다.
- `getBonus()` 메서드는 `pay / 10`을 반환한다.
- `Manager` 클래스는 `Employee`를 상속받는다.
- `Manager`의 `getBonus()`는 `pay / 5`를 반환하도록 오버라이딩한다.
- `Employee e = new Manager("Kim", 1000);`으로 객체를 만들고 보너스를 출력한다.

---

## 14. 정답과 해설

### 문제 1 정답

```text
10
C
```

필드는 참조 타입 `P`, 메서드는 실제 객체 `C` 기준이다.

### 문제 2 정답

```text
3
2
1
```

객체 2개 생성으로 `s = 2`, 이후 `A.s++`로 `3`이다. `a1.n`은 생성자에서 1, 이후 한 번 증가해서 2다. `a2.n`은 1이다.

### 문제 3 정답

```text
10
```

`final Box b`는 b가 다른 객체를 가리키는 것을 막는다. 객체 내부 필드 `value`는 변경 가능하다.

### 문제 4 정답

```text
B
G
```

`a.f()`는 실제 객체 `B`의 오버라이딩 메서드를 실행한다. 실제 객체가 `B`이므로 `(B) a` 형변환 후 `g()` 호출이 가능하다.

### 문제 5 예시 정답

```java
class Employee {
    String name;
    int pay;

    Employee(String name, int pay) {
        this.name = name;
        this.pay = pay;
    }

    int getBonus() {
        return pay / 10;
    }
}

class Manager extends Employee {
    Manager(String name, int pay) {
        super(name, pay);
    }

    int getBonus() {
        return pay / 5;
    }
}

class Main {
    public static void main(String[] args) {
        Employee e = new Manager("Kim", 1000);
        System.out.println(e.getBonus());
    }
}
```

출력:

```text
200
```

`e`의 참조 타입은 `Employee`지만 실제 객체는 `Manager`이므로 오버라이딩된 `Manager.getBonus()`가 실행된다.

---

## 15. 3주차 Java 최종 요약

### 1일차 핵심

- `main`에서 실행이 시작된다.
- 변수는 오른쪽 계산 후 왼쪽 저장이다.
- 배열 인덱스는 0부터 시작한다.
- 반복문은 상태표로 추적한다.

### 2일차 핵심

- 클래스는 설계도, 객체는 실제 데이터다.
- `new`는 새 객체를 만든다.
- 기본형은 값 복사, 객체는 참조 복사다.
- Java에는 C식 포인터 문법은 없지만 참조 흐름은 반드시 추적해야 한다.

### 3일차 핵심

- 생성자는 객체 생성 시 자동 실행된다.
- `this`는 현재 객체다.
- 객체 배열의 칸에는 객체 참조가 들어간다.
- `null`에 접근하면 오류가 난다.

### 4일차 핵심

- 자식 객체 생성 시 부모 생성자가 먼저 실행된다.
- `super`는 부모를 가리킨다.
- 오버라이딩은 부모 메서드를 자식이 재정의하는 것이다.

### 5일차 핵심

- 다형성에서 오버라이딩 메서드는 실제 객체 기준이다.
- 필드는 참조 변수 타입 기준이다.
- `static`은 클래스 공유, 인스턴스 필드는 객체별 보관이다.
- `final` 참조 변수는 다른 객체로 바꿀 수 없지만 객체 내부 필드 변경은 가능하다.

---

## 최종 실전 훈련 방법

Java 실기 문제를 풀 때는 다음 순서로 접근한다.

```text
1. new가 몇 번 나오는지 표시한다.
2. 참조 변수가 어떤 객체를 가리키는지 화살표로 그린다.
3. 생성자 실행 순서를 위에서 아래로 적는다.
4. static 값과 객체별 필드 값을 분리해서 표로 쓴다.
5. 메서드 호출이 오버라이딩인지 확인한다.
6. 필드 접근이면 참조 타입 기준인지 확인한다.
7. 출력문 순서대로 결과를 적는다.
```

이 7단계를 습관화하면 길어 보이는 Java 문제도 대부분 손으로 풀 수 있다.
