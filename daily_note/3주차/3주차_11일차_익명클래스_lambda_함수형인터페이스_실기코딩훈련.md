# 3주차 11일차 - Java 익명 클래스, lambda, 함수형 인터페이스 실기 코딩 훈련

## 오늘의 목표

오늘은 Java의 익명 클래스와 람다식을 중심으로 정보처리기사 실기 코딩 문제를 추적하는 힘을 기른다.

실기시험에서는 `lambda` 자체의 문법만 묻기보다, 인터페이스, 오버라이딩, 메서드 호출, 배열, 반복문, 컬렉션, static 변수와 함께 섞어서 출력 결과를 묻는 경우가 많다. 따라서 오늘 자료는 람다식을 "짧게 쓰는 문법"으로만 보지 않고, 실제로 어떤 메서드가 실행되는지 추적하는 훈련 자료다.

- 익명 클래스가 무엇인지 설명할 수 있다.
- 함수형 인터페이스의 조건을 설명할 수 있다.
- 익명 클래스와 람다식의 차이를 구분할 수 있다.
- 람다식의 매개변수, 실행문, 반환값 형태를 읽을 수 있다.
- 람다식이 변수, 배열, 메서드 인자로 전달될 때 실행 흐름을 추적할 수 있다.
- `this`, 지역 변수, static 변수와 람다식이 섞인 코드를 읽을 수 있다.
- 실기형 출력 추적 문제를 손으로 풀 수 있다.

## 3시간 수업 구성

| 시간 | 내용 |
|---|---|
| 0:00 ~ 0:25 | 인터페이스와 익명 클래스 복습 |
| 0:25 ~ 0:55 | 함수형 인터페이스와 lambda 기본 |
| 0:55 ~ 1:20 | 람다식 문법 축약 규칙 |
| 1:20 ~ 1:30 | 쉬는 시간 |
| 1:30 ~ 1:55 | 람다식을 변수와 매개변수로 사용 |
| 1:55 ~ 2:20 | 배열, 반복문, 컬렉션과 람다 |
| 2:20 ~ 2:45 | this, 지역 변수, static 변수 혼합 |
| 2:45 ~ 3:00 | 실기형 출력 추적 문제 |

---

## 1. 익명 클래스란?

익명 클래스는 이름이 없는 클래스다.

인터페이스나 추상 클래스를 즉석에서 구현할 때 사용한다.

```java
interface Printer {
    void print();
}

class Main {
    public static void main(String[] args) {
        Printer p = new Printer() {
            public void print() {
                System.out.println("Hello");
            }
        };

        p.print();
    }
}
```

출력:

```text
Hello
```

이 코드는 다음 의미다.

```text
Printer 인터페이스를 구현하는 이름 없는 클래스를 즉석에서 만든다.
그 객체를 p에 저장한다.
p.print()를 호출하면 익명 클래스 안의 print()가 실행된다.
```

---

## 2. 일반 클래스와 익명 클래스 비교

### 일반 클래스

```java
interface Printer {
    void print();
}

class MyPrinter implements Printer {
    public void print() {
        System.out.println("A");
    }
}

class Main {
    public static void main(String[] args) {
        Printer p = new MyPrinter();
        p.print();
    }
}
```

출력:

```text
A
```

### 익명 클래스

```java
interface Printer {
    void print();
}

class Main {
    public static void main(String[] args) {
        Printer p = new Printer() {
            public void print() {
                System.out.println("A");
            }
        };

        p.print();
    }
}
```

출력:

```text
A
```

두 코드는 실행 결과가 같다.

차이:

```text
일반 클래스: 클래스 이름이 있음
익명 클래스: 클래스 이름 없이 즉석에서 구현
```

---

## 3. 함수형 인터페이스

람다식은 아무 인터페이스에나 사용할 수 없다.

람다식은 추상 메서드가 1개인 인터페이스에 사용할 수 있다.

이런 인터페이스를 함수형 인터페이스라고 한다.

```java
interface Calculator {
    int calc(int a, int b);
}
```

`Calculator`에는 추상 메서드가 `calc` 1개만 있다. 따라서 람다식으로 구현할 수 있다.

