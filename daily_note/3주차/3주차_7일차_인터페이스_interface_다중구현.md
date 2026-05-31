# 3주차 7일차 - 인터페이스 interface와 다중 구현

## 오늘의 목표

오늘은 `interface`를 다룬다. 인터페이스는 서로 다른 클래스가 반드시 제공해야 할 기능의 규칙을 정한다. 시험에서는 문법 암기만으로 끝나지 않고, 인터페이스 타입 참조와 오버라이딩 호출 결과를 추적해야 한다.

- 인터페이스가 기능 규칙이라는 것을 설명할 수 있다.
- `implements`와 `extends`를 구분할 수 있다.
- 인터페이스 타입 변수로 구현 객체를 참조할 수 있다.
- 한 클래스가 여러 인터페이스를 구현하는 코드를 읽을 수 있다.
- 추상 클래스와 인터페이스의 공통점과 차이점을 구분할 수 있다.
- 인터페이스, 배열, 다형성이 섞인 실기형 코드를 추적할 수 있다.

## 선수 지식

```text
상속          : class Child extends Parent
오버라이딩    : 부모 또는 규칙의 메서드를 자식이 다시 작성
다형성        : 부모 타입이나 인터페이스 타입으로 실제 객체 참조
추상 클래스   : 공통 상태와 기능, 구현 의무를 함께 제공
```

## 3시간 수업 구성

| 시간 | 내용 |
|---|---|
| 0:00 ~ 0:25 | 인터페이스의 필요성과 기본 문법 |
| 0:25 ~ 0:55 | `implements`, 인터페이스 타입 다형성 |
| 0:55 ~ 1:20 | 다중 구현과 상속 결합 |
| 1:20 ~ 1:30 | 쉬는 시간 |
| 1:30 ~ 1:55 | 추상 클래스와 인터페이스 비교 |
| 1:55 ~ 2:35 | 배열, 형변환, 실기형 추적 |
| 2:35 ~ 3:00 | 혼자 연습 문제와 오답 점검 |

---

## 1. 인터페이스는 기능 규칙이다

다음 상황을 생각해보자.

```text
자동차도 움직인다.
드론도 움직인다.
사람도 움직인다.

하지만 자동차, 드론, 사람은 같은 종류가 아니다.
```

상속은 보통 “자식은 부모의 한 종류다”라는 관계에 사용한다.

```text
Dog is an Animal       -> 자연스러움
Car is an Animal       -> 어색함
Drone is a Car         -> 어색함
```

서로 다른 종류라도 같은 기능을 제공해야 할 수 있다. 이때 인터페이스로 규칙을 정한다.

```text
Movable 규칙
  |
  +-- Car: move() 구현
  +-- Drone: move() 구현
  +-- Person: move() 구현
```

---

## 2. interface 기본 문법

```java
interface Movable {
    void move();
}

class Car implements Movable {
    public void move() {
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

### 문법 읽기

```text
interface Movable
=> move() 기능 규칙을 선언한다.

class Car implements Movable
=> Car는 Movable 규칙을 구현한다.
```

---

## 3. 왜 public을 붙이는가

인터페이스의 추상 메서드는 기본적으로 `public abstract`다.

```java
interface Movable {
    void move();
}
```

위 코드는 다음 의미와 같다.

```java
interface Movable {
    public abstract void move();
}
```

구현 메서드는 더 좁은 접근 범위로 만들 수 없다. 따라서 구현할 때 `public`을 붙인다.

```java
interface Movable {
    void move();
}

class Car implements Movable {
    // void move() { } // 컴파일 오류: public보다 좁은 범위

    public void move() {
        System.out.println("drive");
    }
}
```

이 부분은 일반적인 클래스 오버라이딩 예제와 차이가 있으므로 주의한다.

---

## 4. 인터페이스는 직접 객체를 만들 수 없다

```java
interface Movable {
    void move();
}

// Movable m = new Movable(); // 컴파일 오류
```

인터페이스는 기능 규칙이지 완성된 객체 설계도가 아니다.

하지만 인터페이스 타입 변수는 만들 수 있다.

```java
Movable m = new Car();
m.move();
```

출력:

```text
drive
```

그림:

```text
Movable m = new Car();
    |           |
    |           +-- 실제 객체: Car
    +-------------- 참조 변수 타입: Movable

m.move() -> 실제 객체 Car의 move()
```

추상 클래스에서 배운 다형성과 같은 원리다.

---

## 5. 여러 구현 객체를 한 배열에 넣기

```java
interface Soundable {
    void sound();
}

class Dog implements Soundable {
    public void sound() {
        System.out.println("Dog");
    }
}

