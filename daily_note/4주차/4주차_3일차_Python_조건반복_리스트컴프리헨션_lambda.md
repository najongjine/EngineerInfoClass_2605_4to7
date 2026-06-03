# 4주차 3일차 - 조건/반복 심화, 리스트 컴프리헨션, lambda

## 오늘의 목표

오늘은 Python다운 문법을 다룬다. 정보처리기사 실기에서 Python은 C/Java보다 코드가 짧게 나오는 경우가 많다. 특히 리스트 컴프리헨션, `lambda`, `map`, `filter`, `sorted`를 읽을 수 있어야 출력 예측 문제에서 당황하지 않는다.

- `for`, `while`, 중첩 반복문을 표로 추적할 수 있다.
- 리스트 컴프리헨션을 일반 반복문으로 풀어 쓸 수 있다.
- 조건이 붙은 컴프리헨션을 해석할 수 있다.
- `lambda`, `map`, `filter`, `sorted(key=...)`의 실행 결과를 예측할 수 있다.
- 짧은 Python 문법을 시험용 추적표로 바꾸는 습관을 만든다.

## 3시간 수업 구성

| 시간 | 내용 |
|---|---|
| 0:00 ~ 0:25 | for/while 복습과 중첩 반복 추적 |
| 0:25 ~ 0:55 | 리스트 컴프리헨션 기본 |
| 0:55 ~ 1:20 | 조건 포함 컴프리헨션 |
| 1:20 ~ 1:30 | 쉬는 시간 |
| 1:30 ~ 2:05 | lambda, map, filter |
| 2:05 ~ 2:35 | sorted와 key 함수 |
| 2:35 ~ 3:00 | 실기형 종합 문제 |

---

## 1. 반복문은 실행 횟수부터 잡는다

```python
total = 0

for i in range(1, 4):
    for j in range(1, 3):
        total += i * j

print(total)
```

중첩 반복문은 바깥 반복 1번마다 안쪽 반복이 전부 돈다.

```text
i = 1일 때 j = 1, 2
i = 2일 때 j = 1, 2
i = 3일 때 j = 1, 2
```

추적표:

| i | j | i * j | total |
|---:|---:|---:|---:|
| 1 | 1 | 1 | 1 |
| 1 | 2 | 2 | 3 |
| 2 | 1 | 2 | 5 |
| 2 | 2 | 4 | 9 |
| 3 | 1 | 3 | 12 |
| 3 | 2 | 6 | 18 |

출력:

```text
18
```

---

## 2. while문은 조건 변화가 핵심이다

```python
n = 10
count = 0

while n > 1:
    n //= 2
    count += 1

print(n)
print(count)
```

추적표:

| 반복 | 조건 n > 1 | n 변경 | count |
|---:|---|---:|---:|
| 시작 | - | 10 | 0 |
| 1 | True | 5 | 1 |
| 2 | True | 2 | 2 |
| 3 | True | 1 | 3 |
| 종료 | False | 1 | 3 |

출력:

```text
1
3
```

---

## 3. 리스트 컴프리헨션 기본

리스트 컴프리헨션은 리스트를 짧게 만드는 문법이다.

```python
a = [x * 2 for x in range(1, 5)]
print(a)
```

출력:

```text
[2, 4, 6, 8]
```

위 코드는 다음 코드와 같다.

```python
a = []

for x in range(1, 5):
    a.append(x * 2)

print(a)
```

해석 순서:

```text
[결과식 for 변수 in 반복대상]

[x * 2 for x in range(1, 5)]
         --------------------
         먼저 이 반복을 본다

x = 1 => x * 2 = 2
x = 2 => x * 2 = 4
x = 3 => x * 2 = 6
x = 4 => x * 2 = 8
```

---

## 4. 조건이 붙은 리스트 컴프리헨션

```python
a = [x for x in range(1, 8) if x % 2 == 0]
print(a)
```

출력:

```text
[2, 4, 6]
```

