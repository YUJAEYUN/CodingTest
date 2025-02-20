n = int(input())
arr = [int(input()) for _ in range(n)]

# Write your code here!
cnt = 1
count = 1
for i in range(len(arr)-1):
    if arr[i] < arr[i+1]:
        cnt+=1
        count = max(count, cnt)

    else:
        cnt = 1
print(count)
