# 4주차 2일차 - 문자열, 슬라이싱, split, join, replace

## 오늘의 목표

오늘은 Python 실기 문제에서 자주 나오는 문자열 처리와 슬라이싱을 집중적으로 다룬다. 문자열은 리스트처럼 인덱스로 접근할 수 있지만, 리스트와 달리 직접 수정할 수 없다는 점이 중요하다.

- 문자열 인덱스와 음수 인덱스를 읽을 수 있다.
- 슬라이싱 `s[start:end:step]` 결과를 예측할 수 있다.
- `split`, `join`, `replace`, `strip`의 결과를 설명할 수 있다.
- 문자열과 리스트를 함께 쓰는 코드를 추적할 수 있다.
- 시험형 문자열 출력 문제를 직접 변형해 볼 수 있다.

## 3시간 수업 구성

| 시간 | 내용 |
|---|---|
| 0:00 ~ 0:25 | 문자열의 기본 구조와 인덱스 |
| 0:25 ~ 0:55 | 양수/음수 인덱스와 슬라이싱 |
| 0:55 ~ 1:20 | 문자열 반복문과 누적 처리 |
| 1:20 ~ 1:30 | 쉬는 시간 |
| 1:30 ~ 2:05 | split, join, replace, strip |
| 2:05 ~ 2:35 | 문자열 + 리스트 종합 실습 |
| 2:35 ~ 3:00 | 실기형 문제 풀이와 정답 해설 |

---

## 1. 문자열도 인덱스로 접근한다

```python
s = "PYTHON"
print(s[0])
print(s[2])
print(s[5])
```

문자열 그림:

```text
양수 인덱스:  0   1   2   3   4   5
문자:        P   Y   T   H   O   N
음수 인덱스: -6  -5  -4  -3  -2  -1
```

출력:

```text
P
T
N
```

음수 인덱스는 뒤에서부터 센다.

```python
s = "PYTHON"
print(s[-1])
print(s[-3])
```

출력:

```text
N
H
```

---

## 2. 문자열은 직접 수정할 수 없다

리스트는 다음처럼 수정할 수 있다.

```python
a = [1, 2, 3]
a[0] = 9
print(a)
```

출력:

```text
[9, 2, 3]
```

하지만 문자열은 직접 수정할 수 없다.

```python
s = "cat"
# s[0] = "b"  # 오류
```

문자열을 바꾸고 싶으면 새 문자열을 만들어야 한다.

```python
s = "cat"
s = "b" + s[1:]
print(s)
```

출력:

```text
bat
```

핵심:

```text
리스트: 내부 값 변경 가능
문자열: 내부 문자 변경 불가, 새 문자열을 만들어야 함
```

---

## 3. 슬라이싱 기본

슬라이싱은 일부 구간을 잘라내는 문법이다.

```python
s = "PYTHON"
print(s[1:4])
```

결과:

```text
YTH
```

왜 `YTH`일까?

```text
s[1:4]는 인덱스 1부터 4 직전까지

인덱스: 0 1 2 3 4 5
문자:   P Y T H O N
선택:     Y T H
```

끝 인덱스는 포함하지 않는다. `range`와 같은 원리다.

---

## 4. 슬라이싱 생략 규칙

```python
s = "PYTHON"

print(s[:3])
print(s[3:])
print(s[:])
```

출력:

```text
PYT
HON
PYTHON
```

| 문법 | 의미 |
|---|---|
| `s[:3]` | 처음부터 3 직전까지 |
| `s[3:]` | 3부터 끝까지 |
| `s[:]` | 전체 복사 |

---

## 5. step이 있는 슬라이싱

```python
s = "ABCDEFG"
print(s[1:6:2])
```

추적:

```text
인덱스 1부터 6 직전까지: B C D E F
2칸씩 선택: B D F
```

출력:

```text
BDF
```

거꾸로 뒤집기:

```python
s = "ABCDE"
print(s[::-1])
```

출력:

```text
EDCBA
```

시각화:

```text
s[::-1]
끝에서 시작해서 앞으로 1칸씩 이동

A B C D E
        ^
      ^
    ^
  ^
^
```

---

## 6. 문자열 반복문

```python
s = "abc"
result = ""

for ch in s:
    result = ch + result

print(result)
```

추적표:

| 반복 | ch | result 변경 |
|---:|---|---|
| 시작 | - | `""` |
| 1 | `a` | `"a" + "" = "a"` |
| 2 | `b` | `"b" + "a" = "ba"` |
| 3 | `c` | `"c" + "ba" = "cba"` |

출력:

```text
cba
```

이 코드는 문자열을 뒤집는다.

---

## 7. split

`split`은 문자열을 나누어 리스트로 만든다.

```python
s = "10,20,30"
a = s.split(",")
print(a)
```

출력:

```text
['10', '20', '30']
```

주의:

```text
split 결과는 문자열 리스트다.
'10'은 숫자 10이 아니다.
```

숫자로 계산하려면 `int`로 변환해야 한다.

```python
s = "10,20,30"
total = 0

for x in s.split(","):
    total += int(x)

print(total)
```

출력:

