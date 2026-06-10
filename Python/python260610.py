"""
파이썬 기본 자료형
"""
#a = 3
#print(f"a:{type(a)}") # int
#b=1.1
#print(f"b:{type(b)}") # float
#c='c'
#print(f"c:{type(c)}") # string
#d="c"
#print(f"d:{type(d)}") # string
#e=True
#print(f"e:{type(e)}") # bool

score=65

if 100>=score>=90: # score >= 90 && score <=100    c,java 방식
    print("A학점")
elif 89>=score>=80:
    print("b학점")
elif 79>=score>=70:
    print("c학점")
else:
    print("d학점")


"""
python은 scope 개념이 없어요
그래서 코드가 실행하면서 변수가 메모리에 올라요
메모리에 올라간 변수는 그냥 막 사용해도 되요

python에서 유일하게 scope가 작동하는곳은
함수, 클래스
"""
a=1
if a:
    b=2
else: 
    c=3
#print(f"b:{b}")

# for(int i=0; i<3; i++)
for i in range(0,3):
    c=3
    #print(f"i:{i}")

# 2씩 증가. 마지막 값(2)는 stepping 값
for i in range(1,6,2):
    #print(f"i:{i}")
    pass

a = {}
b = set()

print(a)
print(b)