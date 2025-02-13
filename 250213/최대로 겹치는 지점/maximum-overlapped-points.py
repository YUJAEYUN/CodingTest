n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Write your code here!
block = [0 for _ in range(101)]
for segment in segments:
    x1,x2 = segment[0], segment[1]
    for i in range(x1, x2+1):
        block[i]+=1

print(max(block))