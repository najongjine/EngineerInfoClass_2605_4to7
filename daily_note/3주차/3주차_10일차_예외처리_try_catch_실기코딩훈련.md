# 3주차 10일차 - Java 예외처리 try-catch 실기 코딩 훈련

## 오늘의 목표

오늘은 Java의 `try-catch-finally`를 중심으로 정보처리기사 실기 코딩 문제를 추적하는 힘을 기른다.

실기시험의 Java 문제는 한 문법만 단독으로 나오지 않는다. 예외처리 문제처럼 보여도 실제로는 배열, 반복문, 문자열, 클래스, 상속, static, enum, 형변환이 같이 섞여 나온다. 따라서 오늘 자료는 `try-catch`만 외우는 자료가 아니라, 코드 실행 흐름을 손으로 끝까지 추적하는 훈련 자료다.

- `try`, `catch`, `finally`의 실행 순서를 설명할 수 있다.
- 예외가 발생한 줄 이후의 `try` 코드는 실행되지 않는다는 점을 추적할 수 있다.
- 여러 `catch` 중 어떤 블록이 실행되는지 판단할 수 있다.
- `return`과 `finally`가 함께 있을 때 출력과 반환값을 구분할 수 있다.
- `throw`, `throws`, 사용자 정의 예외의 기본 형태를 읽을 수 있다.
- 배열, 문자열, 반복문, 클래스 문법이 섞인 예외처리 코드를 실기 방식으로 추적할 수 있다.

## 3시간 수업 구성

| 시간 | 내용 |
|---|---|
| 0:00 ~ 0:25 | 예외처리 기본 구조 |
| 0:25 ~ 0:55 | try-catch-finally 실행 순서 |
| 0:55 ~ 1:20 | 대표 예외: ArithmeticException, ArrayIndexOutOfBoundsException, NumberFormatException |
| 1:20 ~ 1:30 | 쉬는 시간 |
| 1:30 ~ 1:55 | 여러 catch, catch 순서, Exception |
| 1:55 ~ 2:20 | return, throw, throws |
| 2:20 ~ 2:45 | 클래스, 상속, static, enum과 예외처리 혼합 |
| 2:45 ~ 3:00 | 실기형 출력 추적 문제 |

---

## 1. 예외처리의 핵심

예외는 프로그램 실행 중 발생하는 비정상 상황이다.

예외처리를 하지 않으면 예외가 발생한 지점에서 프로그램이 중단된다.

```java
class Main {
    public static void main(String[] args) {
        System.out.println("A");
        System.out.println(10 / 0);
        System.out.println("B");
    }
}
```

실행 흐름:

```text
A 출력
10 / 0 에서 ArithmeticException 발생
프로그램 중단
B는 출력되지 않음
```

`try-catch`를 사용하면 예외가 발생해도 프로그램 흐름을 이어갈 수 있다.

```java
class Main {
    public static void main(String[] args) {
        System.out.println("A");

        try {
            System.out.println(10 / 0);
        } catch (ArithmeticException e) {
            System.out.println("C");
        }

        System.out.println("B");
    }
}
```

출력:

```text
A
C
B
```

중요한 규칙:

```text
try 안에서 예외 발생
-> 예외가 발생한 줄 이후의 try 코드는 건너뜀
-> 맞는 catch로 이동
-> catch 실행 후 try-catch 밖의 코드 계속 실행
```

---

## 2. try-catch 기본 구조

```java
try {
    예외가 발생할 수 있는 코드
} catch (예외클래스 변수명) {
    예외가 발생했을 때 실행할 코드
}
```

예제:

```java
class Main {
    public static void main(String[] args) {
        int a = 10;
        int b = 0;

        try {
            System.out.println(a / b);
            System.out.println("try end");
        } catch (ArithmeticException e) {
            System.out.println("zero");
        }

        System.out.println("done");
    }
}
```

출력:

```text
zero
done
```

`System.out.println("try end");`는 실행되지 않는다.

왜냐하면 바로 위 줄 `a / b`에서 예외가 발생했기 때문이다.

---

## 3. finally

`finally`는 예외 발생 여부와 관계없이 실행된다.

```java
class Main {
    public static void main(String[] args) {
        try {
            System.out.println("A");
            System.out.println(5 / 0);
            System.out.println("B");
        } catch (ArithmeticException e) {
            System.out.println("C");
        } finally {
            System.out.println("D");
        }

        System.out.println("E");
    }
}
```

