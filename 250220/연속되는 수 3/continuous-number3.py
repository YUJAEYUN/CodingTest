N = int(input())
arr = [int(input()) for _ in range(N)]

# Write your code here!
cnt = 1
count = 1
for i in range(len(arr)-1):
    if arr[i] > 0 and arr[i+1] > 0:
        cnt+=1
        count = max(count, cnt)
    
    elif arr[i] < 0 and arr[i+1] < 0:
        cnt+=1
        count = max(count, cnt)
    else:
        count = max(count, cnt)
        cnt = 1
print(count)

