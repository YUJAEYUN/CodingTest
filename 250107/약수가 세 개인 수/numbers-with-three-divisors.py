start, end = map(int, input().split())
cnt=0
# Write your code here!
for i in range(start, end+1):
    tmpcnt = 0
    for j in range(1, i+1):
        if i%j==0:
            tmpcnt+=1
    if tmpcnt == 3:
        cnt+=1
print(cnt)