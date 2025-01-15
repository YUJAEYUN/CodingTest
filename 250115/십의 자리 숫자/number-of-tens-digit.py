inp = list(map(int, input().split()))

for i in range(1, 10):
    cnt=0
    for num in inp:
        if num == 0:
            print(f"{i} - {cnt}")
            break
        if num//10 == i:
            cnt+=1