class Bell implements Soundable {
    public void sound() {
        System.out.println("Bell");
    }
}

class Main {
    public static void main(String[] args) {
        Soundable[] arr = {
            new Dog(),
            new Bell(),
            new Dog()
        };

        for (int i = 0; i < arr.length; i++) {
            arr[i].sound();
        }
    }
}
```

출력:

```text
Dog
Bell
Dog
```

### 배열 시각화

```text
Soundable[] arr
+-----+-----+-----+
| [0] | [1] | [2] |
+--|--+--|--+--|--+
   |     |     |
   v     v     v
  Dog   Bell   Dog

arr[i].sound()
-> 각 칸의 실제 객체가 구현한 sound() 실행
```

---

## 6. 한 클래스가 여러 인터페이스를 구현할 수 있다

Java 클래스는 여러 클래스를 동시에 상속할 수 없다.

```java
// class C extends A, B { } // 불가능
```

하지만 여러 인터페이스는 동시에 구현할 수 있다.

```java
interface Printable {
    void print();
}

interface Savable {
    void save();
}

class Report implements Printable, Savable {
    public void print() {
        System.out.println("print");
    }

    public void save() {
        System.out.println("save");
    }
}

class Main {
    public static void main(String[] args) {
        Report r = new Report();
        r.print();
        r.save();
    }
}
```

출력:

```text
print
save
```

그림:

```text
Printable ----\
               >---- Report
Savable   ----/
```

---

## 7. 상속과 인터페이스 구현을 함께 사용하기

```java
class Device {
    String name;

    Device(String name) {
        this.name = name;
    }

    void info() {
        System.out.println(name);
    }
}

interface Chargeable {
    void charge();
}

class Phone extends Device implements Chargeable {
    Phone(String name) {
        super(name);
    }

    public void charge() {
        System.out.println(name + ":charge");
    }
}

class Main {
    public static void main(String[] args) {
        Phone p = new Phone("Phone");
        p.info();
        p.charge();
    }
}
```

출력:

```text
Phone
Phone:charge
```

문법 순서:

```text
class 자식 extends 부모 implements 인터페이스
```

---

## 8. 인터페이스 상수

인터페이스에 선언한 필드는 기본적으로 `public static final`이다.

```java
interface Rule {
    int MAX = 100;
}

class Main {
    public static void main(String[] args) {
        System.out.println(Rule.MAX);
        // Rule.MAX = 200; // 컴파일 오류
    }
}
```

출력:

```text
100
```

다음 두 선언은 같은 의미다.

```java
int MAX = 100;
public static final int MAX = 100;
```

시험 포인트:

```text
static -> 인터페이스 이름으로 접근 가능
final  -> 값 변경 불가능
```

---

## 9. default 메서드

인터페이스 메서드는 보통 구현 클래스가 작성한다. 하지만 `default` 메서드는 인터페이스 안에 본문을 가질 수 있다.

```java
interface Printer {
    void print();

    default void ready() {
        System.out.println("ready");
    }
}

class ConsolePrinter implements Printer {
    public void print() {
        System.out.println("print");
    }
}

class Main {
    public static void main(String[] args) {
        Printer p = new ConsolePrinter();
        p.ready();
        p.print();
    }
}
```

출력:

```text
ready
print
```

실기 대비 우선순위는 다음과 같다.

```text
1순위: implements, 구현 메서드, 인터페이스 타입 다형성
2순위: 다중 구현, 상수
3순위: default 메서드의 존재와 호출 결과
```

---

## 10. 추상 클래스와 인터페이스 비교

| 구분 | 추상 클래스 | 인터페이스 |
|---|---|---|
| 선언 | `abstract class A` | `interface A` |
| 관계 키워드 | `extends` | `implements` |
| 직접 객체 생성 | 불가능 | 불가능 |
| 생성자 | 가질 수 있음 | 없음 |
| 인스턴스 필드 | 가질 수 있음 | 일반 인스턴스 필드 없음 |
| 일반 메서드 | 가질 수 있음 | `default` 등 제한적으로 가능 |
| 추상 메서드 | 가질 수 있음 | 핵심 기능 |
| 여러 개 사용 | 클래스 상속은 하나 | 여러 인터페이스 구현 가능 |
| 적합한 상황 | 공통 상태와 공통 코드도 공유 | 서로 다른 클래스에 기능 규칙 부여 |

### 시각화

```text
추상 클래스:
Animal
  |
  +-- Dog
  +-- Cat

"Dog와 Cat은 Animal의 한 종류다."

인터페이스:
Flyable
  |
  +-- Bird
  +-- Drone

