n = int(input())
A = list(map(int, input().split()))

# Please write your code here.
min_sum = 99999
tmp_sum = 0
for i in range(n):
    for j in range(n):
        tmp_sum += (A[j]*(abs(j-i)))
    if min_sum > tmp_sum:
        min_sum = tmp_sum
    tmp_sum = 0
print(min_sum)
