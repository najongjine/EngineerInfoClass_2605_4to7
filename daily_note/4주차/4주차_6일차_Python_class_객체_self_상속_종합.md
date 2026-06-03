# 4주차 6일차 - Python class, 객체, self, 상속, 종합 실전

## 오늘의 목표

Python에도 `class`가 있다. 정보처리기사 실기에서 Python 클래스 문제가 아주 길게 나오지는 않더라도, 객체 생성 순서, `self`, 인스턴스 변수, 클래스 변수, 상속, 오버라이딩은 Java 문제와 비슷한 방식으로 출제될 수 있다.

오늘의 핵심은 "객체가 어디에 만들어지고, 변수 이름이 어떤 객체를 가리키며, 메서드 호출 시 어떤 값이 바뀌는가"를 추적하는 것이다.

- Python 클래스와 객체의 기본 구조를 읽을 수 있다.
- `__init__` 생성자가 언제 실행되는지 설명할 수 있다.
- `self`가 현재 객체 자신을 뜻한다는 것을 이해한다.
- 인스턴스 변수와 클래스 변수를 구분할 수 있다.
- 객체 참조와 리스트 참조의 공통점을 설명할 수 있다.
- 상속과 메서드 오버라이딩의 출력 결과를 예측할 수 있다.

## 3시간 수업 구성

| 시간 | 내용 |
|---|---|
| 0:00 ~ 0:25 | class와 객체 기본 구조 |
| 0:25 ~ 0:55 | `__init__`, `self`, 인스턴스 변수 |
| 0:55 ~ 1:20 | 객체 참조와 값 변경 추적 |
| 1:20 ~ 1:30 | 쉬는 시간 |
| 1:30 ~ 2:00 | 클래스 변수와 인스턴스 변수 |
| 2:00 ~ 2:30 | 상속, `super`, 오버라이딩 |
| 2:30 ~ 3:00 | 실기형 출력 예측 문제 |

---

## 1. class는 객체를 만들기 위한 설계도다

클래스는 객체를 만들기 위한 설계도다.

```python
class Student:
    pass

s1 = Student()
s2 = Student()

print(type(s1))
print(s1 == s2)
```

출력 예:

```text
<class '__main__.Student'>
False
```

`s1`과 `s2`는 같은 `Student` 클래스로 만든 객체지만, 서로 다른 객체다.

그림:

```text
Student 클래스
    |
    +-- s1 객체
    |
    +-- s2 객체

s1과 s2는 따로 만들어진다.
```

Java와 비교:

| Java | Python |
|---|---|
| `class Student { }` | `class Student:` |
| `new Student()` | `Student()` |
| 생성자 이름이 클래스명 | 생성자는 `__init__` |
| `this` | `self` |

---

## 2. `__init__`은 객체 생성 시 자동 실행된다

```python
class Student:
    def __init__(self):
        print("init")

s = Student()
print("end")
```

출력:

```text
init
end
```

실행 흐름:

```mermaid
flowchart TD
    A[Student 클래스 정의] --> B[s = Student()]
    B --> C[새 객체 생성]
    C --> D[__init__ 자동 호출]
    D --> E[print init]
    E --> F[객체를 s에 저장]
    F --> G[print end]
```

중요:

```text
__init__은 객체가 만들어질 때 자동 실행된다.
직접 s.__init__()처럼 부르는 용도가 아니다.
```

---

## 3. self는 현재 객체 자신이다

```python
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_info(self):
        print(self.name, self.score)

s1 = Student("kim", 80)
s2 = Student("lee", 90)

s1.print_info()
s2.print_info()
```

출력:

```text
kim 80
lee 90
```

객체 그림:

```text
s1 --> Student 객체
       name = "kim"
       score = 80

s2 --> Student 객체
       name = "lee"
       score = 90
```

`s1.print_info()`를 호출하면 Python은 내부적으로 다음처럼 생각하면 된다.

```text
Student.print_info(s1)
```

그래서 `print_info(self)`의 `self`는 `s1`이 된다. `s2.print_info()`를 호출하면 `self`는 `s2`가 된다.

---

## 4. 인스턴스 변수

`self.name`, `self.score`처럼 객체마다 따로 가지는 변수를 인스턴스 변수라고 한다.

```python
class Box:
    def __init__(self, value):
        self.value = value

    def add(self, n):
        self.value += n

a = Box(10)
b = Box(20)

a.add(5)
b.add(1)

print(a.value)
print(b.value)
```

추적표:

| 실행 | a.value | b.value |
|---|---:|---:|
| `a = Box(10)` | 10 | - |
| `b = Box(20)` | 10 | 20 |
| `a.add(5)` | 15 | 20 |
| `b.add(1)` | 15 | 21 |

출력:

```text
15
21
```

`a`와 `b`는 서로 다른 객체이므로 값이 따로 바뀐다.

---

## 5. 객체 참조

리스트에서 `b = a`를 하면 같은 리스트를 가리켰다. 객체도 같다.

```python
class Box:
    def __init__(self, value):
        self.value = value

a = Box(10)
b = a

b.value = 99

print(a.value)
print(b.value)
```

