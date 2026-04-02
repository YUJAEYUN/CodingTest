N, B = map(int, input().split())
P = [int(input()) for _ in range(N)]
P.sort()
ans = 0

for i in range(N):
    tmp = 0
    cnt = 0

    price = P[:]
    price[i] //= 2
    price.sort()

    for j in range(N):
        if tmp + price[j] <= B:
            tmp += price[j]
            cnt += 1
        else:
            break

    ans = max(ans, cnt)

print(ans)