```java
class Main {
    public static void main(String[] args) {
        Calculator c = (a, b) -> a + b;
        System.out.println(c.calc(3, 4));
    }
}
```

출력:

```text
7
```

읽는 법:

```text
(a, b) -> a + b

a와 b를 받아서
a + b를 반환하는 calc 메서드 구현
```

---

## 4. 람다식은 익명 클래스의 간단한 표현

익명 클래스:

```java
Calculator c = new Calculator() {
    public int calc(int a, int b) {
        return a + b;
    }
};
```

람다식:

```java
Calculator c = (a, b) -> a + b;
```

둘 다 의미는 같다.

```text
Calculator 인터페이스의 calc 메서드를 구현한다.
calc(3, 4)를 호출하면 7이 나온다.
```

단, 람다식은 함수형 인터페이스에만 사용할 수 있다.

---

## 5. 람다식 기본 문법

```java
(매개변수) -> 실행문
```

또는

```java
(매개변수) -> {
    실행문;
    return 값;
}
```

예제:

```java
interface Job {
    void run();
}

class Main {
    public static void main(String[] args) {
        Job j = () -> System.out.println("run");
        j.run();
    }
}
```

출력:

```text
run
```

매개변수가 없으면 `()`를 쓴다.

---

## 6. 람다식 축약 규칙

### 매개변수가 1개면 괄호 생략 가능

```java
interface Square {
    int get(int n);
}

class Main {
    public static void main(String[] args) {
        Square s = n -> n * n;
        System.out.println(s.get(5));
    }
}
```

출력:

```text
25
```

### 실행문이 1개면 중괄호와 return 생략 가능

```java
Calculator c = (a, b) -> a + b;
```

위 코드는 아래 코드와 같다.

```java
Calculator c = (a, b) -> {
    return a + b;
};
```

### 실행문이 여러 개면 중괄호 필요

```java
Calculator c = (a, b) -> {
    int result = a + b;
    return result * 2;
};
```

---

## 7. 람다식과 변수

람다식도 객체처럼 변수에 저장할 수 있다.

```java
interface Op {
    int apply(int n);
}

class Main {
    public static void main(String[] args) {
        Op op = n -> n + 10;
        System.out.println(op.apply(5));
    }
}
```

출력:

```text
15
```

추적:

```text
op에는 n -> n + 10 이 저장됨
op.apply(5)
n은 5
5 + 10 반환
```

---

## 8. 람다식 교체

같은 인터페이스 타입 변수에 다른 람다식을 다시 저장할 수 있다.

```java
interface Op {
    int apply(int n);
}

class Main {
    public static void main(String[] args) {
        Op op = n -> n + 1;
        System.out.print(op.apply(3) + " ");

        op = n -> n * 2;
        System.out.print(op.apply(3));
    }
}
```

출력:

```text
4 6
```

포인트:

```text
처음 op는 n + 1
나중 op는 n * 2로 바뀜
```

---

## 9. 람다식을 메서드 인자로 전달

람다식은 메서드의 인자로 전달할 수 있다.

```java
interface Op {
    int apply(int a, int b);
}

class Main {
    static int run(Op op, int x, int y) {
        return op.apply(x, y);
    }

    public static void main(String[] args) {
        System.out.println(run((a, b) -> a * b, 3, 4));
    }
}
```

출력:

```text
12
```

추적:

```text
run((a, b) -> a * b, 3, 4)
op는 곱셈 람다식
x는 3, y는 4
op.apply(3, 4) 실행
3 * 4 = 12
```

---

## 10. 람다식 배열

람다식도 배열에 넣을 수 있다.

```java
interface Op {
    int apply(int n);
}

class Main {
    public static void main(String[] args) {
        Op[] ops = {
            n -> n + 1,
            n -> n * 2,
            n -> n - 3
        };

        int result = 5;

        for (Op op : ops) {
            result = op.apply(result);
        }

        System.out.println(result);
    }
}
```

출력:

```text
9
```

추적:

```text
result = 5
첫 번째 람다: 5 + 1 = 6
두 번째 람다: 6 * 2 = 12
세 번째 람다: 12 - 3 = 9
```

---

## 11. 람다식과 반복문

