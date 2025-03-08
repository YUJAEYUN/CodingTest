N, S = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
min_abs = 99999999

sum_N = 0
for num in arr:
    sum_N+= num


for i in range(N-1):
    for j in range(i+1, N):
        tmp = sum_N
        tmp -= (arr[i]+arr[j])
        ans = abs(tmp - S)

        min_abs = min(min_abs, ans)
print(min_abs)
    

