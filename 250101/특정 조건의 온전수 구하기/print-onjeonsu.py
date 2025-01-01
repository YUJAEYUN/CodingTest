n = int(input())

for i in range(1, n+1):
    flag = False
    
    if i%2==0 or i%10==5 or (i%9!=0 and i%3==0):
        flag = True
    if flag == False:
        print(i, end=" ")
