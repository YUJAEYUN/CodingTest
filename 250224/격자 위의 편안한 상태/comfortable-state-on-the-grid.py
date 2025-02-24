N, M = map(int,input().split())

floor = [[0] * (N) for _ in range(N)]
dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1]

def is_range(x, y):
    return 0 <= x < N and 0 <= y < N

def is_check(a, b):
    cnt = 0
    for i in range(4):  # i 사용
        nx, ny = a + dx[i], b + dy[i]
        if is_range(nx, ny) and floor[nx][ny] == 1:
            cnt += 1
    return cnt == 3


for i in range(M):
    r,c = map(int,input().split())
    floor[r-1][c-1] = 1
    if is_check(r-1,c-1):
        print('1')
    else:
        print('0')
