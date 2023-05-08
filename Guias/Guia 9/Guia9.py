import math

########### PALINDORMO #################    ################ EJ 5 ###################
def palindromo(pal):
    k=1
    for i in range(math.floor(len(pal)/2)):
        if pal[i]!=pal[-1-i]:
            print('{0} No es palindromo'.format(pal))
            k=0
            break
    if k!=0:
        print('{0} Es palindromo'.format(pal))
        
palindromo('hola')
palindromo('neuquen')

##### EJ 6 ######
def recursiveSum(lst):
    if len(lst) == 0:
        return 0
    else:
        return lst[0] + recursiveSum(lst[1:])
    
    
lst1 = [1,2,3,4,5]
print(recursiveSum(lst1))