출력:

```text
99
99
```

그림:

```text
a ----+
      v
b --> Box 객체
      value = 99
```

`b = a`는 객체를 복사하는 것이 아니다. 같은 객체를 같이 가리키게 만든다.

비교:

```text
리스트: b = a  -> 같은 리스트
객체:   b = a  -> 같은 객체
```

---

## 6. 클래스 변수

클래스 변수는 객체마다 따로 있는 값이 아니라 클래스가 공유하는 값이다.

```python
class Counter:
    total = 0

    def __init__(self):
        Counter.total += 1
        self.count = 1

a = Counter()
b = Counter()
c = Counter()

print(Counter.total)
print(a.count)
print(b.count)
```

출력:

```text
3
1
1
```

구조:

```text
Counter 클래스 공유 공간
total = 3

a 객체: count = 1
b 객체: count = 1
c 객체: count = 1
```

Java의 `static` 변수와 비슷하게 생각하면 된다.

---

## 7. 클래스 변수와 인스턴스 변수 이름이 같을 때

이 부분은 실기에서 함정이 되기 좋다.

```python
class Test:
    x = 10

a = Test()
b = Test()

a.x = 20

print(Test.x)
print(a.x)
print(b.x)
```

출력:

```text
10
20
10
```

왜 그럴까?

```text
Test.x는 클래스 변수다.
a.x = 20을 실행하면 a 객체 안에 x라는 인스턴스 변수가 새로 생긴다.
b에는 인스턴스 변수 x가 없으므로 클래스 변수 Test.x를 찾아간다.
```

그림:

```text
Test 클래스
  x = 10

a 객체
  x = 20

b 객체
  x 없음 -> Test.x 사용 -> 10
```

---

## 8. 메서드에서 클래스 변수 변경

```python
class Count:
    total = 0

    def __init__(self):
        Count.total += 1
        self.num = 0

    def add(self):
        Count.total += 1
        self.num += 1

a = Count()
b = Count()

a.add()
b.add()
b.add()

print(Count.total)
print(a.num)
print(b.num)
```

추적표:

| 실행 | Count.total | a.num | b.num |
|---|---:|---:|---:|
| `a = Count()` | 1 | 0 | - |
| `b = Count()` | 2 | 0 | 0 |
| `a.add()` | 3 | 1 | 0 |
| `b.add()` | 4 | 1 | 1 |
| `b.add()` | 5 | 1 | 2 |

출력:

```text
5
1
2
```

---

## 9. 상속

상속은 부모 클래스의 기능을 자식 클래스가 물려받는 것이다.

```python
class Animal:
    def sound(self):
        print("Animal")

class Dog(Animal):
    pass

d = Dog()
d.sound()
```

출력:

```text
Animal
```

`Dog` 안에 `sound`가 없어도 부모 `Animal`에서 찾아 실행한다.

```text
Dog 객체
  Dog 클래스에서 sound 찾기
  없으면 Animal 클래스에서 sound 찾기
```

---

## 10. 오버라이딩

자식 클래스가 부모의 메서드를 다시 정의하면 오버라이딩이다.

```python
class Animal:
    def sound(self):
        print("Animal")

class Dog(Animal):
    def sound(self):
        print("Dog")

a = Animal()
d = Dog()

a.sound()
d.sound()
```

출력:

```text
Animal
Dog
```

`Dog` 객체에서 `sound`를 호출하면 `Dog` 클래스의 `sound`가 먼저 실행된다.

---

## 11. super

`super()`는 부모 클래스의 메서드를 호출할 때 쓴다.

```python
class Parent:
    def __init__(self):
        print("Parent init")

    def show(self):
        print("Parent")

class Child(Parent):
    def __init__(self):
        super().__init__()
        print("Child init")

    def show(self):
        print("Child")
        super().show()

c = Child()
c.show()
```

출력:

```text
Parent init
Child init
Child
Parent
```

실행 흐름:

```text
c = Child()
=> Child.__init__ 실행
=> super().__init__으로 Parent.__init__ 실행
=> Parent init 출력
=> Child init 출력

c.show()
=> Child.show 실행
=> Child 출력
=> super().show()로 Parent.show 실행
=> Parent 출력
```

---

## 12. 다형성 느낌 잡기

Python은 Java처럼 변수 타입을 앞에 쓰지 않는다. 그래도 실제 객체의 메서드가 실행된다는 점은 비슷하다.

```python
class A:
    def f(self):
        print("A")

class B(A):
    def f(self):
        print("B")

items = [A(), B(), A()]

for item in items:
    item.f()
```

출력:

```text
A
B
A
```

각 리스트 원소가 실제로 어떤 객체인지에 따라 실행되는 메서드가 달라진다.

---

## 13. 실기형 예제 1

다음 코드의 출력 결과를 예측하시오.

```python
class Person:
    def __init__(self, name):
        self.name = name

    def change(self, name):
        self.name = name

p1 = Person("kim")
p2 = p1
p2.change("lee")

print(p1.name)
print(p2.name)
```

정답:

```text
lee
lee
```

해설:

