
num=3000

v=[0,1]
k=0

while v[-1] < num:
    
    v.append(v[k]+v[k+1])
    k+=1
    
v.pop(-1)
print(v)