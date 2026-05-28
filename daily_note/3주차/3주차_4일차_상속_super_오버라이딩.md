# 3주차 4일차 - 상속, super, 오버라이딩

## 오늘의 목표

오늘은 Java 실기 문제의 핵심인 상속과 오버라이딩을 다룬다. 시험에서는 “어떤 메서드가 호출되는가?”를 묻는 문제가 많다.

- 부모 클래스와 자식 클래스의 관계를 설명할 수 있다.
- 생성자 실행 순서에서 부모가 먼저 실행된다는 것을 추적할 수 있다.
- `super`가 부모를 가리킨다는 것을 이해한다.
- 오버라이딩된 메서드 호출 결과를 예측할 수 있다.

## 3시간 수업 구성

| 시간 | 내용 |
|---|---|
| 0:00 ~ 0:25 | 상속 기본 |
| 0:25 ~ 0:55 | 부모 필드와 자식 필드 |
| 0:55 ~ 1:20 | 생성자 실행 순서와 super |
| 1:20 ~ 1:30 | 쉬는 시간 |
| 1:30 ~ 2:10 | 메서드 오버라이딩 |
| 2:10 ~ 2:40 | 실기형 상속 추적 |
| 2:40 ~ 3:00 | 연습 문제 풀이 |

---

## 1. 상속 기본

상속은 기존 클래스의 기능을 물려받아 새 클래스를 만드는 것이다.

```java
class Animal {
    String name;

    void sound() {
        System.out.println("sound");
    }
}

class Dog extends Animal {
    void run() {
        System.out.println("run");
    }
}

class Main {
    public static void main(String[] args) {
        Dog d = new Dog();
        d.name = "Happy";
        d.sound();
        d.run();
    }
}
```

출력:

```text
sound
run
```

`Dog`는 `Animal`의 `name` 필드와 `sound()` 메서드를 물려받았다.

```text
Animal
  |
  +-- Dog
```

---

## 2. is-a 관계

상속은 “자식은 부모의 한 종류다”가 자연스러울 때 사용한다.

```text
Dog is an Animal -> 자연스러움
Car is an Engine -> 어색함
```

시험에서는 설계 철학보다 코드 실행 결과가 중요하지만, 관계를 이해하면 코드가 덜 낯설어진다.

---

## 3. 부모 필드와 자식 필드

```java
class Parent {
    int a = 10;
}

class Child extends Parent {
    int b = 20;
}

class Main {
    public static void main(String[] args) {
        Child c = new Child();
        System.out.println(c.a);
        System.out.println(c.b);
    }
}
```

출력:

```text
10
20
```

그림:

```text
Child 객체
+----------------------+
| Parent 부분           |
| a = 10               |
+----------------------+
| Child 부분            |
| b = 20               |
+----------------------+
```

자식 객체 안에는 부모로부터 물려받은 부분이 함께 들어 있다고 생각하면 된다.

---

## 4. 생성자 실행 순서

자식 객체를 만들면 부모 생성자가 먼저 실행되고, 그 다음 자식 생성자가 실행된다.

```java
class Parent {
    Parent() {
        System.out.println("Parent");
    }
}

class Child extends Parent {
    Child() {
        System.out.println("Child");
    }
}

class Main {
    public static void main(String[] args) {
        Child c = new Child();
    }
}
```

출력:

```text
Parent
Child
```

흐름:

```mermaid
flowchart TD
    A[new Child()] --> B[Child 객체 공간 생성]
    B --> C[Parent 생성자 실행]
    C --> D[Child 생성자 실행]
    D --> E[c가 객체 참조]
```

자식 생성자 첫 줄에는 부모 생성자를 호출하는 `super()`가 숨어 있다고 보면 된다.

---

## 5. super로 부모 생성자 호출

부모 생성자에 매개변수가 있으면 자식 생성자에서 `super(...)`로 명시적으로 호출해야 한다.

```java
class Parent {
    int a;

    Parent(int a) {
        this.a = a;
    }
}

class Child extends Parent {
    int b;

    Child(int a, int b) {
        super(a);
        this.b = b;
    }
}

class Main {
    public static void main(String[] args) {
        Child c = new Child(3, 5);
        System.out.println(c.a);
        System.out.println(c.b);
    }
}
```

출력:

```text
3
5
```

`super(a)`는 부모 생성자 `Parent(int a)`를 호출한다.

주의: `super(...)`는 생성자의 첫 줄에 있어야 한다.

---

## 6. super로 부모 필드와 메서드 접근

```java
class Parent {
    int value = 10;

    void print() {
        System.out.println("Parent");
    }
}

class Child extends Parent {
    int value = 20;

    void print() {
        System.out.println("Child");
    }

    void test() {
        System.out.println(value);
        System.out.println(super.value);
        print();
        super.print();
    }
}

class Main {
    public static void main(String[] args) {
        Child c = new Child();
        c.test();
    }
}
```

출력:

```text
20
10
Child
Parent
```

| 표현 | 의미 |
|---|---|
| `value` | 현재 클래스의 필드 우선 |
| `super.value` | 부모 클래스의 필드 |
| `print()` | 현재 클래스의 메서드 |
| `super.print()` | 부모 클래스의 메서드 |

---

## 7. 오버라이딩

오버라이딩은 부모에게 물려받은 메서드를 자식이 다시 정의하는 것이다.

