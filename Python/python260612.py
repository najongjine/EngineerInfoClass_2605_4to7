nums = [1, 2, 3, 4, 5]

result = [nums.pop() if i % 2 == 0 else nums.pop(0) for i in nums]

# print(nums) # [1,2,3]
# print(result) # [4,5]

data = ["aa", "b", "cccc", "ddd"]
"""
map 은 forloop 라고 생각 하세요
"""
#                            리턴값                 검사조건
result = list(map(lambda x: len(x), filter(lambda x: len(x) >= 2, data)))
#print(result)

a = [1, 2, 3]
#                     리턴값    검사조건(검사조건 없으면 그냥 패스)
b = list(map(lambda x: x * 2, a))
#print(b)



x = 10
def f():
    """
    global은 주로 함수 안에서 쓰는 키워드다.

    이 함수 안에서 x라는 이름을 사용할 때,
    새 지역변수 x를 만들지 말고
    바깥에 있는 전역변수 x를 사용하겠다고 선언한다.

    이 선언은 f 함수 안에서만 적용된다.
    다른 함수에는 영향을 주지 않는다.
    """
    global x
    x = 20

def f2():
    # 얘는 밖에 있는 x 값 안바꾸고 f2 scope 안에 지역변수 만듬
    x=30

f()
f2()
#print(x)


def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)

#print(fact(4))


a = [1, 2, 3]
b = a # 100% 주소값 공유
c = a[:] # 내용물 복사해서 주기. 주소가 a,b랑은 완전 다름

"""
i=0
i=1
i=2
"""
for i in range(len(a)):
    b[i] += i
    c[i] += b[i]

#print(a)
#print(b)
#print(c)

"""
파이썬 리스트에 원소 10개를 랜덤정수로 채운다.
리스트안에 prime number가 몇개인지 알아내는 알고리즘을 만드시오
1보다 크고, 1과 자기 자신으로만 나누어떨어지는 수
예: 2,3,5,7,11,13,17...
"""
import random
arr1=[]
for a in range(0,10):
    arr1.append(random.randint(1,99999))
print(arr1)
#arr1=[3,5,7]
count =0
for element in arr1:
    bprime=True
    if element==2:
        count+=1
        continue
    else:
        for check_num in range(2,element):
            if element % check_num ==0:
                bprime=False
                break
    if bprime:
        count+=1
#print(count)


def f1(x=1,b=True,c="페페"):
    pass

f1(c="모모")
    


