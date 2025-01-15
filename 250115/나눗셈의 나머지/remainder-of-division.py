a, b = map(int, input().split())
arr = []
result=0
while a>1:
    a = a//b
    arr.append(a%b)

for i in range(b):
    cnt = 0
    for num in arr:
        if i==num:
            cnt+=1
    result+=cnt**2
print(result)
    
    