일반 반복문으로 풀면 다음과 같다.

```python
a = []

for x in range(1, 8):
    if x % 2 == 0:
        a.append(x)

print(a)
```

추적표:

| x | 조건 x % 2 == 0 | 추가 여부 |
|---:|---|---|
| 1 | False | 추가 안 함 |
| 2 | True | 2 |
| 3 | False | 추가 안 함 |
| 4 | True | 4 |
| 5 | False | 추가 안 함 |
| 6 | True | 6 |
| 7 | False | 추가 안 함 |

---

## 5. 결과식에 조건이 있는 경우

아래 문법은 위치가 다르다.

```python
a = ["even" if x % 2 == 0 else "odd" for x in range(1, 5)]
print(a)
```

출력:

```text
['odd', 'even', 'odd', 'even']
```

일반 반복문:

```python
a = []

for x in range(1, 5):
    if x % 2 == 0:
        a.append("even")
    else:
        a.append("odd")
```

비교:

| 문법 | 의미 |
|---|---|
| `[x for x in data if 조건]` | 조건을 만족하는 값만 남김 |
| `[A if 조건 else B for x in data]` | 모든 값을 돌면서 A 또는 B를 선택 |

---

## 6. 중첩 리스트 컴프리헨션

```python
a = [i * j for i in range(1, 4) for j in range(1, 3)]
print(a)
```

일반 반복문:

```python
a = []

for i in range(1, 4):
    for j in range(1, 3):
        a.append(i * j)
```

추적:

| i | j | i * j |
|---:|---:|---:|
| 1 | 1 | 1 |
| 1 | 2 | 2 |
| 2 | 1 | 2 |
| 2 | 2 | 4 |
| 3 | 1 | 3 |
| 3 | 2 | 6 |

출력:

```text
[1, 2, 2, 4, 3, 6]
```

---

## 7. lambda

`lambda`는 이름 없는 짧은 함수다.

```python
f = lambda x: x * 2
print(f(3))
```

출력:

```text
6
```

일반 함수로 쓰면 다음과 같다.

```python
def f(x):
    return x * 2
```

`lambda x: x * 2`는 다음처럼 읽는다.

```text
x를 받아서 x * 2를 반환하는 함수
```

---

## 8. map

`map`은 각 원소에 함수를 적용한다.

```python
a = [1, 2, 3]
b = list(map(lambda x: x * 2, a))
print(b)
```

흐름:

```text
1 -> lambda -> 2
2 -> lambda -> 4
3 -> lambda -> 6
```

출력:

```text
[2, 4, 6]
```

리스트 컴프리헨션으로 쓰면 다음과 같다.

```python
b = [x * 2 for x in a]
```

---

## 9. filter

`filter`는 조건을 만족하는 원소만 남긴다.

```python
a = [1, 2, 3, 4, 5]
b = list(filter(lambda x: x % 2 == 1, a))
print(b)
```

출력:

```text
[1, 3, 5]
```

흐름:

```text
1 -> True  -> 남김
2 -> False -> 버림
3 -> True  -> 남김
4 -> False -> 버림
5 -> True  -> 남김
```

컴프리헨션으로 쓰면 다음과 같다.

```python
b = [x for x in a if x % 2 == 1]
```

---

## 10. sorted와 key

`sorted`는 정렬된 새 리스트를 반환한다.

```python
a = [3, 1, 4, 2]
b = sorted(a)

print(a)
print(b)
```

출력:

```text
[3, 1, 4, 2]
[1, 2, 3, 4]
```

원본 `a`는 바뀌지 않는다.

`key`는 정렬 기준을 지정한다.

```python
words = ["apple", "kiwi", "banana"]
print(sorted(words, key=lambda x: len(x)))
```

출력:

```text
['kiwi', 'apple', 'banana']
```

정렬 기준표:

| 단어 | len(단어) |
|---|---:|
| apple | 5 |
| kiwi | 4 |
| banana | 6 |

