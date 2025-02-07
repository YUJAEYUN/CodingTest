n, k, t = input().split()
n, k = int(n), int(k)
str = [input() for _ in range(n)]
flag = False
str.sort()
cnt = 0
# Write your code here!
for arr in str:
    flag = False
    for i in range(len(t)):
        if len(arr) < len(t):
            break
        elif t[i] == arr[i]:
            flag = True
        else:
            flag = False

    if flag==True:
        cnt+=1
        if cnt == k:
            print(arr)
