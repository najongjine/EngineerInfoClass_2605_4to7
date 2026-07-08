#i = input()
i="HumanDev"
x = [] 
 
"""
  "HumanDev"   ["HumanDev"]
"""
for word in i.split():
    # x=["HumanDev"]
    x.append(word)

# y="HumanDev"
y = ''.join(x)
z = ''.join(c for c in y[::-1] if c not in 'ong')
 
print(z)