```java
class Animal {
    void sound() {
        System.out.println("Animal");
    }
}

class Cat extends Animal {
    void sound() {
        System.out.println("Cat");
    }
}

class Main {
    public static void main(String[] args) {
        Cat c = new Cat();
        c.sound();
    }
}
```

출력:

```text
Cat
```

자식이 같은 이름과 같은 매개변수 형태로 메서드를 다시 만들면 자식 메서드가 우선 실행된다.

---

## 8. 오버로딩과 오버라이딩 비교

| 구분 | 오버로딩 | 오버라이딩 |
|---|---|---|
| 뜻 | 같은 이름, 다른 매개변수 | 부모 메서드를 자식이 재정의 |
| 클래스 관계 | 같은 클래스에서도 가능 | 상속 관계 필요 |
| 매개변수 | 달라야 함 | 같아야 함 |
| 시험 포인트 | 어떤 메서드가 선택되는가 | 실제 객체 기준으로 호출 |

예:

```java
void print(int n) { }
void print(String s) { } // 오버로딩
```

```java
class Parent {
    void print() { }
}
class Child extends Parent {
    void print() { } // 오버라이딩
}
```

---

## 9. 실전 실기형 예제 1

다음 코드의 출력 결과를 쓰시오.

```java
class A {
    A() {
        System.out.println("A");
    }
}

class B extends A {
    B() {
        System.out.println("B");
    }
}

class Main {
    public static void main(String[] args) {
        B b = new B();
    }
}
```

정답:

```text
A
B
```

자식 객체 생성 시 부모 생성자가 먼저 실행된다.

---

## 10. 실전 실기형 예제 2

다음 코드의 출력 결과를 쓰시오.

```java
class A {
    int x = 1;

    void print() {
        System.out.println(x);
    }
}

class B extends A {
    int x = 2;

    void print() {
        System.out.println(x);
        System.out.println(super.x);
    }
}

class Main {
    public static void main(String[] args) {
        B b = new B();
        b.print();
    }
}
```

정답:

```text
2
1
```

`x`는 자식 필드, `super.x`는 부모 필드다.

---

## 11. 실전 실기형 예제 3

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
        f();
        super.f();
    }
}

class Main {
    public static void main(String[] args) {
        B b = new B();
        b.g();
    }
}
```

정답:

```text
B
A
```

`f()`는 오버라이딩된 자식 메서드, `super.f()`는 부모 메서드다.

---

## 12. 오늘의 혼자 연습 문제

### 문제 1

다음 코드의 출력 결과를 쓰시오.

```java
class P {
    P() {
        System.out.println("P");
    }
}

class C extends P {
    C() {
        System.out.println("C");
    }
}

class Main {
    public static void main(String[] args) {
        C c = new C();
    }
}
```

### 문제 2

다음 코드의 출력 결과를 쓰시오.

```java
class P {
    int n = 10;
}

class C extends P {
    int n = 20;

    void show() {
        System.out.println(n);
        System.out.println(super.n);
    }
}

class Main {
    public static void main(String[] args) {
        C c = new C();
        c.show();
    }
}
```

### 문제 3

다음 코드의 출력 결과를 쓰시오.

```java
class P {
    void print() {
        System.out.println("P");
    }
}

class C extends P {
    void print() {
        System.out.println("C");
    }
}

class Main {
    public static void main(String[] args) {
        C c = new C();
        c.print();
    }
}
```

### 문제 4

다음 코드의 출력 결과를 쓰시오.

```java
class P {
    P(int n) {
        System.out.println(n);
    }
}

class C extends P {
    C() {
        super(7);
        System.out.println(3);
    }
}

class Main {
    public static void main(String[] args) {
        C c = new C();
    }
}
```

### 문제 5

`Vehicle` 클래스를 만들고 `move()` 메서드가 `"move"`를 출력하게 하시오. `Car` 클래스가 `Vehicle`을 상속받아 `move()`를 `"drive"`로 오버라이딩하게 하시오. `Car` 객체를 만들어 `move()`를 호출하는 코드를 작성하시오.

---

## 13. 정답과 해설

### 문제 1 정답

```text
P
C
```

부모 생성자가 먼저다.

### 문제 2 정답

```text
20
10
```

`n`은 자식 필드, `super.n`은 부모 필드다.

### 문제 3 정답

```text
C
```

자식이 오버라이딩한 메서드가 실행된다.

### 문제 4 정답

```text
7
3
```

`super(7)`로 부모 생성자를 먼저 호출한 뒤 자식 생성자 본문을 실행한다.

### 문제 5 예시 정답

```java
class Vehicle {
    void move() {
        System.out.println("move");
    }
}

class Car extends Vehicle {
    void move() {
        System.out.println("drive");
    }
}

class Main {
    public static void main(String[] args) {
        Car car = new Car();
        car.move();
    }
}
```

출력:

```text
drive
```

---

## 오늘의 마무리 체크

- `extends`는 상속을 뜻한다.
- 자식 객체에는 부모 부분과 자식 부분이 함께 있다.
- 자식 생성자 호출 시 부모 생성자가 먼저 실행된다.
- `super`는 부모를 가리킨다.
- 오버라이딩은 부모 메서드를 자식이 다시 정의하는 것이다.
- 같은 이름의 필드가 있으면 `super.필드`로 부모 필드에 접근한다.
