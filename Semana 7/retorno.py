
def minmax(a,b,c):
    #minimo
    if a<b:
        if a<c:
            min=a
        else:
            min=c
    else:
        if b<c:
            min=b
        else:
            min=c
    #maximo
    if a>b:
         if a>c:
            max=a
         else:
            max=c
    else:
        if b>c:
            max=b
        else:
            max=c
    
    return[min,max]
print(minmax(1,52,0))