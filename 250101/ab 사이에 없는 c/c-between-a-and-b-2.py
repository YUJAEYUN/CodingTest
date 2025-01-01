a, b, c = map(int, input().split())

for i in range(a, b+1):
    if c%i==0:
        flag=True
        print("YES")
        break
    flag=False

if flag == False:
    print("NO")