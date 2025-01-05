n = int(input())
cntodd = 1
cnteven = n
for i in range(n):
    for j in range(n):
        if j%2==0:
            print(cntodd,end="")
        elif j%2!=0:
            print(cnteven, end="")
    print()
    cnteven-=1
    cntodd+=1