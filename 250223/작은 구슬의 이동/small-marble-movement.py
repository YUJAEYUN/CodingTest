n, t = map(int, input().split())
r, c, d = input().split()
r, c = int(r), int(c)

if d == 'U':
    dir_num=0
elif d=='D':
    dir_num=3
elif d=='R':
    dir_num=1
else:
    dir_num=2

# Write your code here!
dxs,dys = [0,1,-1,0], [1,0,0,-1] #북동서남 

def in_range(r,c):
    return 0<=r and r<n and 0<=c and c<n

for i in range(t):
    c,r = c+dxs[dir_num], r+dys[dir_num]
    if not in_range(r,c):
        dir_num=3-dir_num
        continue
    c,r = c+dxs[dir_num], r+dys[dir_num]
    if i == t-1:
        print(r, c)