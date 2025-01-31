a, b = map(int, input().split())
tmp = str(a+b)
cnt = 0
for i in range(len(tmp)):
    if tmp[i] == '1':
        cnt+=1
print(cnt)