result = 0
cnt = 0

for i in range(10):
    num = int(input())
    if num >=0 and num <= 200:
        result += num
        cnt += 1

print(result, "%.1f" % (result/cnt))