```java
interface Check {
    boolean test(int n);
}

class Main {
    public static void main(String[] args) {
        int[] arr = { 1, 2, 3, 4, 5 };
        Check even = n -> n % 2 == 0;
        int count = 0;

        for (int n : arr) {
            if (even.test(n)) {
                count++;
            }
        }

        System.out.println(count);
    }
}
```

출력:

```text
2
```

짝수는 2와 4이므로 count는 2다.

---

## 12. 람다식과 문자열

```java
interface Text {
    String change(String s);
}

class Main {
    public static void main(String[] args) {
        Text t = s -> s.substring(1) + s.charAt(0);
        System.out.println(t.change("JAVA"));
    }
}
```

출력:

```text
AVAJ
```

추적:

```text
s = "JAVA"
s.substring(1) -> "AVA"
s.charAt(0) -> 'J'
"AVA" + 'J' -> "AVAJ"
```

---

## 13. 람다식과 조건문

```java
interface Grade {
    String get(int score);
}

class Main {
    public static void main(String[] args) {
        Grade g = score -> {
            if (score >= 60) {
                return "P";
            }
            return "F";
        };

        System.out.println(g.get(75));
    }
}
```

출력:

```text
P
```

중괄호를 쓰면 `return`을 직접 적어야 한다.

---

## 14. 람다식과 static 변수

```java
interface Counter {
    void add();
}

class Main {
    static int count = 0;

    public static void main(String[] args) {
        Counter c = () -> count++;

        c.add();
        c.add();
        c.add();

        System.out.println(count);
    }
}
```

출력:

```text
3
```

`count++`는 현재 값을 사용한 뒤 1 증가시킨다.

---

## 15. 람다식과 지역 변수

람다식 안에서 지역 변수를 사용할 수 있다.

```java
interface Op {
    int apply(int n);
}

class Main {
    public static void main(String[] args) {
        int base = 10;
        Op op = n -> n + base;

        System.out.println(op.apply(5));
    }
}
```

출력:

```text
15
```

단, 람다식에서 사용하는 지역 변수는 이후에 변경하면 안 된다.

잘못된 코드:

```java
int base = 10;
Op op = n -> n + base;
base = 20;
```

이 코드는 컴파일 오류다.

이유:

```text
람다식에서 사용하는 지역 변수는 final 또는 effectively final이어야 한다.
effectively final은 final을 붙이지 않았지만 실제로 값이 한 번만 정해진 변수를 말한다.
```

---

## 16. 익명 클래스의 this

익명 클래스 안의 `this`는 익명 클래스 객체 자신을 가리킨다.

```java
interface Printer {
    void print();
}

class Main {
    int value = 10;

    void run() {
        Printer p = new Printer() {
            int value = 20;

            public void print() {
                System.out.println(this.value);
            }
        };

        p.print();
    }

    public static void main(String[] args) {
        new Main().run();
    }
}
```

출력:

```text
20
```

익명 클래스 안의 `this.value`는 익명 클래스의 `value`다.

---

## 17. 람다식의 this

람다식 안의 `this`는 람다식을 감싸고 있는 바깥 객체를 가리킨다.

```java
interface Printer {
    void print();
}

class Main {
    int value = 10;

    void run() {
        Printer p = () -> System.out.println(this.value);
        p.print();
    }

    public static void main(String[] args) {
        new Main().run();
    }
}
```

출력:

```text
10
```

비교:

```text
익명 클래스의 this -> 익명 클래스 객체
람다식의 this -> 바깥 객체
```

---

## 18. 기본 함수형 인터페이스

Java에는 자주 쓰는 함수형 인터페이스가 `java.util.function` 패키지에 준비되어 있다.

실기에서는 이름과 역할 정도를 알아두면 좋다.

| 인터페이스 | 추상 메서드 | 의미 |
|---|---|---|
| `Function<T, R>` | `R apply(T t)` | T를 받아 R을 반환 |
| `Consumer<T>` | `void accept(T t)` | T를 받아 소비, 반환 없음 |
| `Supplier<T>` | `T get()` | 매개변수 없이 T 반환 |
| `Predicate<T>` | `boolean test(T t)` | T를 받아 boolean 반환 |
| `BinaryOperator<T>` | `T apply(T a, T b)` | 같은 타입 2개를 받아 같은 타입 반환 |

