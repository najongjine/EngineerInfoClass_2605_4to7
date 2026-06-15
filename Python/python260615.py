"""
파이썬은 주소값 잘 안보여주고, 비교시 바로 내용물 비교 하는 습성이 있어요
하지만, 클래스에서는 자바처럼 포인터로 작동합니다.
즉 주소값으로 보여 준다고요
"""
class A:
    # class 변수. 자바의 static 변수
    share=5
    # 파이썬 클래스 메소드들은 self 필수
    def __init__(self,a=1,b=3):
        print("A class init")
        # 필드 추가
        self.a=a
        self.b=b

#a1=A()
#a1.a=1
#print(a1.a)


class Counter:
    # 공용. 단 하나만 존재.
    total = 0

    def __init__(self):
        Counter.total += 1
        # 필드. 각 heap 영역에 각각 존재
        self.count = 1

c1=Counter()
c2=Counter()
c3=Counter()
"""
요 단계에서는
* c1에 있는 total 필드를 찾으로감.
* 필드가 없네? 그러면 static 공간에 있는거 갔다 써야지
"""
#print(f"c1.total:{c1.total}") # 3
"""
이거 static 필드에 접근한게 아니라, 필드 하나 더 만든거에요
c1에 total 이라는 필드 없네? 만들어야지
"""
c1.total=1
#print(f"Counter.total:{Counter.total}") # 3
#print(f"c1.total:{c1.total}") # 1
#print(f"c3.total:{c3.total}") # 3

"""
파이썬 클래스는 오버로딩 오버라이딩 업캐스팅 그런거 없어요
생성자도 그냥 기본적으로 하나만 실행해요
"""
class Animal():
    def __init__(self):
        self.name="동물"
        print(f"animal init")
    def sound(self):
        print("크르릉")
    def show(self):
        print(f"name:{self.name}")

class Dog(Animal):
    def __init__(self):
        #나는 죽어도 부모꺼 생성자 호출 하고싶다
        #super().__init__()
        print(f"Dog init")
    def sound(self):
        #나는 죽어도 부모꺼 sound 호출하고 싶다
        #super().sound()
        print("멍멍")

class Cat(Animal):
    def sound(self):
        print("야옹")

arr1=[Dog(),Cat()]
for e in arr1:
    #e.sound()
    pass


class A:
    x = 1

    def __init__(self):
        self.y = 2
"""
a = A()
b = A()
a.x = 10
b.y = 20

print(A.x)
print(a.x)
print(a.y)
print(b.x)
print(b.y)
"""

class Parent:
    def __init__(self):
        print("P")

    def call(self):
        print("Parent")

class Child(Parent):
    def __init__(self):
        #super().__init__()
        print("C")

    def call(self):
        print("Child")

"""
obj = Parent()
obj.call()
"""


a = {1, 1, 1}
a.add(2)
a.add(2)
a.remove(1)
a.update({4,5,6})
print(a)