N, M = map(int, input().split())
arr = [input() for _ in range(N)]

# Please write your code here.
def in_range(x,y):
    return 0<=x and x<N and 0<=y and y<M
dxs, dys = [0,-1,-1,-1,0,1,1,1], [-1,-1,0,1,1,1,0,-1]
cnt = 0

for i in range(N):
    for j in range(M):
        
        if arr[i][j] == 'L':
            for dx,dy in zip(dxs,dys):
                curt = 1
                curx = i
                cury = j
                for _ in range(2):
                    nx = curx + dx
                    ny = cury + dy
                    if in_range(nx,ny)==False:
                        break
                    if arr[nx][ny] != 'E':
                        break
                    curt+=1
                    curx = nx
                    cury = ny
                    
                if curt == 3:
                    cnt+=1
print(cnt)
                
