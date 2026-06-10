# 4주차 보충 - Python tuple, set, dictionary

## 오늘의 목표

리스트까지 배웠다면 이제 Python에서 자주 같이 나오는 `tuple`, `set`, `dictionary`를 읽을 수 있어야 한다. 정보처리기사 실기에서는 긴 문법 설명보다 "값이 어떻게 저장되고 바뀌는가"를 묻는 문제가 많다.

- `tuple`은 순서가 있고 수정할 수 없는 자료구조임을 설명할 수 있다.
- `set`은 중복을 제거하고 집합 연산을 할 수 있음을 설명할 수 있다.
- `dictionary`는 key로 value를 찾는 자료구조임을 설명할 수 있다.
- 출력 예측 문제에서 자료구조의 변화를 표로 추적할 수 있다.

---

## 1. 리스트와 비교해서 보기

| 자료구조 | 예시 | 순서 | 중복 | 수정 |
|---|---|---|---|---|
| list | `[1, 2, 3]` | O | O | O |
| tuple | `(1, 2, 3)` | O | O | X |
| set | `{1, 2, 3}` | X | X | O |
| dictionary | `{"kim": 80}` | O | key 중복 X | O |

주의:

```text
set과 dictionary는 둘 다 { }를 사용한다.
빈 { }는 set이 아니라 dictionary다.
빈 set은 set()으로 만든다.
```

```python
a = {}
b = set()

print(type(a))
print(type(b))
```

출력:

```text
<class 'dict'>
<class 'set'>
```

---

## 2. tuple

튜플은 리스트처럼 인덱스로 값을 읽을 수 있지만, 한 번 만든 뒤 내부 값을 직접 바꿀 수 없다.

```python
t = (10, 20, 30)

print(t[0])
print(t[1:])
```

출력:

```text
10
(20, 30)
```

수정은 불가능하다.

```python
t = (10, 20, 30)
# t[0] = 99  # TypeError
```

### 튜플 언패킹

튜플은 여러 값을 한 번에 변수에 나누어 담을 때 자주 사용한다.

```python
student = ("kim", 80)
name, score = student

print(name)
print(score)
```

출력:

```text
kim
80
```

추적:

| 코드 | name | score |
|---|---|---|
| `student = ("kim", 80)` | - | - |
| `name, score = student` | `"kim"` | `80` |

### 원소가 1개인 튜플

원소가 1개인 튜플은 쉼표가 필요하다.

```python
a = (10)
b = (10,)

print(type(a))
print(type(b))
```

출력:

```text
<class 'int'>
<class 'tuple'>
```

---

## 3. set

set은 중복을 허용하지 않는다.

```python
a = [1, 2, 2, 3, 3, 3]
b = set(a)

print(b)
```

출력 예:

```text
{1, 2, 3}
```

set은 순서를 중요하게 보지 않는다. 시험에서 set 출력 순서가 애매하면 보통 핵심은 "중복 제거"다.

### set에 값 추가/삭제

```python
s = {1, 2, 3}

s.add(4)
s.remove(2)

print(s)
```

출력 예:

```text
{1, 3, 4}
```

### 집합 연산

```python
a = {1, 2, 3}
b = {3, 4, 5}

print(a & b)
print(a | b)
print(a - b)
```

| 연산 | 의미 | 결과 |
|---|---|---|
| `a & b` | 교집합 | `{3}` |
| `a | b` | 합집합 | `{1, 2, 3, 4, 5}` |
| `a - b` | 차집합 | `{1, 2}` |

---

## 4. dictionary

dictionary는 key와 value를 묶어서 저장한다.

```python
score = {"kim": 80, "lee": 90}

print(score["kim"])
```

출력:

```text
80
```

구조:

```text
key       value
kim   -> 80
lee   -> 90
```

### 값 추가와 변경

```python
score = {"kim": 80, "lee": 90}

score["park"] = 70
score["kim"] = 85

print(score)
```

출력:

```text
{'kim': 85, 'lee': 90, 'park': 70}
```

추적:

| 코드 | dictionary 상태 |
|---|---|
| `score = {"kim": 80, "lee": 90}` | `{"kim": 80, "lee": 90}` |
| `score["park"] = 70` | `{"kim": 80, "lee": 90, "park": 70}` |
| `score["kim"] = 85` | `{"kim": 85, "lee": 90, "park": 70}` |

### key가 있는지 확인

```python
score = {"kim": 80, "lee": 90}

if "kim" in score:
    print(score["kim"])

if "park" not in score:
    score["park"] = 0

print(score)
```

