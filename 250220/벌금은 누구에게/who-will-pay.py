N,M,K = map(int,input().split())
flag = False
li = [0] * (N + 1)
for i in range(M):
    num = int(input())
    li[num] +=1

    if li[num] >= K:
        flag = True
        print(num)
if flag == False:
    print("-1")