출력:

```text
A
C
D
E
```

흐름:

```text
A 출력
5 / 0 예외 발생
B 건너뜀
catch 실행 -> C 출력
finally 실행 -> D 출력
try-catch-finally 밖으로 이동 -> E 출력
```

예외가 발생하지 않아도 `finally`는 실행된다.

```java
class Main {
    public static void main(String[] args) {
        try {
            System.out.println("A");
            System.out.println(5 / 1);
        } catch (ArithmeticException e) {
            System.out.println("B");
        } finally {
            System.out.println("C");
        }
    }
}
```

출력:

```text
A
5
C
```

---

## 4. 대표 예외 1: ArithmeticException

정수를 0으로 나누면 발생한다.

```java
class Main {
    public static void main(String[] args) {
        int[] arr = { 10, 5, 0, 2 };

        for (int i = 0; i < arr.length; i++) {
            try {
                System.out.print(20 / arr[i] + " ");
            } catch (ArithmeticException e) {
                System.out.print("X ");
            }
        }
    }
}
```

출력:

```text
2 4 X 10
```

추적:

| i | arr[i] | 20 / arr[i] | 출력 |
|---|---:|---:|---|
| 0 | 10 | 2 | 2 |
| 1 | 5 | 4 | 4 |
| 2 | 0 | 예외 | X |
| 3 | 2 | 10 | 10 |

---

## 5. 대표 예외 2: ArrayIndexOutOfBoundsException

배열 범위를 벗어나면 발생한다.

```java
class Main {
    public static void main(String[] args) {
        int[] arr = { 3, 6, 9 };

        try {
            for (int i = 0; i <= arr.length; i++) {
                System.out.print(arr[i] + " ");
            }
        } catch (ArrayIndexOutOfBoundsException e) {
            System.out.print("end");
        }
    }
}
```

출력:

```text
3 6 9 end
```

주의:

```text
arr.length는 3
사용 가능한 인덱스는 0, 1, 2
i <= arr.length 이므로 i가 3일 때 arr[3] 접근
arr[3]은 없으므로 예외 발생
```

---

## 6. 대표 예외 3: NumberFormatException

숫자로 바꿀 수 없는 문자열을 `Integer.parseInt()`로 변환하면 발생한다.

```java
class Main {
    public static void main(String[] args) {
        String[] data = { "10", "20", "A", "30" };
        int sum = 0;

        for (String s : data) {
            try {
                sum += Integer.parseInt(s);
            } catch (NumberFormatException e) {
                sum += 100;
            }
        }

        System.out.println(sum);
    }
}
```

출력:

```text
160
```

추적:

```text
"10" -> 10 더함 -> sum = 10
"20" -> 20 더함 -> sum = 30
"A"  -> 예외 발생 -> 100 더함 -> sum = 130
"30" -> 30 더함 -> sum = 160
```

---

## 7. 여러 catch

여러 종류의 예외를 다르게 처리할 수 있다.

```java
class Main {
    public static void main(String[] args) {
        String[] arr = { "8", "0", "A" };

        for (int i = 0; i <= arr.length; i++) {
            try {
                int n = Integer.parseInt(arr[i]);
                System.out.print(24 / n + " ");
            } catch (ArithmeticException e) {
                System.out.print("Z ");
            } catch (NumberFormatException e) {
                System.out.print("N ");
            } catch (ArrayIndexOutOfBoundsException e) {
                System.out.print("O ");
            }
        }
    }
}
```

출력:

```text
3 Z N O
```

추적:

| i | arr[i] | 변환 | 24 / n | 출력 |
|---|---|---|---|---|
| 0 | "8" | 8 | 3 | 3 |
| 1 | "0" | 0 | 예외 | Z |
| 2 | "A" | 예외 | 실행 안 함 | N |
| 3 | 범위 초과 | 예외 | 실행 안 함 | O |

---

## 8. catch 순서

부모 예외 클래스인 `Exception`을 먼저 쓰면 뒤의 세부 예외 catch는 도달할 수 없다.

잘못된 코드:

```java
try {
    System.out.println(10 / 0);
} catch (Exception e) {
    System.out.println("E");
} catch (ArithmeticException e) {
    System.out.println("A");
}
```

이 코드는 컴파일 오류다.

이유:

```text
ArithmeticException은 Exception의 자식 클래스다.
Exception이 먼저 모든 예외를 잡아버리므로
뒤의 ArithmeticException catch는 실행될 가능성이 없다.
```