출력:

```text
80
{'kim': 80, 'lee': 90, 'park': 0}
```

### dictionary 반복

```python
score = {"kim": 80, "lee": 90}

for name in score:
    print(name, score[name])
```

출력:

```text
kim 80
lee 90
```

`items()`를 사용하면 key와 value를 같이 꺼낼 수 있다.

```python
score = {"kim": 80, "lee": 90}

for name, point in score.items():
    print(name, point)
```

출력:

```text
kim 80
lee 90
```

---

## 5. 실기형 예제 1 - tuple 정렬

```python
data = [("kim", 80), ("lee", 90), ("park", 70)]
result = sorted(data, key=lambda x: x[1])

print(result)
```

추적:

| x | x[0] | x[1] |
|---|---|---:|
| `("kim", 80)` | `"kim"` | 80 |
| `("lee", 90)` | `"lee"` | 90 |
| `("park", 70)` | `"park"` | 70 |

`x[1]`을 기준으로 오름차순 정렬한다.

출력:

```text
[('park', 70), ('kim', 80), ('lee', 90)]
```

---

## 6. 실기형 예제 2 - set 중복 제거

```python
data = ["A", "B", "A", "C", "B"]
result = set(data)

print(len(result))
```

추적:

```text
data에는 5개가 있지만 서로 다른 값은 A, B, C 3개다.
```

출력:

```text
3
```

---

## 7. 실기형 예제 3 - dictionary 누적

```python
data = ["kim:80", "lee:90", "kim:70"]
score = {}

for item in data:
    name, point = item.split(":")
    point = int(point)

    if name in score:
        score[name] += point
    else:
        score[name] = point

print(score)
```

추적:

| item | name | point | score |
|---|---|---:|---|
| `"kim:80"` | kim | 80 | `{"kim": 80}` |
| `"lee:90"` | lee | 90 | `{"kim": 80, "lee": 90}` |
| `"kim:70"` | kim | 70 | `{"kim": 150, "lee": 90}` |

출력:

```text
{'kim': 150, 'lee': 90}
```

---

## 8. 혼자 푸는 연습문제

### 문제 1

다음 코드의 출력 결과를 쓰시오.

```python
t = (3, 5, 7)
a, b, c = t

print(a + c)
```

### 문제 2

다음 코드의 출력 결과를 쓰시오.

```python
a = [1, 1, 2, 3, 3, 4]
b = set(a)

print(len(b))
```

### 문제 3

다음 코드의 출력 결과를 쓰시오.

```python
d = {"A": 2, "B": 3}
d["C"] = d["A"] + d["B"]
d["A"] = 10

print(d["C"])
print(d["A"])
```

### 문제 4

다음 코드의 출력 결과를 쓰시오.

```python
a = {1, 2, 3, 4}
b = {3, 4, 5}

print(a & b)
print(a - b)
```

### 문제 5

리스트 `["red", "blue", "red", "green", "blue"]`에서 중복을 제거한 색상의 개수를 출력하는 코드를 작성하시오.

---

## 9. 정답과 해설

### 문제 1 정답

```text
10
```

`a = 3`, `b = 5`, `c = 7`이므로 `a + c = 10`이다.

### 문제 2 정답

```text
4
```

중복을 제거하면 `{1, 2, 3, 4}`가 된다.

### 문제 3 정답

```text
5
10
```

`d["C"]`는 처음 계산될 때 `2 + 3 = 5`로 저장된다. 이후 `d["A"]`를 10으로 바꾸어도 `d["C"]`가 자동으로 다시 계산되지는 않는다.

### 문제 4 정답

```text
{3, 4}
{1, 2}
```

`a & b`는 공통 원소, `a - b`는 a에는 있지만 b에는 없는 원소다.

### 문제 5 예시 정답

```python
colors = ["red", "blue", "red", "green", "blue"]
unique_colors = set(colors)

print(len(unique_colors))
```

출력:

```text
3
```

---

## 마무리 체크

- tuple은 리스트처럼 순서가 있지만 값을 직접 수정할 수 없다.
- 원소가 1개인 tuple은 `(10,)`처럼 쉼표가 필요하다.
- set은 중복 제거와 교집합, 합집합, 차집합에 자주 사용한다.
- 빈 set은 `{}`가 아니라 `set()`으로 만든다.
- dictionary는 key로 value를 찾는다.
- dictionary에서 같은 key에 다시 대입하면 기존 value가 바뀐다.
