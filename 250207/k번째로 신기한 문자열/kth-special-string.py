n, k, t = input().split()
n, k = int(n), int(k)
str = [input() for _ in range(n)]
flag = False
tmp = []
# Write your code here!
for arr in str:
    for i in range(len(t)):
        if len(arr) < len(t):
            break
        elif t[i] == arr[i]:
            flag = True
        else:
            flag = False
    if flag==True:
        tmp.append(arr)
        flag = False

tmp.sort()

print(tmp[k-1])
