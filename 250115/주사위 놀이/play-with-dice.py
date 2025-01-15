arr = list(map(int, input().split()))

for i in range(1,7):
    cnt=0
    for num in arr:
        if i == num:
            cnt+=1
    print(f"{i} - {cnt}")