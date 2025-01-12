arr = list(map(int, input().split()))
n = len(arr)
cnt=0
result1=0
result2=0
for i in range(n):
    if i%2!=0:
        result1+=arr[i]
    if (i+1)%3==0:
        result2+=arr[i]
        cnt+=1
print(f"{result1} {result2/cnt:.1f}")