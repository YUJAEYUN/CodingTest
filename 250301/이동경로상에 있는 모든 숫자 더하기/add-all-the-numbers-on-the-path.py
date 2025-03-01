n, T = map(int, input().split())
str = input()
board = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
def in_range(x,y):
    return 0<=x and x<n and 0<=y and y<n

x, y = n//2, n//2
dir_num = 0
dxs, dys = [-1,0,1,0], [0,1,0,-1] #북 동 남 서
result = board[x][y]
board[x][y] = 0

for i in range(T):
    if str[i] == 'L':
        dir_num = (dir_num-1)%4
    
    elif str[i] == 'R':
        dir_num = (dir_num+1)%4
    else:
        nx,ny = x+dxs[dir_num], y+dys[dir_num]
        if in_range(nx,ny):
            x, y = nx, ny
            result += board[x][y]
            board[x][y] = 0

        else:
            x, y = x, y

print(result)
