# x=abdcabcabca   y="ab"
def fnCalculation(x,y):
    result = 0; # 1
    # 0 ~ 10   
    for i in range(len(x)): # 11    i=2
     #      x[2:4] == dc
     # temp=dc
     temp = x[i:i+len(y)] 
     #  dc == ab
     if temp == y:
       result += 1;
    return result
 
a = "abdcabcabca"
p1 = "ab";
p2 = "ca";
#               3                    3
out = f"ab{fnCalculation(a,p1)}ca{fnCalculation(a,p2)}"
print(out) #ab3ca3
