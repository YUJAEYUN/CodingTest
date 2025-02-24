
n = list(input())
x,y = 0,0
dx,dy = [1,0,-1,0],[0,-1,0,1] # 동남서북
dir_num = 3
cnt=0
for req in n:
    if req == 'L':
        dir_num = (dir_num-1)%4
        cnt+=1
    elif req == 'R':
        dir_num = (dir_num+1)%4
        cnt+=1
    else:
        x, y = x+dx[dir_num], y+dy[dir_num]
        cnt+=1
    
    if x==0 and y==0:
        flag = True
        print(cnt)
        break
if flag == False:
    print('-1')

