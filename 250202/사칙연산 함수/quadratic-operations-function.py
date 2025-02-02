a, o, c = input().split()
a = int(a)
c = int(c)

# Write your code here!
def plus(a,c):
    print(f"{a} + {c} =",end=" ")
    return a+c
def minus(a,c):
    print(f"{a} - {c} =",end=" ")
    return a-c
def mul(a,c):
    print(f"{a} * {c} =",end=" ")
    return a*c
def div(a,c):
    print(f"{a} / {c} =",end=" ")
    return int(a/c)

def ans(a,o,c):
    if o =='+':
        return plus(a,c)
    elif o =='-':
        return minus(a,c)
    elif o == '/':
        return div(a,c)
    elif o =='*':
        return mul(a,c)
    else:
        return False

print(ans(a,o,c))