올바른 순서:

```java
try {
    System.out.println(10 / 0);
} catch (ArithmeticException e) {
    System.out.println("A");
} catch (Exception e) {
    System.out.println("E");
}
```

규칙:

```text
자식 예외 먼저
부모 예외 나중
```

---

## 9. Exception 하나로 잡기

실기 문제에서는 `Exception` 하나만 사용하는 코드도 자주 읽게 된다.

```java
class Main {
    public static void main(String[] args) {
        int result = 0;

        try {
            int[] arr = { 1, 2, 3 };
            result += arr[1];
            result += arr[3];
            result += 10;
        } catch (Exception e) {
            result += 100;
        }

        System.out.println(result);
    }
}
```

출력:

```text
102
```

추적:

```text
result = 0
arr[1]은 2 -> result = 2
arr[3]에서 예외 발생
result += 10은 실행되지 않음
catch로 이동 -> result += 100
result = 102
```

---

## 10. return과 finally

`return`이 있어도 `finally`는 실행된다.

```java
class Main {
    static int test() {
        try {
            System.out.println("A");
            return 10;
        } catch (Exception e) {
            System.out.println("B");
            return 20;
        } finally {
            System.out.println("C");
        }
    }

    public static void main(String[] args) {
        System.out.println(test());
    }
}
```

출력:

```text
A
C
10
```

흐름:

```text
try에서 A 출력
return 10을 만나 반환 준비
메서드가 끝나기 전에 finally 실행
C 출력
최종적으로 10 반환
main에서 10 출력
```

주의할 함정:

```java
class Main {
    static int test() {
        try {
            return 1;
        } finally {
            return 2;
        }
    }

    public static void main(String[] args) {
        System.out.println(test());
    }
}
```

출력:

```text
2
```

`finally`에서 `return`하면 try의 반환값을 덮어쓴다.

시험에서는 이런 코드를 읽어야 할 수 있지만, 실제 개발에서는 `finally` 안에서 `return`을 쓰지 않는 것이 좋다.

---

## 11. throw

`throw`는 예외를 직접 발생시킨다.

```java
class Main {
    static void check(int n) {
        if (n < 0) {
            throw new IllegalArgumentException();
        }
        System.out.println(n);
    }

    public static void main(String[] args) {
        try {
            check(3);
            check(-1);
            check(5);
        } catch (IllegalArgumentException e) {
            System.out.println("bad");
        }
    }
}
```

출력:

```text
3
bad
```

`check(-1)`에서 예외가 발생하므로 `check(5)`는 실행되지 않는다.

---

## 12. throws

`throws`는 이 메서드에서 예외가 발생할 수 있다고 선언하는 문법이다.

```java
class Main {
    static int div(int a, int b) throws ArithmeticException {
        return a / b;
    }

    public static void main(String[] args) {
        try {
            System.out.println(div(10, 2));
            System.out.println(div(10, 0));
        } catch (ArithmeticException e) {
            System.out.println("error");
        }
    }
}
```

출력:

```text
5
error
```

`throws`는 예외를 처리하는 코드가 아니다. 예외가 발생할 수 있음을 메서드 선언부에 표시하는 것이다.

---

## 13. 사용자 정의 예외

사용자 정의 예외는 보통 `Exception` 또는 `RuntimeException`을 상속해서 만든다.

```java
class ScoreException extends RuntimeException {
    ScoreException(String message) {
        super(message);
    }
}

class Main {
    static void checkScore(int score) {
        if (score < 0 || score > 100) {
            throw new ScoreException("score error");
        }
        System.out.println("score=" + score);
    }

    public static void main(String[] args) {
        try {
            checkScore(80);
            checkScore(120);
            checkScore(90);
        } catch (ScoreException e) {
            System.out.println(e.getMessage());
        }
    }
}
```

출력:

```text
score=80
score error
```

---

## 14. 클래스와 예외처리 혼합

```java
class Counter {
    int value;

    Counter(int value) {
        this.value = value;
    }

    int divide(int n) {
        return value / n;
    }
}

class Main {
    public static void main(String[] args) {
        Counter c = new Counter(20);
        int[] arr = { 5, 0, 4 };

        for (int i = 0; i < arr.length; i++) {
            try {
                System.out.print(c.divide(arr[i]) + " ");
            } catch (ArithmeticException e) {
                System.out.print("X ");
            }
        }
    }
}
```

