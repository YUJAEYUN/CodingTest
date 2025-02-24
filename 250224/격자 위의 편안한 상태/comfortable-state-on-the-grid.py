N, M = map(int,input().split())

floor = [[0] * (N+2) for _ in range(N+2)]
    
def is_check(r,c):
    dx,dy = [-1,0,1,0], [0,-1,0,1]
    cnt = 0
    for i in range(4):
        if floor[r+dx[i]][c+dy[i]] == 1:
            cnt+=1
        if cnt==3:
            return True
    return False

for i in range(M):
    r,c = map(int,input().split())
    floor[r][c] = 1
    if is_check(r,c):
        print('1')
    else:
        print('0')
