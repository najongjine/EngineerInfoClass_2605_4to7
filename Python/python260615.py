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

c1.total=1
print(f"Counter.total:{Counter.total}") # 3
print(f"c1.total:{c1.total}") # 1