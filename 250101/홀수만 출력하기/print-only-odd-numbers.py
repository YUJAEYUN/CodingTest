N = int(input())
for i in range(N):
    num = int(input())
    if num %2 != 0 and num %3 == 0:
        print(num)