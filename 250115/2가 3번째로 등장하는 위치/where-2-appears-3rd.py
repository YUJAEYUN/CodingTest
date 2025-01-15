n = int(input())
inp = input().split()
cnt=0
idx = 0

for i in inp:
    idx+=1
    if i == '2':
        cnt+=1
        if cnt == 3:
            print(idx)