a = ["Seoul", "Kyeonggi", "Incheon", "Daejun", "Daegu", "Pusan"] 
str = "S"
 
"""
   i      a
"Seoul"  ["Seoul", "Kyeonggi", "Incheon", "Daejun", "Daegu", "Pusan"]
"""
for i in a:
    """
          "S" +  "Seoul"[1] = "Se"
          "Se" + "Kyeonggi"[1] = "Sey"
          "Sey" + "Incheon"[1] = "Seyn" ...
    """
    str = str + i[1]
 
print(str)
