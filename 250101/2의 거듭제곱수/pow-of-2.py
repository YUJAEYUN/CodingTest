N = int(input())
cnt = 0
while True:
    cnt += 1
    N//=2

    if N == 1:
        print(cnt)
        break