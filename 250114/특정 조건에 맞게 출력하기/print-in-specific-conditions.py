arr = map(int, input().split())

for i in arr:
    if i==0:
        break
    if i%2!=0:
        print(i+3, end=" ")
    elif i%2==0:
        print(i//2, end=" ")