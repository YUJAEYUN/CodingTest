cnt = 0
tmp = []
while True:
    inp = input()
    if inp == '0':
        break
    else:
        cnt+=1
        if cnt%2!=0:
            tmp.append(inp)

print(cnt)
if len(tmp)!=0:
    for i in tmp:
        print(i)