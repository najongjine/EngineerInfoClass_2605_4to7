# 4주차 5일차 - Python 종합 실전, 출력 예측, 변형 문제

## 오늘의 목표

오늘은 4주차 Python 마무리다. 단일 문법을 따로 보는 것이 아니라, 문자열, 리스트, 딕셔너리, 함수, 재귀, 컴프리헨션, lambda가 섞인 코드를 실기 문제처럼 추적한다. 최종 목표는 "처음 보는 Python 코드도 표를 그리며 끝까지 따라갈 수 있는 상태"다.

- Python 실기형 코드를 읽는 순서를 익힌다.
- 변수 추적표, 리스트 그림, 함수 호출 스택을 직접 작성한다.
- 짧은 문법을 일반 반복문으로 풀어 해석한다.
- 문제의 숫자, 조건, 반복 범위를 바꾼 변형 문제를 만들 수 있다.
- 혼자 복습할 수 있도록 오답 원인을 분류한다.

## 3시간 수업 구성

| 시간 | 내용 |
|---|---|
| 0:00 ~ 0:20 | Python 실기 문제 접근 순서 |
| 0:20 ~ 0:50 | 리스트/문자열 출력 예측 |
| 0:50 ~ 1:20 | 함수/재귀 출력 예측 |
| 1:20 ~ 1:30 | 쉬는 시간 |
| 1:30 ~ 2:00 | dict/set/comprehension/lambda 종합 |
| 2:00 ~ 2:35 | 변형 문제 만들기와 검증 |
| 2:35 ~ 3:00 | 미니 모의고사와 정답 해설 |

---

## 1. Python 실기 문제 접근 순서

시험장에서 Python 코드를 보면 이 순서로 본다.

```text
1. print가 몇 번 나오는지 표시한다.
2. def가 있으면 함수 호출 위치부터 찾는다.
3. 반복문의 range 끝 값이 포함되는지 확인한다.
4. 리스트/딕셔너리가 원본 변경인지 새 객체 생성인지 구분한다.
5. 컴프리헨션, map, filter, lambda는 일반 반복문으로 풀어 쓴다.
6. 재귀는 멈추는 조건과 return식을 먼저 찾는다.
7. 마지막에 출력 순서대로 답을 쓴다.
```

핵심 도구 3개:

```text
변수 추적표: 숫자와 문자열 값 추적
리스트 그림: 같은 리스트를 가리키는지 확인
호출 스택: 함수와 재귀의 호출/반환 순서 확인
```

---

## 2. 종합 예제 1 - 리스트와 문자열

```python
data = "3,1,4,1,5"
nums = []

for x in data.split(","):
    n = int(x)
    if n % 2 == 1:
        nums.append(n * 2)
    else:
        nums.append(n)

print(nums)
print(sum(nums))
```

단계:

```text
data.split(",") => ["3", "1", "4", "1", "5"]
```

추적표:

| x | n | 홀수? | 추가값 | nums |
|---|---:|---|---:|---|
| `"3"` | 3 | True | 6 | `[6]` |
| `"1"` | 1 | True | 2 | `[6, 2]` |
| `"4"` | 4 | False | 4 | `[6, 2, 4]` |
| `"1"` | 1 | True | 2 | `[6, 2, 4, 2]` |
| `"5"` | 5 | True | 10 | `[6, 2, 4, 2, 10]` |

정답:

```text
[6, 2, 4, 2, 10]
24
```

변형 연습:

```text
1. 조건을 n % 2 == 0으로 바꾸면?
2. nums.append(n * 2)를 nums.append(n + 2)로 바꾸면?
3. data를 "2,4,6"으로 바꾸면?
```

---

## 3. 종합 예제 2 - 참조와 복사

```python
a = [1, 2, 3]
b = a
c = a[:]

for i in range(len(a)):
    b[i] += i
    c[i] += b[i]

print(a)
print(b)
print(c)
```

관계 그림:

```text
a ----+
      v
b --> [1, 2, 3]

c --> [1, 2, 3]  별도 리스트
```

추적표:

| i | b[i] 변경 | a/b | c[i] 변경 | c |
|---:|---|---|---|---|
| 0 | `1 + 0 = 1` | `[1, 2, 3]` | `1 + 1 = 2` | `[2, 2, 3]` |
| 1 | `2 + 1 = 3` | `[1, 3, 3]` | `2 + 3 = 5` | `[2, 5, 3]` |
| 2 | `3 + 2 = 5` | `[1, 3, 5]` | `3 + 5 = 8` | `[2, 5, 8]` |

정답:

```text
[1, 3, 5]
[1, 3, 5]
[2, 5, 8]
```

---

## 4. 종합 예제 3 - 함수와 리스트

```python
def work(arr):
    total = 0
    for i in range(len(arr)):
        arr[i] += i
        total += arr[i]
    return total

data = [2, 2, 2]
result = work(data)

print(data)
print(result)
```

