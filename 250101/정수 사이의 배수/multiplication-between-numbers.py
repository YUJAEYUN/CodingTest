a, b = map(int, input().split())
cnt=0
result = 0

for i in range(a, b+1):
    if i%5==0 or i%7==0:
        result+=i
        cnt+=1

print(result, "%.1f" %(result/cnt))