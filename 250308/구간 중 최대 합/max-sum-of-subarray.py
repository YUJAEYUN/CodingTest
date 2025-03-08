n, k = map(int, input().split())
arr = list(map(int, input().split()))
max_sum = 0
# Please write your code here.
for i in range(n-k+1):
    tmp = 0
    for j in range(i, i+k):
        tmp += arr[j]
    
    max_sum = max(max_sum, tmp)
print(max_sum)
