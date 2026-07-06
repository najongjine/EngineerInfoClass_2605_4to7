# [99,2,3]
lst = [1,2,3]
"""
       {1:2
       2:4}  -> 2:7
       3:6}
"""
dst = {i : i* 2 for i in lst}

"""
dictionary 에서 value 들만 쫙 뽑고, 그걸 set 로 만들어라
{2,4,6} -> {2,4,6,99}
"""
s = set(dst.values())
lst[0] = 99 
dst[2]=7
s.add(99)
print(f"dst:",dst)
"""
            {2,4,6,99} & {2,7,6} -> len({2,6})
"""
print(len(s & set(dst.values())))