출력:

```text
4 X 5
```

포인트:

```text
객체 c의 value는 20
c.divide(5) -> 20 / 5 -> 4
c.divide(0) -> 20 / 0 -> 예외
c.divide(4) -> 20 / 4 -> 5
```

---

## 15. 상속과 예외처리 혼합

```java
class Parent {
    int calc(int n) {
        return 10 / n;
    }
}

class Child extends Parent {
    int calc(int n) {
        return 20 / n;
    }
}

class Main {
    public static void main(String[] args) {
        Parent p = new Child();
        int[] nums = { 2, 0, 5 };

        for (int n : nums) {
            try {
                System.out.print(p.calc(n) + " ");
            } catch (Exception e) {
                System.out.print("E ");
            }
        }
    }
}
```

출력:

```text
10 E 4
```

핵심:

```text
Parent p = new Child();
참조 변수 타입은 Parent
실제 객체 타입은 Child
오버라이딩 메서드는 실제 객체 기준으로 실행
따라서 Child의 calc가 실행됨
```

---

## 16. static과 예외처리 혼합

```java
class Box {
    static int count = 0;
    int value;

    Box(int value) {
        this.value = value;
        count++;
    }

    int get(int n) {
        return value / n;
    }
}

class Main {
    public static void main(String[] args) {
        Box b1 = new Box(10);
        Box b2 = new Box(20);
        int sum = 0;

        try {
            sum += b1.get(2);
            sum += b2.get(0);
            sum += Box.count;
        } catch (Exception e) {
            sum += Box.count;
        }

        System.out.println(sum);
    }
}
```

출력:

```text
7
```

추적:

```text
b1 생성 -> count = 1
b2 생성 -> count = 2
sum += b1.get(2) -> 10 / 2 -> sum = 5
sum += b2.get(0) -> 예외 발생
sum += Box.count는 실행되지 않음
catch 실행 -> sum += 2
최종 sum = 7
```

---

## 17. enum, switch, 예외처리 혼합

```java
enum Grade {
    A, B, C
}

class Main {
    static int score(Grade g) {
        switch (g) {
            case A:
                return 100;
            case B:
                return 80;
            default:
                return 60;
        }
    }

    public static void main(String[] args) {
        String[] data = { "A", "D", "C" };
        int sum = 0;

        for (String s : data) {
            try {
                Grade g = Grade.valueOf(s);
                sum += score(g);
            } catch (IllegalArgumentException e) {
                sum += 10;
            }
        }

        System.out.println(sum);
    }
}
```

출력:

```text
170
```

추적:

```text
"A" -> Grade.A -> 100
"D" -> enum에 없음 -> IllegalArgumentException -> 10
"C" -> Grade.C -> default -> 60
합계 170
```

---

## 18. 실기 출력 추적 요령

예외처리 문제가 나오면 다음 순서로 손으로 표시한다.

```text
1. try 안에서 위에서 아래로 실행한다.
2. 예외가 발생하는 줄을 찾는다.
3. 예외 발생 줄 이후의 try 코드는 지운다.
4. 예외 타입에 맞는 catch를 찾는다.
5. finally가 있으면 무조건 실행한다.
6. 반복문 안에 try-catch가 있는지, try-catch 밖에 반복문이 있는지 구분한다.
7. static 변수와 객체 변수 값을 따로 추적한다.
8. 오버라이딩 메서드는 실제 객체 기준으로 실행한다.
```

특히 6번이 중요하다.

### 반복문 안에 try-catch가 있는 경우

```java
for (...) {
    try {
        ...
    } catch (...) {
        ...
    }
}
```

한 번 예외가 발생해도 다음 반복으로 넘어간다.

### try-catch 안에 반복문이 있는 경우

```java
try {
    for (...) {
        ...
    }
} catch (...) {
    ...
}
```

반복 중 예외가 한 번 발생하면 반복문 자체를 빠져나와 catch로 이동한다.

---

## 19. 비교 예제: try 위치에 따른 차이

### 코드 A

```java
class Main {
    public static void main(String[] args) {
        int[] arr = { 2, 0, 4 };

        for (int n : arr) {
            try {
                System.out.print(8 / n + " ");
            } catch (Exception e) {
                System.out.print("X ");
            }
        }
    }
}
```

출력:

```text
4 X 2
```

### 코드 B