```text
60
```

---

## 8. join

`join`은 문자열 리스트를 하나의 문자열로 합친다.

```python
a = ["A", "B", "C"]
print("-".join(a))
```

출력:

```text
A-B-C
```

그림:

```text
["A", "B", "C"]
   사이마다 "-"를 끼워 넣음
=> "A-B-C"
```

`join`은 리스트 안의 값이 문자열이어야 한다.

```python
nums = [1, 2, 3]
# print(",".join(nums))  # 오류
```

숫자 리스트는 문자열로 바꿔야 한다.

```python
nums = [1, 2, 3]
words = []

for n in nums:
    words.append(str(n))

print(",".join(words))
```

출력:

```text
1,2,3
```

---

## 9. replace와 strip

`replace`는 문자열 일부를 바꾼 새 문자열을 반환한다.

```python
s = "banana"
t = s.replace("a", "A")

print(s)
print(t)
```

출력:

```text
banana
bAnAnA
```

원본 `s`는 바뀌지 않는다. 새 문자열 `t`가 만들어진다.

`strip`은 양끝 공백을 제거한다.

```python
s = "  hello  "
print(s.strip())
print(s.lstrip())
print(s.rstrip())
```

출력:

```text
hello
hello  
  hello
```

---

## 10. 문자열 + 리스트 종합 예제

```python
text = "kim,80|lee,90|park,70"
items = text.split("|")
result = []

for item in items:
    name, score = item.split(",")
    if int(score) >= 80:
        result.append(name.upper())

print(result)
print("-".join(result))
```

데이터 구조 변화:

```text
text
=> "kim,80|lee,90|park,70"

text.split("|")
=> ["kim,80", "lee,90", "park,70"]

각 item.split(",")
=> ["kim", "80"]
=> ["lee", "90"]
=> ["park", "70"]
```

추적표:

| item | name | score | 조건 | result |
|---|---|---:|---|---|
| `kim,80` | kim | 80 | True | `["KIM"]` |
| `lee,90` | lee | 90 | True | `["KIM", "LEE"]` |
| `park,70` | park | 70 | False | `["KIM", "LEE"]` |

출력:

```text
['KIM', 'LEE']
KIM-LEE
```

---

## 11. 실기형 예제 1

```python
s = "ABCDE"
print(s[1:4])
print(s[:3])
print(s[::2])
print(s[::-1])
```

정답:

```text
BCD
ABC
ACE
EDCBA
```

---

## 12. 실기형 예제 2

```python
s = "a-b-c-d"
a = s.split("-")
b = []

for i in range(len(a)):
    if i % 2 == 0:
        b.append(a[i].upper())
    else:
        b.append(a[i])

print(b)
print("".join(b))
```

추적표:

| i | a[i] | 조건 | b |
|---:|---|---|---|
| 0 | a | True | `["A"]` |
| 1 | b | False | `["A", "b"]` |
| 2 | c | True | `["A", "b", "C"]` |
| 3 | d | False | `["A", "b", "C", "d"]` |

정답:

```text
['A', 'b', 'C', 'd']
AbCd
```

---

## 13. 혼자 푸는 연습문제

### 문제 1

```python
s = "INFORMATION"
print(s[0])
print(s[-1])
print(s[2:6])
print(s[::3])
```

### 문제 2

```python
s = "2026-06-03"
a = s.split("-")
print(a)
print(a[1] + "/" + a[2])
```

### 문제 3

```python
s = "level"
print(s == s[::-1])
```

### 문제 4

```python
data = "A:10,B:20,C:30"
items = data.split(",")
total = 0

for item in items:
    name, score = item.split(":")
    total += int(score)

print(total)
```

### 문제 5

문자열 `"hello python"`에서 공백을 기준으로 나눈 뒤, 각 단어의 첫 글자만 대문자로 바꾸어 `"Hello Python"`을 출력하는 코드를 작성하시오.

---

## 14. 정답과 해설

### 문제 1 정답

```text
I
N
FORM
IROO
```

`s[2:6]`은 인덱스 2, 3, 4, 5를 선택한다. `s[::3]`은 0, 3, 6, 9번째 문자를 선택한다.

### 문제 2 정답

```text
['2026', '06', '03']
06/03
```

### 문제 3 정답

```text
True
```

`s[::-1]`도 `"level"`이므로 같다.

### 문제 4 정답

```text
60
```

각 점수 `10`, `20`, `30`을 정수로 바꾸어 더한다.

### 문제 5 예시 정답

```python
s = "hello python"
words = s.split()
result = []

for word in words:
    result.append(word[0].upper() + word[1:])

print(" ".join(result))
```

---

## 오늘의 마무리 체크

- 문자열 인덱스도 0부터 시작한다.
- 음수 인덱스는 뒤에서부터 센다.
- 슬라이싱의 끝 인덱스는 포함하지 않는다.
- `s[::-1]`은 문자열을 뒤집는다.
- `split`은 문자열을 리스트로 만든다.
- `join`은 문자열 리스트를 문자열로 합친다.
- `replace`는 원본을 바꾸지 않고 새 문자열을 만든다.
