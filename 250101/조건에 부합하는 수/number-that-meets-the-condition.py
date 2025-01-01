a = int(input())

for i in range(1, a+1):
    flag = False
    if (i%2==0 and i%4!=0) or i//8%2==0 or i%7<4:
        flag = True
    if flag == False:
        print(i, end=" ")