예제:

```java
import java.util.function.Predicate;

class Main {
    public static void main(String[] args) {
        Predicate<Integer> p = n -> n > 0;
        System.out.println(p.test(3));
        System.out.println(p.test(-1));
    }
}
```

출력:

```text
true
false
```

---

## 19. 컬렉션과 람다

`ArrayList`와 람다식이 같이 나올 수 있다.

```java
import java.util.ArrayList;

class Main {
    public static void main(String[] args) {
        ArrayList<Integer> list = new ArrayList<>();
        list.add(3);
        list.add(1);
        list.add(4);

        list.forEach(n -> System.out.print(n * 2 + " "));
    }
}
```

출력:

```text
6 2 8
```

`forEach`는 리스트의 원소를 하나씩 꺼내 람다식에 전달한다.

---

## 20. sort와 람다

정렬 기준을 람다식으로 줄 수 있다.

```java
import java.util.ArrayList;
import java.util.Collections;

class Main {
    public static void main(String[] args) {
        ArrayList<Integer> list = new ArrayList<>();
        list.add(3);
        list.add(1);
        list.add(4);

        Collections.sort(list, (a, b) -> b - a);

        for (int n : list) {
            System.out.print(n + " ");
        }
    }
}
```

출력:

```text
4 3 1
```

정렬 기준:

```text
(a, b) -> a - b  오름차순
(a, b) -> b - a  내림차순
```

---

## 21. 실기 출력 추적 요령

람다식 문제가 나오면 다음 순서로 추적한다.

```text
1. 인터페이스의 추상 메서드 이름과 매개변수, 반환 타입을 확인한다.
2. 람다식이 그 추상 메서드를 구현한다고 생각한다.
3. 람다식이 언제 실행되는지 찾는다.
4. 변수에 저장만 한 줄은 실행이 아니다.
5. apply(), test(), accept(), run() 같은 메서드를 호출해야 실행된다.
6. 람다식 안에서 사용하는 외부 변수 값을 확인한다.
7. static 변수는 호출이 반복될 때 계속 누적된다.
8. 익명 클래스와 람다의 this 차이를 구분한다.
```

중요한 문장:

```text
람다식은 저장되는 순간 실행되는 것이 아니다.
추상 메서드를 호출할 때 실행된다.
```

---

## 22. 실전 문제 1

다음 코드의 출력 결과를 쓰시오.

```java
interface Calc {
    int run(int a, int b);
}

class Main {
    public static void main(String[] args) {
        Calc c = (a, b) -> a + b * 2;
        System.out.println(c.run(3, 4));
    }
}
```

정답:

```text
11
```

해설:

```text
a = 3, b = 4
a + b * 2
3 + 4 * 2 = 11
```

---

## 23. 실전 문제 2

다음 코드의 출력 결과를 쓰시오.

```java
interface Op {
    int apply(int n);
}

class Main {
    static int run(Op op, int n) {
        return op.apply(n) + 1;
    }

    public static void main(String[] args) {
        System.out.println(run(x -> x * x, 5));
    }
}
```

정답:

```text
26
```

해설:

```text
op.apply(5) -> 5 * 5 = 25
run은 op.apply(n) + 1 반환
25 + 1 = 26
```

---

## 24. 실전 문제 3

다음 코드의 출력 결과를 쓰시오.

```java
interface Op {
    int apply(int n);
}

class Main {
    public static void main(String[] args) {
        Op[] ops = {
            n -> n + 2,
            n -> n * 3,
            n -> n - 4
        };

        int x = 1;
        for (Op op : ops) {
            x = op.apply(x);
        }

        System.out.println(x);
    }
}
```

정답:

```text
5
```

해설:

```text
x = 1
첫 번째: 1 + 2 = 3
두 번째: 3 * 3 = 9
세 번째: 9 - 4 = 5
```

---

## 25. 실전 문제 4

다음 코드의 출력 결과를 쓰시오.

```java
interface Check {
    boolean test(int n);
}

class Main {
    public static void main(String[] args) {
        int[] arr = { 2, 5, 8, 11 };
        Check c = n -> n % 2 == 0;
        int sum = 0;

        for (int n : arr) {
            if (c.test(n)) {
                sum += n;
            }
        }

        System.out.println(sum);
    }
}
```