길이가 짧은 순서로 정렬된다.

---

## 11. 튜플 정렬

실기에서 자주 나오는 형태다.

```python
data = [("kim", 80), ("lee", 90), ("park", 70)]
result = sorted(data, key=lambda x: x[1])
print(result)
```

`x`는 튜플 하나다.

```text
x = ("kim", 80)  -> x[1] = 80
x = ("lee", 90)  -> x[1] = 90
x = ("park", 70) -> x[1] = 70
```

출력:

```text
[('park', 70), ('kim', 80), ('lee', 90)]
```

내림차순:

```python
result = sorted(data, key=lambda x: x[1], reverse=True)
```

---

## 12. 실기형 예제 1

```python
a = [x * x for x in range(1, 6) if x % 2 == 1]
print(a)
```

추적:

| x | 홀수? | x * x | 추가 |
|---:|---|---:|---|
| 1 | True | 1 | O |
| 2 | False | 4 | X |
| 3 | True | 9 | O |
| 4 | False | 16 | X |
| 5 | True | 25 | O |

정답:

```text
[1, 9, 25]
```

---

## 13. 실기형 예제 2

```python
data = ["aa", "b", "cccc", "ddd"]
result = list(map(lambda x: len(x), filter(lambda x: len(x) >= 2, data)))
print(result)
```

단계별 해석:

```text
filter(lambda x: len(x) >= 2, data)
=> ["aa", "cccc", "ddd"]

map(lambda x: len(x), ...)
=> [2, 4, 3]
```

정답:

```text
[2, 4, 3]
```

---

## 14. 혼자 푸는 연습문제

### 문제 1

```python
a = [x + 1 for x in range(4)]
print(a)
```

### 문제 2

```python
a = [x for x in range(10) if x % 3 == 0]
print(a)
```

### 문제 3

```python
a = ["Y" if x > 2 else "N" for x in [1, 3, 2, 4]]
print(a)
```

### 문제 4

```python
f = lambda a, b: a * 2 + b
print(f(3, 4))
```

### 문제 5

```python
data = [("A", 3), ("B", 1), ("C", 2)]
print(sorted(data, key=lambda x: x[1], reverse=True))
```

### 문제 6

리스트 `[1, 2, 3, 4, 5]`에서 짝수는 제곱하고 홀수는 그대로 두어 `[1, 4, 3, 16, 5]`를 만드는 리스트 컴프리헨션을 작성하시오.

---

## 15. 정답과 해설

### 문제 1 정답

```text
[1, 2, 3, 4]
```

`range(4)`는 0, 1, 2, 3이다.

### 문제 2 정답

```text
[0, 3, 6, 9]
```

3으로 나누어 나머지가 0인 값만 남긴다.

### 문제 3 정답

```text
['N', 'Y', 'N', 'Y']
```

모든 원소를 돌면서 조건에 따라 `"Y"` 또는 `"N"`을 넣는다.

### 문제 4 정답

```text
10
```

`3 * 2 + 4 = 10`이다.

### 문제 5 정답

```text
[('A', 3), ('C', 2), ('B', 1)]
```

두 번째 값 기준 내림차순이다.

### 문제 6 예시 정답

```python
arr = [1, 2, 3, 4, 5]
result = [x * x if x % 2 == 0 else x for x in arr]
print(result)
```

---

## 오늘의 마무리 체크

- 컴프리헨션은 일반 반복문으로 풀어서 읽으면 쉽다.
- `[식 for 변수 in 대상 if 조건]`은 조건을 만족한 값만 추가한다.
- `[A if 조건 else B for 변수 in 대상]`은 모든 값을 돌며 A/B 중 하나를 선택한다.
- `lambda x: 식`은 x를 받아 식을 반환하는 짧은 함수다.
- `map`은 변환, `filter`는 선별이다.
- `sorted(..., key=lambda x: x[1])`은 정렬 기준을 직접 지정한다.
