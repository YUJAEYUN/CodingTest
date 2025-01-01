a, b, c = map(int, input().split())

for i in range(a, b+1):
    if i%c==0:
        print("YES")
        flag = True
        break
    flag = False

if flag == False:
    print("NO")