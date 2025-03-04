n = int(input())
a = [int(input()) for _ in range(n)]
min_ans = 99999999999
# Please write your code here.
for i in range(n):
    ans = 0
    for j in range(n):
        if i <= j:
            ans += a[j] * (j-i)
        else:
            ans += a[j]*((j-i)+len(a))
    min_ans = min(ans, min_ans)
print(min_ans)
    

