N, M = map(int,input().split())

floor = [[0] * (N+1) for _ in range(N+1)]
    
def is_check(r,c):
    dx,dy = [-1,0,1,0], [0,-1,0,1]
    cnt = 0
    for _ in range(4):
        if floor[r+dx[_]][c+dy[_]] == 1:
            cnt+=1
        if cnt==3:
            return True
    return False

for i in range(M):
    r,c = map(int,input().split())
    floor[r-1][c-1] = 1
    if is_check(r-1,c-1):
        print('1')
    else:
        print('0')
