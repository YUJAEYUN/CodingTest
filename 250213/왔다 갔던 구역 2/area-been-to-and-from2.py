n = int(input())

moves = [0 for _ in range(100)]
move = 0
# Write your code here!
for _ in range(n):
    xi, di = input().split()
    xi = int(xi)
    if di=="L":
        for i in range(move, move-xi, -1):
            moves[i]+=1
        move-=xi
    else:
        for i in range(move, move+xi):
            moves[i]+=1
        move+=xi

cnt=0
for _ in range(len(moves)):
    if moves[_] > 1:
        cnt+=1

print(cnt)