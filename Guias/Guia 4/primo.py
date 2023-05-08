    
k=0
p=[]
for num in range(0,10000):
    v=[]

    for i in range(2,(num+1)//2):
        if (num%i)>0:
            v.append(0)
        else :
            v.append(1)


    if all(x==0 for x in v):
        #print('{0} Es Primo'.format(num))
        p.append(num)
    elif num==4:
        print('{0} Es Primo'.format(num))
    #else:
        #print('{0} No es Primo'.format(num))
        

d=[]
a=0
for i in range(0,(len(p)-1)):
    a=i+1
    d.append(p[a]-p[i])
    
print(max(d))
 
    
