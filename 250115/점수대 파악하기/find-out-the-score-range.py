inp = list(map(int, input().split()))

for i in range(10, 0, -1):
    cnt = 0
    for num in inp:
        if num==0:
            print(f"{i*10} - {cnt}")
            break
        if num//10==i:
            cnt+=1