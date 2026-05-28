# 3주차 3일차 - 생성자, this, 객체 배열

## 오늘의 목표

오늘은 객체가 만들어지는 순간을 다룬다. 생성자와 `this`는 실기 Java 문제에서 자주 섞여 나온다. 특히 필드와 매개변수 이름이 같을 때 어떤 값이 바뀌는지 구분해야 한다.

- 생성자가 언제 실행되는지 설명할 수 있다.
- `this`가 현재 객체를 의미한다는 것을 이해한다.
- 객체 배열을 만들고 각 원소가 객체 참조라는 점을 추적할 수 있다.
- 생성자 호출 순서와 필드 변경 결과를 예측할 수 있다.

## 3시간 수업 구성

| 시간 | 내용 |
|---|---|
| 0:00 ~ 0:25 | 생성자 기본 |
| 0:25 ~ 0:55 | this와 이름 충돌 |
| 0:55 ~ 1:20 | 생성자 오버로딩 |
| 1:20 ~ 1:30 | 쉬는 시간 |
| 1:30 ~ 2:10 | 객체 배열과 참조 |
| 2:10 ~ 2:40 | 실기형 생성자 추적 |
| 2:40 ~ 3:00 | 연습 문제 풀이 |

---

## 1. 생성자란 무엇인가

생성자는 객체가 만들어질 때 자동으로 실행되는 특별한 메서드다.

```java
class Person {
    String name;
    int age;

    Person() {
        name = "Unknown";
        age = 0;
    }
}

class Main {
    public static void main(String[] args) {
        Person p = new Person();
        System.out.println(p.name);
        System.out.println(p.age);
    }
}
```

출력:

```text
Unknown
0
```

### 생성자의 특징

| 특징 | 설명 |
|---|---|
| 이름 | 클래스 이름과 같아야 한다 |
| 반환형 | `void`도 쓰지 않는다 |
| 실행 시점 | `new 클래스명(...)` 때 자동 실행 |
| 역할 | 필드 초기화 |

흐름:

```mermaid
flowchart TD
    A[new Person()] --> B[메모리에 Person 객체 생성]
    B --> C[Person 생성자 실행]
    C --> D[name = Unknown]
    D --> E[age = 0]
    E --> F[p가 객체를 참조]
```

---

## 2. 매개변수가 있는 생성자

```java
class Person {
    String name;
    int age;

    Person(String n, int a) {
        name = n;
        age = a;
    }
}

class Main {
    public static void main(String[] args) {
        Person p = new Person("Lee", 20);
        System.out.println(p.name);
        System.out.println(p.age);
    }
}
```

출력:

```text
Lee
20
```

상태 변화:

```text
new Person("Lee", 20)

생성자 안:
n = "Lee"
a = 20
name = n  -> p.name = "Lee"
age = a   -> p.age = 20
```

---

## 3. this의 의미

`this`는 “현재 객체 자신”을 뜻한다.

```java
class Person {
    String name;
    int age;

    Person(String name, int age) {
        this.name = name;
        this.age = age;
    }
}
```

여기서 왼쪽 `this.name`은 필드, 오른쪽 `name`은 매개변수다.

```text
this.name = name
     |       |
     |       +-- 생성자로 들어온 매개변수
     +---------- 현재 객체의 필드
```

### this가 없으면?

```java
class Person {
    String name;

    Person(String name) {
        name = name;
    }
}
```

이 코드는 필드가 바뀌지 않는다. 양쪽 `name`이 모두 매개변수로 해석되기 때문이다.

```java
class Main {
    public static void main(String[] args) {
        Person p = new Person("Kim");
        System.out.println(p.name);
    }
}
```

출력:

```text
null
```

`String` 필드의 기본값은 `null`이다.

---

## 4. 기본값

객체의 필드는 값을 직접 넣지 않아도 기본값이 들어간다.

| 자료형 | 필드 기본값 |
|---|---|
| `int` | `0` |
| `double` | `0.0` |
| `boolean` | `false` |
| `char` | `\u0000` |
| 참조형 | `null` |

