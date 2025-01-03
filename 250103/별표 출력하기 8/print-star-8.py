n = int(input())

for i in range(1, n+1):

    if i%2==0: # 짝수행일때
        for j in range(i):
            print("*", end=" ")
        print()


    else: # 홀수행일떄
        print("*", end=" ")
        print()