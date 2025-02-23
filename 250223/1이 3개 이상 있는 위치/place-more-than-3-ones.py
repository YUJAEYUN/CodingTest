
def in_range(x,y,N):
    return 0 <=x and x<N and 0<=y and y<N

N = int(input())
a = [list(map(int,input().split())) for i in range(N)]
result=0
dxs,dys = [0,1,0,-1], [1,0,-1,0]

for i in range(N):
    for j in range(N):
        cnt = 0
        for dx,dy in zip(dxs,dys):
            nx,ny = i+dx, j+dy
            if in_range(nx,ny,N) and a[nx][ny] == 1:
                cnt+=1
        if cnt>=3:
            result+=1
print(result)