지역 변수는 다르다. 지역 변수는 직접 초기화하지 않으면 사용할 수 없다.

```java
class Main {
    public static void main(String[] args) {
        int x;
        // System.out.println(x); // 컴파일 오류
    }
}
```

---

## 5. 생성자 오버로딩

오버로딩은 같은 이름의 메서드나 생성자를 매개변수 형태가 다르게 여러 개 만드는 것이다.

```java
class Member {
    String name;
    int point;

    Member() {
        this.name = "guest";
        this.point = 0;
    }

    Member(String name) {
        this.name = name;
        this.point = 10;
    }

    Member(String name, int point) {
        this.name = name;
        this.point = point;
    }
}

class Main {
    public static void main(String[] args) {
        Member a = new Member();
        Member b = new Member("Kim");
        Member c = new Member("Lee", 50);

        System.out.println(a.name + ":" + a.point);
        System.out.println(b.name + ":" + b.point);
        System.out.println(c.name + ":" + c.point);
    }
}
```

출력:

```text
guest:0
Kim:10
Lee:50
```

어떤 생성자가 실행되는지는 괄호 안 인자의 개수와 자료형으로 결정된다.

---

## 6. 객체 배열

배열에는 기본형 값뿐 아니라 객체 참조도 들어갈 수 있다.

```java
class Student {
    String name;
    int score;

    Student(String name, int score) {
        this.name = name;
        this.score = score;
    }
}

class Main {
    public static void main(String[] args) {
        Student[] arr = new Student[3];

        arr[0] = new Student("Kim", 80);
        arr[1] = new Student("Lee", 90);
        arr[2] = new Student("Park", 70);

        System.out.println(arr[1].name);
        System.out.println(arr[1].score);
    }
}
```

출력:

```text
Lee
90
```

그림:

```text
arr
+-----+-----+-----+
| [0] | [1] | [2] |
+--|--+--|--+--|--+
   |     |     |
   v     v     v
 Kim   Lee   Park
 80    90    70
```

주의:

```java
Student[] arr = new Student[3];
System.out.println(arr[0].score);
```

위 코드는 오류가 난다. `arr[0]`에는 아직 객체가 없고 기본값 `null`이 들어 있기 때문이다.

```text
arr[0] = null
null.score 접근 시도 -> NullPointerException
```

여기서도 “포인터가 완전히 사라졌다”가 아니라 “null 참조를 따라가면 오류가 난다”고 이해해야 한다.

---

## 7. 객체 배열 반복

```java
class Student {
    String name;
    int score;

    Student(String name, int score) {
        this.name = name;
        this.score = score;
    }
}

class Main {
    public static void main(String[] args) {
        Student[] arr = {
            new Student("Kim", 80),
            new Student("Lee", 90),
            new Student("Park", 70)
        };

        int sum = 0;

        for (int i = 0; i < arr.length; i++) {
            sum += arr[i].score;
        }

        System.out.println(sum);
    }
}
```

출력:

```text
240
```

상태표:

| i | arr[i].name | arr[i].score | sum |
|---:|---|---:|---:|
| 0 | Kim | 80 | 80 |
| 1 | Lee | 90 | 170 |
| 2 | Park | 70 | 240 |

---

## 8. 실전 실기형 예제 1

다음 코드의 출력 결과를 쓰시오.

```java
class A {
    int x;

    A(int x) {
        x = x + 1;
    }
}

class Main {
    public static void main(String[] args) {
        A a = new A(10);
        System.out.println(a.x);
    }
}
```

정답:

```text
0
```

생성자의 `x = x + 1`은 매개변수 `x`만 바꾼다. 필드 `x`는 건드리지 않았으므로 기본값 `0`이다.

---

## 9. 실전 실기형 예제 2

다음 코드의 출력 결과를 쓰시오.

```java
class A {
    int x;

    A(int x) {
        this.x = x + 1;
    }
}

class Main {
    public static void main(String[] args) {
        A a = new A(10);
        System.out.println(a.x);
    }
}
```