"Bird와 Drone은 종류는 다르지만 fly() 기능을 제공한다."
```

---

## 11. 인터페이스 타입과 형변환

인터페이스 타입 변수로는 인터페이스에 선언된 메서드만 바로 호출할 수 있다.

```java
interface Movable {
    void move();
}

class Car implements Movable {
    public void move() {
        System.out.println("move");
    }

    void stop() {
        System.out.println("stop");
    }
}

class Main {
    public static void main(String[] args) {
        Movable m = new Car();
        m.move();
        // m.stop(); // 컴파일 오류

        Car c = (Car) m;
        c.stop();
    }
}
```

출력:

```text
move
stop
```

`m`이 실제로 `Car` 객체를 가리키므로 형변환 후 `Car`만 가진 `stop()`을 호출할 수 있다.

---

## 12. 실기 문제 추적 순서

```text
1. interface 선언과 메서드 목록을 찾는다.
2. implements가 있는 클래스를 찾는다.
3. 구현 메서드에 public이 있는지 확인한다.
4. new 뒤의 실제 객체 타입을 적는다.
5. 인터페이스 타입 배열이면 인덱스별 실제 객체를 적는다.
6. 호출 가능한 메서드는 참조 타입으로 확인한다.
7. 실행되는 오버라이딩 메서드는 실제 객체로 확인한다.
```

---

## 13. 실전 실기형 예제 1

다음 코드의 출력 결과를 쓰시오.

```java
interface A {
    void print();
}

class B implements A {
    public void print() {
        System.out.print("B");
    }
}

class C implements A {
    public void print() {
        System.out.print("C");
    }
}

class Main {
    public static void main(String[] args) {
        A[] arr = { new B(), new C(), new B() };

        for (int i = 0; i < arr.length; i++) {
            arr[i].print();
        }
    }
}
```

정답:

```text
BCB
```

---

## 14. 실전 실기형 예제 2

다음 코드의 출력 결과를 쓰시오.

```java
interface Calc {
    int run(int n);
}

class Add implements Calc {
    public int run(int n) {
        return n + 2;
    }
}

class Multi implements Calc {
    public int run(int n) {
        return n * 3;
    }
}

class Main {
    public static void main(String[] args) {
        Calc[] arr = { new Add(), new Multi(), new Add() };
        int result = 1;

        for (int i = 0; i < arr.length; i++) {
            result = arr[i].run(result);
        }

        System.out.println(result);
    }
}
```

상태표:

| i | 실제 객체 | 계산 | result |
|---:|---|---|---:|
| 시작 | - | - | 1 |
| 0 | `Add` | `1 + 2` | 3 |
| 1 | `Multi` | `3 * 3` | 9 |
| 2 | `Add` | `9 + 2` | 11 |

정답:

```text
11
```

---

## 15. 실전 실기형 예제 3

다음 코드의 출력 결과를 쓰시오.

```java
interface Printable {
    void print();
}

interface Countable {
    int count();
}

class Report implements Printable, Countable {
    int n;

    Report(int n) {
        this.n = n;
    }

    public void print() {
        System.out.print("R");
    }

    public int count() {
        return n * 2;
    }
}

class Main {
    public static void main(String[] args) {
        Report r = new Report(4);
        Printable p = r;
        Countable c = r;

        p.print();
        System.out.println(c.count());
    }
}
```

정답:

```text
R8
```

`p`와 `c`는 타입은 다르지만 같은 `Report` 객체를 참조한다.

```text
p --------\
           >---- Report 객체: n = 4
c --------/
```

---

## 16. 직접 코딩 실습

### 실습 1: 알림 기능 만들기

```text
1. interface Notifier를 만든다.
2. void send(String message)를 선언한다.
3. EmailNotifier와 SmsNotifier가 Notifier를 구현한다.
4. 각 send()는 "EMAIL:" 또는 "SMS:" 뒤에 message를 출력한다.
5. Notifier[] 배열을 만들고 반복문으로 send("hello")를 호출한다.
```

### 실습 2: 다중 구현 추가

```text
1. interface Loggable을 만든다.
2. void log()를 선언한다.
3. EmailNotifier가 Notifier, Loggable을 모두 구현하게 한다.
4. EmailNotifier 객체를 만든 뒤 두 메서드를 호출한다.
```

### 실습 3: 변형 훈련

- `PushNotifier`를 추가한다.
- 배열의 순서를 바꾼다.
- `send()`에 호출 횟수를 세는 필드를 추가한다.
- 각 객체가 호출된 횟수를 출력한다.

---

## 17. 오늘의 혼자 연습 문제

### 문제 1

빈칸에 들어갈 키워드를 쓰시오.

```java
interface Flyable {
    void fly();
}