함수 안 추적:

| i | arr[i] 변경 | arr | total |
|---:|---|---|---:|
| 시작 | - | `[2, 2, 2]` | 0 |
| 0 | `2 + 0 = 2` | `[2, 2, 2]` | 2 |
| 1 | `2 + 1 = 3` | `[2, 3, 2]` | 5 |
| 2 | `2 + 2 = 4` | `[2, 3, 4]` | 9 |

정답:

```text
[2, 3, 4]
9
```

포인트:

```text
arr[i] += i는 리스트 내부를 바꾼다.
따라서 함수 밖 data도 바뀐다.
```

---

## 5. 종합 예제 4 - 재귀

```python
def f(n):
    if n <= 0:
        return 0
    if n % 2 == 0:
        return n + f(n - 1)
    return f(n - 1)

print(f(5))
```

의미:

```text
n이 짝수이면 더하고
n이 홀수이면 그냥 지나간다.
```

호출 추적:

```text
f(5) = f(4)
f(4) = 4 + f(3)
f(3) = f(2)
f(2) = 2 + f(1)
f(1) = f(0)
f(0) = 0
```

계산:

```text
f(1) = 0
f(2) = 2 + 0 = 2
f(3) = 2
f(4) = 4 + 2 = 6
f(5) = 6
```

정답:

```text
6
```

---

## 6. 종합 예제 5 - 딕셔너리와 정렬

```python
data = ["kim:80", "lee:90", "kim:70", "park:60"]
score = {}

for item in data:
    name, value = item.split(":")
    value = int(value)
    score[name] = score.get(name, 0) + value

result = sorted(score.items(), key=lambda x: x[1], reverse=True)

print(score)
print(result[0][0])
```

딕셔너리 추적:

| item | name | value | score |
|---|---|---:|---|
| `kim:80` | kim | 80 | `{"kim": 80}` |
| `lee:90` | lee | 90 | `{"kim": 80, "lee": 90}` |
| `kim:70` | kim | 70 | `{"kim": 150, "lee": 90}` |
| `park:60` | park | 60 | `{"kim": 150, "lee": 90, "park": 60}` |

`score.items()`:

```text
dict_items([('kim', 150), ('lee', 90), ('park', 60)])
```

정렬 기준:

```text
lambda x: x[1]
('kim', 150) -> 150
('lee', 90) -> 90
('park', 60) -> 60
```

정답:

```text
{'kim': 150, 'lee': 90, 'park': 60}
kim
```

---

## 7. 종합 예제 6 - 컴프리헨션과 join

```python
words = ["python", "java", "c", "sql"]
result = [w[0].upper() for w in words if len(w) >= 3]
print(result)
print("".join(result))
```

일반 반복문으로 풀기:

```python
result = []

for w in words:
    if len(w) >= 3:
        result.append(w[0].upper())
```

추적표:

| w | len(w) >= 3 | w[0].upper() | result |
|---|---|---|---|
| python | True | P | `["P"]` |
| java | True | J | `["P", "J"]` |
| c | False | - | `["P", "J"]` |
| sql | True | S | `["P", "J", "S"]` |

정답:

```text
['P', 'J', 'S']
PJS
```

---

## 8. 변형 문제 만드는 법

실기 대비는 기출을 그대로 외우는 것보다 변형을 많이 해보는 쪽이 강하다.

변형 포인트:

| 바꿀 부분 | 예시 |
|---|---|
| 숫자 | `[1, 2, 3]`을 `[2, 4, 6]`으로 변경 |
| 조건 | `x % 2 == 0`을 `x % 3 == 0`으로 변경 |
| 반복 범위 | `range(1, 5)`를 `range(0, 5, 2)`로 변경 |
| 누적 방식 | `+=`를 `*=` 또는 `-=`로 변경 |
| 슬라이싱 | `s[1:4]`를 `s[::2]`, `s[::-1]`로 변경 |
| 정렬 기준 | `x[1]`을 `len(x[0])`으로 변경 |

검증 순서:

```text
1. 먼저 손으로 답을 예측한다.
2. Python으로 실행한다.
3. 답이 다르면 추적표에서 어느 줄이 틀렸는지 표시한다.
4. 틀린 이유를 문법별로 분류한다.
```

오답 분류:

| 오답 유형 | 대표 원인 |
|---|---|
| 범위 실수 | `range` 끝 값 포함 착각 |
| 인덱스 실수 | 0번 시작, 음수 인덱스 착각 |
| 참조 실수 | `b = a`와 `b = a[:]` 혼동 |
| 함수 실수 | return 이후 코드 실행 착각 |
| 재귀 실수 | 호출 순서와 반환 순서 혼동 |
| 문자열 실수 | `split` 결과가 문자열임을 잊음 |

---

## 9. 미니 모의고사

### 문제 1

```python
s = "A1B2C3"
result = ""

for ch in s:
    if ch.isdigit():
        result += str(int(ch) * 2)
    else:
        result += ch.lower()

print(result)
```

