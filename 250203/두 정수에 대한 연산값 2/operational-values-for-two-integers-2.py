a, b = map(int, input().split())

# Write your code here!
def ans(a,b):
    if a>b:
        a*=2
        b+=10
        return a,b
    a+=10
    b*=2
    return a,b

a, b = ans(a,b)
print(a, b)