```java
class Main {
    public static void main(String[] args) {
        int[] arr = { 2, 0, 4 };

        try {
            for (int n : arr) {
                System.out.print(8 / n + " ");
            }
        } catch (Exception e) {
            System.out.print("X ");
        }
    }
}
```

출력:

```text
4 X
```

코드 B에서는 `0`에서 예외가 발생하는 순간 반복문 전체가 중단된다. 따라서 `4`에 대한 계산은 하지 않는다.

---

## 20. 실전 문제 1

다음 코드의 출력 결과를 쓰시오.

```java
class Main {
    public static void main(String[] args) {
        int a = 0;

        try {
            a += 1;
            a += 10 / 0;
            a += 3;
        } catch (ArithmeticException e) {
            a += 5;
        } finally {
            a += 7;
        }

        System.out.println(a);
    }
}
```

정답:

```text
13
```

해설:

```text
a = 0
a += 1 -> a = 1
10 / 0 예외 발생
a += 3 실행 안 함
catch -> a += 5 -> a = 6
finally -> a += 7 -> a = 13
```

---

## 21. 실전 문제 2

다음 코드의 출력 결과를 쓰시오.

```java
class Main {
    static int f(int n) {
        try {
            return 12 / n;
        } catch (ArithmeticException e) {
            return -1;
        } finally {
            System.out.print("F ");
        }
    }

    public static void main(String[] args) {
        System.out.print(f(3) + " ");
        System.out.print(f(0) + " ");
    }
}
```

정답:

```text
F 4 F -1
```

해설:

```text
f(3)
12 / 3 = 4 반환 준비
finally에서 F 출력
main에서 4 출력

f(0)
12 / 0 예외 발생
catch에서 -1 반환 준비
finally에서 F 출력
main에서 -1 출력
```

---

## 22. 실전 문제 3

다음 코드의 출력 결과를 쓰시오.

```java
class Main {
    public static void main(String[] args) {
        String[] data = { "2", "A", "0", "4" };
        int sum = 0;

        for (String s : data) {
            try {
                int n = Integer.parseInt(s);
                sum += 8 / n;
            } catch (NumberFormatException e) {
                sum += 10;
            } catch (ArithmeticException e) {
                sum += 20;
            }
        }

        System.out.println(sum);
    }
}
```

정답:

```text
36
```

해설:

```text
"2" -> 8 / 2 = 4 -> sum = 4
"A" -> 숫자 변환 실패 -> sum += 10 -> sum = 14
"0" -> 8 / 0 예외 -> sum += 20 -> sum = 34
"4" -> 8 / 4 = 2 -> sum = 36
```

---

## 23. 실전 문제 4

다음 코드의 출력 결과를 쓰시오.

```java
class A {
    int x = 3;

    int calc(int n) {
        return x / n;
    }
}

class B extends A {
    int x = 10;

    int calc(int n) {
        return x / n;
    }
}

class Main {
    public static void main(String[] args) {
        A obj = new B();
        int result = 0;

        try {
            result += obj.calc(2);
            result += obj.calc(0);
            result += obj.x;
        } catch (Exception e) {
            result += obj.x;
        }

        System.out.println(result);
    }
}
```

정답:

```text
8
```

해설:

```text
obj.calc(2)는 오버라이딩 메서드이므로 B의 calc 실행
B의 x는 10 -> 10 / 2 = 5
result = 5

obj.calc(0) -> B의 x 10 / 0 -> 예외
result += obj.x는 실행되지 않음

필드 x는 참조 변수 타입 A 기준
obj.x는 A의 x인 3
catch에서 result += 3
최종 result = 8
```

시험 포인트:

```text
오버라이딩 메서드 -> 실제 객체 기준
필드 -> 참조 변수 타입 기준
```

---

## 24. 실전 문제 5

다음 코드의 출력 결과를 쓰시오.

```java
class Main {
    static int count = 0;

    static void add(String s) {
        try {
            count += Integer.parseInt(s);
        } catch (Exception e) {
            count++;
        } finally {
            count *= 2;
        }
    }

    public static void main(String[] args) {
        add("3");
        add("A");
        add("2");
        System.out.println(count);
    }
}
```

정답:

```text
32
```

해설:

```text
처음 count = 0

add("3")
count += 3 -> 3
finally -> count *= 2 -> 6

add("A")
parseInt 예외
catch -> count++ -> 7
finally -> count *= 2 -> 14

add("2")
count += 2 -> 16
finally -> count *= 2 -> 32
```

---

## 25. 실전 문제 6