### 문제 2

```python
a = [1, 2, 3, 4]
b = a
c = a[:]

b.pop()
c.append(5)
a[0] = 9

print(a)
print(b)
print(c)
```

### 문제 3

```python
def f(n):
    if n == 1:
        return 1
    return n * 2 + f(n - 1)

print(f(4))
```

### 문제 4

```python
data = ["A,3", "B,1", "C,2"]
result = sorted(data, key=lambda x: int(x.split(",")[1]))
print(result)
```

### 문제 5

```python
nums = [1, 2, 3, 4, 5]
result = [x * 10 if x % 2 == 0 else x for x in nums if x >= 2]
print(result)
```

### 문제 6

아래 조건을 만족하는 코드를 작성하시오.

- 문자열 `"kim:80|lee:90|park:70"`을 사용한다.
- 점수가 80 이상인 이름만 리스트에 담는다.
- 결과는 `["kim", "lee"]`가 출력되어야 한다.

---

## 10. 미니 모의고사 정답과 해설

### 문제 1 정답

```text
a2b4c6
```

문자는 소문자로 바꾸고, 숫자는 정수로 변환해 2배 한 뒤 다시 문자열로 붙인다.

추적:

| ch | 처리 | result |
|---|---|---|
| A | `a` | `a` |
| 1 | `2` | `a2` |
| B | `b` | `a2b` |
| 2 | `4` | `a2b4` |
| C | `c` | `a2b4c` |
| 3 | `6` | `a2b4c6` |

### 문제 2 정답

```text
[9, 2, 3]
[9, 2, 3]
[1, 2, 3, 4, 5]
```

`a`와 `b`는 같은 리스트다. `b.pop()`은 원본에서 마지막 4를 제거한다. `c`는 복사본이므로 `append(5)`가 원본에 영향을 주지 않는다.

### 문제 3 정답

```text
19
```

```text
f(1) = 1
f(2) = 2 * 2 + 1 = 5
f(3) = 3 * 2 + 5 = 11
f(4) = 4 * 2 + 11 = 19
```

### 문제 4 정답

```text
['B,1', 'C,2', 'A,3']
```

정렬 기준은 쉼표 뒤의 숫자다.

### 문제 5 정답

```text
[20, 3, 40, 5]
```

먼저 `if x >= 2`로 2, 3, 4, 5만 남긴다. 그 다음 짝수는 10배, 홀수는 그대로 둔다.

### 문제 6 예시 정답

```python
data = "kim:80|lee:90|park:70"
result = []

for item in data.split("|"):
    name, score = item.split(":")
    if int(score) >= 80:
        result.append(name)

print(result)
```

---

## 11. 4주차 Python 최종 요약

### 반드시 외워야 하는 차이

| 항목 | 핵심 |
|---|---|
| `/` | 실수 나눗셈 |
| `//` | 몫 |
| `%` | 나머지 |
| `range(a, b)` | a부터 b 직전까지 |
| `s[a:b]` | a부터 b 직전까지 |
| `b = a` | 같은 객체 참조 |
| `b = a[:]` | 얕은 복사 |
| `split` | 문자열을 리스트로 |
| `join` | 문자열 리스트를 문자열로 |
| `return` | 함수 종료와 값 반환 |
| `lambda` | 짧은 함수 |

### 시험장에서 쓸 Python 코드 추적 양식

```text
문제 번호:

1. print 위치:

2. 변수 초기값:

3. 반복 범위:

4. 리스트/딕셔너리 변화:

5. 함수 호출 순서:

6. 최종 출력:
```

### 마지막 체크 문제

아래 코드를 보고 출력 결과를 직접 표로 추적하시오.

```python
def solve(text):
    result = {}
    for item in text.split("|"):
        name, score = item.split(":")
        score = int(score)
        if score >= 80:
            result[name] = result.get(name, 0) + score
    return sorted(result.items(), key=lambda x: x[1])

print(solve("kim:80|lee:70|kim:90|park:85"))
```

정답:

```text
[('park', 85), ('kim', 170)]
```

해설:

```text
lee는 70점이라 제외된다.
kim은 80 + 90 = 170이다.
park는 85이다.
점수 기준 오름차순 정렬이므로 park가 먼저 나온다.
```

---

## 12. 다음 주 SQL로 넘어가기 전 연결 포인트

Python에서 딕셔너리와 리스트를 다루는 방식은 SQL 결과표를 이해할 때도 도움이 된다.

```text
Python 리스트 안 딕셔너리
[
  {"name": "kim", "score": 80},
  {"name": "lee", "score": 90}
]

SQL 테이블
name | score
kim  | 80
lee  | 90
```

다음 주 SQL에서는 이 데이터를 코드가 아니라 테이블로 보고, `SELECT`, `WHERE`, `GROUP BY`, `JOIN`으로 원하는 결과를 뽑는 연습을 한다.
