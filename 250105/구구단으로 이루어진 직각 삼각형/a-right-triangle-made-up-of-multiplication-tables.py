n = int(input())
cnt = n
for i in range(1, n+1):
    for j in range(1, cnt+1):
        if j==cnt:
            print(f"{i} * {j} = {i*j}")
            cnt-=1
        else:
            print(f"{i} * {j} = {i*j} /", end=" ")