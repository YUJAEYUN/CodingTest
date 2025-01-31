n = int(input())
res = 0
for i in range(n):
    num = int(input())
    res += num

res = str(res)
res = res[1:]+res[0]
print(res)