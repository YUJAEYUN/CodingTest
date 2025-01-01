n = int(input())
num = 0
for i in range(1, 101):
    if num >= n:
        print(i-1)
        break
    else:
        num += i