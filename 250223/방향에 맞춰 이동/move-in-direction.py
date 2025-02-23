n = int(input())
x, y = 0,0
dx, dy = [1,0,-1,0], [0,-1,0,1]

for i in range(n):
    dir_num, num = input().split()
    for _ in range(int(num)):
        if dir_num == 'E':
            x,y = x+dx[0], y+dy[0]
        elif dir_num == 'S':
            x,y = x+dx[1],y+dy[1]
        elif dir_num == 'W':
            x,y = x+dx[2],y+dy[2]
        elif dir_num == 'N':
            x,y = x+dx[3], y+dy[3]
    
    
print(x,y)