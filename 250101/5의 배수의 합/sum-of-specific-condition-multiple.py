a, b = map(int, input().split())
result = 0
if a>b:
    a,b=b,a

for i in range(a, b+1):
    if i%5==0:
        result+=i

print(result)