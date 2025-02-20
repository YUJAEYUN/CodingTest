n, t = map(int, input().split())
arr = list(map(int, input().split()))

# Write your code here!
cnt = 0
count = 0
for i in range(len(arr)-1):
    if arr[i] > t :
        cnt+=1
        count = max(count, cnt)
    
    else:
        cnt = 0
print(count)
