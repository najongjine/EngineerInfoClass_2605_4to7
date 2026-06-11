a=[1,2,3] # 배열(list)
a=(1,2,3) # 튜플
"""
튜플은 튜플 세트자체를 교체하는건 가능하다.
왜냐면 변수에 데이터 저장 하는것이기 때문
"""
a=(4,5,6)
# 튜플의 원소를 바꾸려하면 런타임 에러 터짐
#a[0]=8

a=[("apple",500),("banana",300)]
# 튜플 언패킹 기법
for (name,value) in a:
    print(f"{name},{value}")
    pass

a={1,2,3} # 세트
a=set([1,2,3,3,3,3,3,3,3,3,3,3]) # 세트
"""
세트는 중복이 제거된다
시험에서 세트 문제가 나오면, 무조건 중복 제거 하려고 넣은 코드다
"""
a.add(9) # 세트에 요소추가
a.remove(9) # 세트에 있는 원소 삭제


a = {1, 2, 3}
b = {3, 4, 5}

#print(list(a & b)) # [3]
#print(a | b) # {1, 2, 3, 4, 5}
#print(a - b) # {1, 2}

# dictionary  key : value 형태로 되있음
score = {"kim": 80, "lee": 90}
score["새로운놈"]=9
score["kim"]=99
#print(score["새로운놈"])
"""
dictionary도 forloop에 바로 넣버릴수 있음
dictionary의 key가 name에 옴
"""
for name in score:
    #print(name, score[name])
    pass

score = [{"kim": 80, "lee": 90},{"kim2": 80, "lee2": 90}]
for name in score:
    #print(name)
    pass

data = [("kim", 80), ("lee", 90), ("park", 70)]
"""
정렬하는 코드
sorted 이건 정렬하겠구나
key=lambda x: x[0]  뭔지 모르지만 뭘 기준으로 삼을지 정하는 거구나
"""
result = sorted(data, key=lambda x: x[0])
#print(result)

data = ["A", "B", "A", "C", "B"]
result = set(data)
#print(f"result:{result}")
result = sorted(result, key=lambda x: x[0])
#print(f"result:{result}")


data = ["kim:80", "lee:90", "kim:70"]
score = {}

for item in data:
    name, point = item.split(":") 
    point = int(point)
    if name in score:
        score[name] += point
    else:
        score[name] = point


for a in range(len(data)):
    pass


a=[9,4,67,3]
# 0번째부터 ~ 3미만
#print(a[1:3])

s = "ABCDE"
#print(s[:-1]) # ABCD

"""
join은 배열에 있는것들을 합쳐서 문자열로 만듬
"""
a = ["A", "B", "C"]
#print(",".join(a))
a.append("D") # D 추가
a.extend([1,2]) # 추가
a.index(1) # 똑같은 요소의 index 번호 찾기
a.insert(1,3) # 1번째 index에 3이라는 요소를 끼워넣어라
a.remove('D') # D라는 요소 삭제
#print(a.pop()) # 맨 마지막요소가 팝 하고 뱉어짐, 원본에선 제거됨
#print(a) 
#print(a.pop(3)) # index 3번째 요소가 팝 하고 뱉어짐, 원본에선 제거됨
#print(a)

"""
자료결합도
- c언어는 포인터 계열이 stamp 결합도, 나머지는 다 자료결합도
- java, python은 포인터 연산자가 없어요.
  숫자, boolean, 문자열은 자료결합도. 나머지는 다 stamp 결합도
"""
a=5
def change(a):
    # 함수 내부에는 scope이 있어요
    a=3
    pass
change(a)

a="dfd"
change(a)

a={"a":1,"b":2,"c":3}
def change(a):
    a['a']=9
change(a)
print(a)


