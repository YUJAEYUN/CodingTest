n, k, t = input().split()
n, k = int(n), int(k)
str = [input() for _ in range(n)]
flag = False
tmp = []
# Write your code here!
for arr in str:
    if len(arr) < len(t):
        pass
    for i in range(len(t)):
        if t[i] == arr[i]:
            flag = True
        else:
            flag = False
    if flag==True:
        tmp.append(arr)

tmp.sort()

print(tmp[k-1])
