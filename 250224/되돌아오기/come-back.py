OFFSET = 1000
MAX_R = 2000

floor = [[0]*(MAX_R+1) for _ in range(MAX_R+1)]
n = int(input())

dxs, dys = [0,1,0,-1], [1,0,-1,0] # 동남서북, x행y열
x,y = OFFSET,OFFSET


floor[x][y] = 1
time = 0
flag = False
for i in range(n):
    dirs, num = input().split()
    num = int(num)
    if dirs =='W':
        dir_num = 2
    elif dirs=='S':
        dir_num = 1
    elif dirs == 'N':
        dir_num = 3
    else:
        dir_num = 0
    for _ in range(num):
        x,y = x+dxs[dir_num], y+dys[dir_num]
        time+=1
        if floor[x][y] == 1:
            flag = True
            print(time)
        floor[x][y] = 1

if flag == False:
    print('-1')