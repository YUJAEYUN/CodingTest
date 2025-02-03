a, b = map(int, input().split())

# Write your code here!
def ans(a,b):
    if a>b: # b가 항상 크다고 가정
        a,b = b,a
    a*=2
    b+=25
    return a, b

a, b = ans(a,b)
print(a, b)