다음 코드의 출력 결과를 쓰시오.

```java
class Main {
    static int test(int n) {
        try {
            if (n % 2 == 0) {
                throw new RuntimeException();
            }
            return n;
        } catch (RuntimeException e) {
            return n * 10;
        } finally {
            System.out.print(n + " ");
        }
    }

    public static void main(String[] args) {
        int sum = 0;
        for (int i = 1; i <= 3; i++) {
            sum += test(i);
        }
        System.out.println(sum);
    }
}
```

정답:

```text
1 2 3 24
```

해설:

```text
i = 1 -> 홀수 -> return 1, finally에서 1 출력
i = 2 -> 짝수 -> throw -> catch return 20, finally에서 2 출력
i = 3 -> 홀수 -> return 3, finally에서 3 출력
sum = 1 + 20 + 3 = 24
```

---

## 26. 실전 문제 7

다음 코드의 출력 결과를 쓰시오.

```java
enum State {
    READY(1), RUN(2), STOP(3);

    int code;

    State(int code) {
        this.code = code;
    }
}

class Main {
    public static void main(String[] args) {
        String[] input = { "READY", "ERROR", "STOP" };
        int result = 0;

        for (String s : input) {
            try {
                State st = State.valueOf(s);
                result += st.code;
            } catch (IllegalArgumentException e) {
                result += 10;
            }
        }

        System.out.println(result);
    }
}
```

정답:

```text
14
```

해설:

```text
"READY" -> code 1
"ERROR" -> enum 값 없음 -> 예외 -> 10
"STOP" -> code 3
result = 1 + 10 + 3 = 14
```

---

## 27. 실전 문제 8

다음 코드의 출력 결과를 쓰시오.

```java
class Main {
    public static void main(String[] args) {
        int[] arr = { 1, 0, 2 };
        int result = 0;

        try {
            for (int i = 0; i <= arr.length; i++) {
                result += 6 / arr[i];
            }
        } catch (ArithmeticException e) {
            result += 100;
        } catch (ArrayIndexOutOfBoundsException e) {
            result += 200;
        } finally {
            result += 300;
        }

        System.out.println(result);
    }
}
```

정답:

```text
406
```

해설:

```text
i = 0 -> arr[0] = 1 -> 6 / 1 = 6 -> result = 6
i = 1 -> arr[1] = 0 -> ArithmeticException
catch ArithmeticException -> result += 100 -> 106
finally -> result += 300 -> 406

예외가 발생해서 for문을 빠져나왔으므로
i = 2와 i = 3은 실행되지 않는다.
```

---

## 28. 실전 문제 9

다음 코드의 출력 결과를 쓰시오.

```java
class Main {
    static int f() {
        int x = 1;
        try {
            x += 2;
            return x;
        } finally {
            x += 3;
            System.out.print(x + " ");
        }
    }

    public static void main(String[] args) {
        System.out.println(f());
    }
}
```

정답:

```text
6 3
```

해설:

```text
x = 1
try에서 x += 2 -> x = 3
return x는 현재 값 3을 반환값으로 준비
finally 실행
x += 3 -> x = 6
6 출력
이미 준비된 반환값 3 반환
main에서 3 출력
```

---

## 29. 실전 문제 10

다음 코드의 출력 결과를 쓰시오.

```java
class Main {
    public static void main(String[] args) {
        String s = null;

        try {
            System.out.print("A ");
            System.out.print(s.length() + " ");
            System.out.print("B ");
        } catch (NullPointerException e) {
            System.out.print("C ");
        } catch (Exception e) {
            System.out.print("D ");
        } finally {
            System.out.print("E ");
        }

        System.out.print("F");
    }
}
```

정답:

```text
A C E F
```

---

## 30. 오늘의 암기보다 중요한 것

예외처리는 문법 이름을 외우는 것보다 실행 흐름을 추적하는 것이 중요하다.

다음 문장을 확실히 기억한다.

```text
예외가 발생한 줄에서 try의 정상 흐름은 끊긴다.
맞는 catch로 이동한다.
finally는 마지막에 실행된다.
반복문과 try-catch의 위치가 출력 결과를 바꾼다.
메서드는 실제 객체 기준, 필드는 참조 타입 기준이다.
static 변수는 모든 객체가 공유한다.
```

실기시험 코딩 문제를 풀 때는 머릿속으로만 계산하지 말고, 변수 표를 만들면서 한 줄씩 지워나가듯 추적한다.
