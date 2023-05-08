
def factorial(n):
    if n==0:
        return 1
    return n*factorial(n-1)

print(factorial(3))

def reverse(s):
    if s=='':
        return ''
    return reverse(s[1:])+s[0]

print(reverse('hola'))