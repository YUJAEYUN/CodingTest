N = int(input())

arr2d = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    tmp = 1
    for j in range(N):
        if i%2==0:
            arr2d[j][i] = tmp
        else:
            arr2d[j][i] = N-tmp+1
        tmp+=1

for _ in arr2d:
    print(_, end="")
print()