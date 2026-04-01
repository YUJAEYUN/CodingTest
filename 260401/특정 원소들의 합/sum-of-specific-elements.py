arr2d=[]

for i in range(4):
    arr = input().split(" ")
    arr2d.append(arr)

tmp = 0
for j in range(4):
    for k in range(4):
        if k > j:
            pass
        else:
            tmp += int(arr2d[j][k])

print(tmp)