n, k = map(int, input().split())
commands = [tuple(map(int, input().split())) for _ in range(k)]

# Write your code here!
block = [0 for _ in range(n+1)]
for command in commands:
    a,b = command[0], command[1]
    for i in range(a,b+1):
        block[i]+=1

print(max(block))