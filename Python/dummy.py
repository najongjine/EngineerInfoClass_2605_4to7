data = [
    [3, 5, 2, 4, 1],
    [4, 5, 1],
    [4, 4, 1, 5, 4],
    [4, 5]
]
 
result = {}
"""

data:                [
                            [3, 5, 2, 4, 1],
                            [4, 5, 1],
                            [4, 4, 1, 5, 4],
                            [4, 5]
                     ]
lis = [3, 5, 2, 4, 1]
       [4, 5, 1]
       [4, 4, 1, 5, 4]
       [4, 5]
"""
for index, lis in enumerate(data):
    list_sum = sum(lis) # 15
    list_len = len(lis) # 5
    """
       result[0] = (15,5)
       result[1] = (10,3)
       {0: (15, 5), 1: (10, 3), 2: (18, 5), 3: (9, 2)}
    """
    result[index] = (list_sum, list_len)
 
print(result)