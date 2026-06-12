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
print(result)

a = [1, 2, 3]
#                     리턴값    검사조건(검사조건 없으면 그냥 패스)
b = list(map(lambda x: x * 2, a))
print(b)