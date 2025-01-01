cnt=0

while True:
    num = int(input())
    if num%2==0:
        num//=2
        cnt+=1
        print(num)
    
    if cnt == 3:
        break