정답:

```text
11
```

`this.x`가 필드이므로 객체의 `x`에 `11`이 저장된다.

---

## 10. 실전 실기형 예제 3

다음 코드의 출력 결과를 쓰시오.

```java
class Box {
    int n;

    Box(int n) {
        this.n = n;
    }
}

class Main {
    public static void main(String[] args) {
        Box[] boxes = new Box[2];
        boxes[0] = new Box(3);
        boxes[1] = boxes[0];

        boxes[1].n = 8;

        System.out.println(boxes[0].n);
        System.out.println(boxes[1].n);
    }
}
```

정답:

```text
8
8
```

`boxes[1] = boxes[0]` 때문에 두 칸이 같은 객체를 가리킨다.

---

## 11. 오늘의 혼자 연습 문제

### 문제 1

다음 코드의 출력 결과를 쓰시오.

```java
class User {
    String id;
    int level;

    User(String id) {
        this.id = id;
        level = 1;
    }

    User(String id, int level) {
        this.id = id;
        this.level = level;
    }
}

class Main {
    public static void main(String[] args) {
        User a = new User("kim");
        User b = new User("lee", 3);

        System.out.println(a.id + ":" + a.level);
        System.out.println(b.id + ":" + b.level);
    }
}
```

### 문제 2

다음 코드의 출력 결과를 쓰시오.

```java
class Data {
    int x;

    Data(int x) {
        x = x * 2;
    }
}

class Main {
    public static void main(String[] args) {
        Data d = new Data(5);
        System.out.println(d.x);
    }
}
```

### 문제 3

다음 코드의 출력 결과를 쓰시오.

```java
class Data {
    int x;

    Data(int x) {
        this.x = x * 2;
    }
}

class Main {
    public static void main(String[] args) {
        Data d = new Data(5);
        System.out.println(d.x);
    }
}
```

### 문제 4

다음 코드의 출력 결과를 쓰시오.

```java
class Score {
    int value;

    Score(int value) {
        this.value = value;
    }
}

class Main {
    public static void main(String[] args) {
        Score[] arr = {
            new Score(10),
            new Score(20),
            new Score(30)
        };

        arr[0] = arr[2];
        arr[0].value += 5;

        System.out.println(arr[2].value);
    }
}
```

### 문제 5

`Book` 클래스를 만들고 제목과 가격을 생성자로 초기화하시오. `Book` 객체 3개를 배열에 넣고 총 가격을 출력하는 코드를 작성하시오.

---

## 12. 정답과 해설

### 문제 1 정답

```text
kim:1
lee:3
```

인자 1개 생성자와 인자 2개 생성자가 각각 호출된다.

### 문제 2 정답

```text
0
```

`x = x * 2`는 매개변수 `x`만 바꾸며 필드는 기본값 0이다.

### 문제 3 정답

```text
10
```

`this.x`가 필드다.

### 문제 4 정답

```text
35
```

`arr[0] = arr[2]` 후 `arr[0]`과 `arr[2]`는 같은 객체다.

### 문제 5 예시 정답

```java
class Book {
    String title;
    int price;

    Book(String title, int price) {
        this.title = title;
        this.price = price;
    }
}

class Main {
    public static void main(String[] args) {
        Book[] books = {
            new Book("A", 10000),
            new Book("B", 12000),
            new Book("C", 8000)
        };

        int total = 0;
        for (int i = 0; i < books.length; i++) {
            total += books[i].price;
        }

        System.out.println(total);
    }
}
```

---

## 오늘의 마무리 체크

- 생성자는 `new` 할 때 자동 실행된다.
- 생성자는 클래스 이름과 같고 반환형이 없다.
- `this`는 현재 객체 자신이다.
- 필드와 매개변수 이름이 같으면 `this.필드명`으로 구분한다.
- 객체 배열의 각 칸에는 객체 자체가 아니라 참조가 들어간다.
- `null` 참조에 `.`으로 접근하면 오류가 난다.
