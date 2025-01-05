n = int(input())
oddCnt=1
evenCnt=n
for i in range(n):
    for j in range(n):
        if i%2==0:
            print(oddCnt, end="")
            oddCnt+=1
            
        else:
            print(evenCnt, end="")
            evenCnt-=1
    print()
    oddCnt=1
    evenCnt=n