정답:

```text
10
```

해설:

```text
짝수는 2, 8
sum = 2 + 8 = 10
```

---

## 26. 실전 문제 5

다음 코드의 출력 결과를 쓰시오.

```java
interface Text {
    String apply(String s);
}

class Main {
    public static void main(String[] args) {
        Text t = s -> s.charAt(1) + s.substring(2);
        System.out.println(t.apply("KOREA"));
    }
}
```

정답:

```text
OREA
```

해설:

```text
s = "KOREA"
s.charAt(1) -> 'O'
s.substring(2) -> "REA"
'O' + "REA" -> "OREA"
```

---

## 27. 실전 문제 6

다음 코드의 출력 결과를 쓰시오.

```java
interface Job {
    void run();
}

class Main {
    static int count = 1;

    public static void main(String[] args) {
        Job j = () -> count *= 2;

        j.run();
        j.run();

        System.out.println(count);
    }
}
```

정답:

```text
4
```

해설:

```text
count = 1
첫 번째 j.run() -> count = 2
두 번째 j.run() -> count = 4
```

---

## 28. 실전 문제 7

다음 코드의 출력 결과를 쓰시오.

```java
interface Calc {
    int run(int n);
}

class Main {
    public static void main(String[] args) {
        int base = 3;
        Calc c = n -> n + base;

        System.out.println(c.run(7));
    }
}
```

정답:

```text
10
```

해설:

```text
base = 3
n = 7
n + base = 10
```

---

## 29. 실전 문제 8

다음 코드의 출력 결과를 쓰시오.

```java
interface Printer {
    void print();
}

class Main {
    int value = 5;

    void run() {
        Printer p = new Printer() {
            int value = 9;

            public void print() {
                System.out.print(this.value + " ");
            }
        };

        p.print();

        Printer q = () -> System.out.print(this.value + " ");
        q.print();
    }

    public static void main(String[] args) {
        new Main().run();
    }
}
```

정답:

```text
9 5
```

해설:

```text
익명 클래스 안의 this.value -> 익명 클래스의 value = 9
람다식 안의 this.value -> 바깥 Main 객체의 value = 5
```

---

## 30. 실전 문제 9

다음 코드의 출력 결과를 쓰시오.

```java
import java.util.function.Function;

class Main {
    public static void main(String[] args) {
        Function<Integer, Integer> f = n -> n * 2 + 1;
        System.out.println(f.apply(4));
    }
}
```

정답:

```text
9
```

해설:

```text
Function<T, R>의 메서드는 apply
f.apply(4) -> 4 * 2 + 1 = 9
```

---

## 31. 실전 문제 10

다음 코드의 출력 결과를 쓰시오.

```java
import java.util.ArrayList;
import java.util.Collections;

class Main {
    public static void main(String[] args) {
        ArrayList<Integer> list = new ArrayList<>();
        list.add(7);
        list.add(2);
        list.add(5);

        Collections.sort(list, (a, b) -> a - b);

        list.forEach(n -> System.out.print(n + 1 + " "));
    }
}
```

정답:

```text
3 6 8
```

해설:

```text
정렬 전: 7, 2, 5
(a, b) -> a - b 이므로 오름차순 정렬
정렬 후: 2, 5, 7
forEach에서 각 값에 1을 더해 출력
3 6 8
```

---

## 32. 오늘의 핵심 정리

람다식은 문법 모양보다 실행 시점을 잡는 것이 중요하다.

```text
익명 클래스는 이름 없는 클래스다.
람다식은 함수형 인터페이스를 간단히 구현하는 문법이다.
함수형 인터페이스는 추상 메서드가 1개인 인터페이스다.
람다식은 저장만 해서는 실행되지 않는다.
run(), apply(), test(), accept() 같은 메서드를 호출할 때 실행된다.
람다식에서 사용하는 지역 변수는 final 또는 effectively final이어야 한다.
익명 클래스의 this와 람다식의 this는 다르다.
```

실기시험에서는 람다식이 보이면 먼저 인터페이스의 추상 메서드를 찾고, 그 메서드가 호출되는 순간에 람다식 본문을 대입해서 계산한다.