class Bird ______ Flyable {
    public void fly() {
        System.out.println("fly");
    }
}
```

### 문제 2

다음 코드의 출력 결과를 쓰시오.

```java
interface A {
    void f();
}

class B implements A {
    public void f() {
        System.out.print("1");
    }
}

class C implements A {
    public void f() {
        System.out.print("2");
    }
}

class Main {
    public static void main(String[] args) {
        A a = new C();
        a.f();
        a = new B();
        a.f();
    }
}
```

### 문제 3

다음 코드의 출력 결과를 쓰시오.

```java
interface Rule {
    int VALUE = 10;
}

class Main {
    public static void main(String[] args) {
        System.out.println(Rule.VALUE);
    }
}
```

그리고 `Rule.VALUE = 20;`을 추가할 수 없는 이유를 설명하시오.

### 문제 4

다음 코드의 출력 결과를 쓰시오.

```java
interface Calc {
    int calc(int n);
}

class Plus implements Calc {
    public int calc(int n) {
        return n + 1;
    }
}

class Square implements Calc {
    public int calc(int n) {
        return n * n;
    }
}

class Main {
    public static void main(String[] args) {
        Calc[] arr = { new Plus(), new Square(), new Plus() };
        int result = 2;

        for (int i = 0; i < arr.length; i++) {
            result = arr[i].calc(result);
        }

        System.out.println(result);
    }
}
```

### 문제 5

다음 조건을 만족하는 코드를 작성하시오.

```text
- interface Discountable에 int discount(int price)를 선언한다.
- StudentDiscount는 가격에서 1000을 뺀다.
- VipDiscount는 가격의 20%를 뺀다. 정수 계산을 사용한다.
- Discountable 배열에 두 객체를 넣는다.
- 시작 가격 10000에 할인 정책을 배열 순서대로 적용하고 최종 가격을 출력한다.
```

---

## 18. 정답과 해설

### 문제 1 정답

```text
implements
```

클래스가 인터페이스 규칙을 구현할 때 `implements`를 사용한다.

### 문제 2 정답

```text
21
```

인터페이스 타입 변수 `a`가 처음에는 `C`, 다음에는 `B` 객체를 가리킨다. 실제 객체의 구현 메서드가 실행된다.

### 문제 3 정답

```text
10
```

인터페이스 필드는 기본적으로 `public static final`이다. `final`이므로 다른 값을 다시 대입할 수 없다.

### 문제 4 정답

```text
10
```

상태표:

| 단계 | 계산 | result |
|---|---|---:|
| 시작 | - | 2 |
| `Plus` | `2 + 1` | 3 |
| `Square` | `3 * 3` | 9 |
| `Plus` | `9 + 1` | 10 |

### 문제 5 예시 정답

```java
interface Discountable {
    int discount(int price);
}

class StudentDiscount implements Discountable {
    public int discount(int price) {
        return price - 1000;
    }
}

class VipDiscount implements Discountable {
    public int discount(int price) {
        return price - price * 20 / 100;
    }
}

class Main {
    public static void main(String[] args) {
        Discountable[] arr = {
            new StudentDiscount(),
            new VipDiscount()
        };

        int price = 10000;
        for (int i = 0; i < arr.length; i++) {
            price = arr[i].discount(price);
        }

        System.out.println(price);
    }
}
```

출력:

```text
7200
```

---

## 19. 오늘의 마무리 체크

- 인터페이스는 서로 다른 클래스에 공통 기능 규칙을 부여한다.
- 클래스가 인터페이스를 구현할 때 `implements`를 쓴다.
- 인터페이스는 직접 객체를 만들 수 없지만 참조 변수 타입으로 사용할 수 있다.
- 인터페이스 메서드를 구현할 때 `public`을 빠뜨리지 않는다.
- 한 클래스는 여러 인터페이스를 구현할 수 있다.
- 인터페이스 필드는 기본적으로 `public static final`이다.
- 인터페이스 타입으로 호출 가능한 메서드와 실제 객체가 실행하는 메서드를 구분한다.

## 20. 5분 오답 노트

```text
1. class가 interface를 구현할 때 키워드는 ______ 이다.
2. interface 메서드는 기본적으로 public ______ 이다.
3. interface의 필드는 기본적으로 public static ______ 이다.
4. 한 class는 여러 interface를 ______ 할 수 있다.
5. 인터페이스 타입 변수로 호출한 구현 메서드는 ______ 객체 기준으로 실행된다.
```

