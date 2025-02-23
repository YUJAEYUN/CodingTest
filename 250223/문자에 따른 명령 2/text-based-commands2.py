dirs = input()

# Write your code here!
x,y = 0,0
dx,dy = [1,0,-1,0],[0,-1,0,1] # 동남서북
dir_num = 3

for direction in dirs:
    if direction == 'L':
        dir_num = (dir_num-1)%4
    elif direction == 'R':
        dir_num = (dir_num+1)%4
    elif direction == 'F':
        x,y = x+dx[dir_num],y+dy[dir_num]
print(x, y)
