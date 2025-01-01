n = int(input())
result = 0
cnt = 0
for i in range(n):
    num = int(input())
    result += num
    cnt += 1

print(result, "%.1f" %(result/cnt))