for i in range(5):
    num = int(input())
    if num%3==0:
        flag=True
    else:
        flag=False
        print(0)
        break

if flag == True:
    print(1)