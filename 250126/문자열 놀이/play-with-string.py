s, q = input().split()
s = list(s)

for i in range(int(q)):
    que = input().split()
    if que[0] == '1':
        s[int(que[1])-1], s[int(que[2])-1] = s[int(que[2])-1], s[int(que[1])-1]
        for k in range(len(s)):
            print(s[k],end="")
        print()
    else:
        for j in range(len(s)):
            if s[j] == que[1]:
                s[j] = que[2]
        for k in range(len(s)):
            print(s[k],end="")
        print()
