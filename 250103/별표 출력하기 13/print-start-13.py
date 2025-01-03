n = int(input())
odd = 1
even = n
for i in range(1, 2*n+1):

    if i%2!=0:
        for j in range(even):
            print("*", end=" ")
        even-=1
        print()


    else:
        for k in range(odd):
            print("*", end=" ")
        odd+=1
        print()