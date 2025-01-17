n = int(input())
a = list(map(int, input().split()))
flag = True
# Write your code here!

while flag == True:
    for i in range(len(a)):

        if max(a) == a[i]:
            if max(a) == a[0]:
                flag = False
            print(i+1, end=" ")
            del a[i:]
            break