```text
p2 = p1이므로 p1과 p2는 같은 객체를 가리킨다.
p2.change("lee")는 같은 객체의 name을 "lee"로 바꾼다.
```

---

## 14. 실기형 예제 2

```python
class A:
    x = 1

    def __init__(self):
        self.y = 2

a = A()
b = A()

a.x = 10
b.y = 20

print(A.x)
print(a.x)
print(a.y)
print(b.x)
print(b.y)
```

정답:

```text
1
10
2
1
20
```

해설:

```text
A.x는 클래스 변수 1이다.
a.x = 10은 a 객체에 인스턴스 변수 x를 새로 만든다.
b에는 x가 없으므로 A.x인 1을 사용한다.
y는 __init__에서 객체마다 만들어지는 인스턴스 변수다.
```

---

## 15. 실기형 예제 3

```python
class Parent:
    def __init__(self):
        print("P")

    def call(self):
        print("Parent")

class Child(Parent):
    def __init__(self):
        super().__init__()
        print("C")

    def call(self):
        print("Child")

obj = Child()
obj.call()
```

정답:

```text
P
C
Child
```

`Child()` 생성 시 `Child.__init__`이 실행되고, 그 안에서 `super().__init__()`이 부모 생성자를 호출한다.

---

## 16. 혼자 푸는 연습문제

### 문제 1

```python
class Box:
    def __init__(self, value):
        self.value = value

    def add(self, n):
        self.value += n

b = Box(5)
b.add(3)
b.add(2)
print(b.value)
```

### 문제 2

```python
class Test:
    total = 0

    def __init__(self):
        Test.total += 1

a = Test()
b = Test()

print(Test.total)
```

### 문제 3

```python
class Data:
    def __init__(self, n):
        self.n = n

x = Data(1)
y = Data(2)
z = x

z.n = 5
y.n += z.n

print(x.n)
print(y.n)
print(z.n)
```

### 문제 4

```python
class A:
    def f(self):
        print("A")

class B(A):
    def f(self):
        print("B")

class C(B):
    pass

items = [A(), B(), C()]

for item in items:
    item.f()
```

### 문제 5

```python
class Parent:
    def show(self):
        print("P")

class Child(Parent):
    def show(self):
        super().show()
        print("C")

c = Child()
c.show()
```

### 문제 6

아래 조건을 만족하는 클래스를 작성하시오.

- `Score` 클래스를 만든다.
- 생성자에서 `name`, `score`를 저장한다.
- `is_pass()` 메서드는 점수가 60 이상이면 `True`, 아니면 `False`를 반환한다.
- `Score("kim", 80)` 객체를 만들고 `is_pass()` 결과를 출력한다.

---

## 17. 정답과 해설

### 문제 1 정답

```text
10
```

처음 5에서 3을 더해 8, 다시 2를 더해 10이다.

### 문제 2 정답

```text
2
```

객체가 두 번 생성되어 `__init__`이 두 번 실행된다. 클래스 변수 `Test.total`이 2가 된다.

### 문제 3 정답

```text
5
7
5
```

`z = x`이므로 `z`와 `x`는 같은 객체다. `z.n = 5`는 `x.n`도 5가 되게 한다. `y.n += z.n`은 2 + 5 = 7이다.

### 문제 4 정답

```text
A
B
B
```

`C`는 `B`를 상속받고 `f`를 따로 정의하지 않았으므로 `B.f`가 실행된다.

### 문제 5 정답

```text
P
C
```

`Child.show` 안에서 `super().show()`가 먼저 실행되어 `P`가 출력되고, 그 다음 `C`가 출력된다.

### 문제 6 예시 정답

```python
class Score:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def is_pass(self):
        return self.score >= 60

s = Score("kim", 80)
print(s.is_pass())
```

출력:

```text
True
```

---

## 18. Python class 최종 요약

| 문법 | 의미 |
|---|---|
| `class A:` | A 클래스 정의 |
| `A()` | A 객체 생성 |
| `__init__` | 객체 생성 시 자동 실행되는 생성자 |
| `self` | 현재 객체 자신 |
| `self.x` | 객체마다 따로 가지는 인스턴스 변수 |
| `A.x` | 클래스가 공유하는 클래스 변수 |
| `class B(A):` | B가 A를 상속 |
| `super()` | 부모 클래스 메서드 호출 |

시험에서 class 문제를 풀 때 순서:

```text
1. 객체가 몇 개 생성되는지 센다.
2. __init__이 몇 번 실행되는지 표시한다.
3. self.변수는 객체별로 따로 적는다.
4. 클래스 변수는 클래스 이름 옆에 따로 적는다.
5. b = a 같은 대입은 같은 객체를 가리키는지 확인한다.
6. 메서드가 오버라이딩되었는지 확인한다.
7. super()가 있으면 부모 메서드 호출 위치를 표시한다.
```

Java 주차에서 배운 생성자, 객체 참조, 상속, 오버라이딩과 연결해서 보면 Python 클래스도 어렵지 않다. 문법 모양만 다르고, "객체를 만들고 그 객체 안의 값을 바꾼다"는 핵심은 같다.
