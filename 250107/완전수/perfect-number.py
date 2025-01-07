start, end = map(int, input().split())
cnt=0
# Write your code here!
for i in range(start, end+1):
    addSum = 0
    for j in range(1,i):
        if i%j==0:
            addSum+=j
    if addSum == i:
        cnt+=1
print(cnt)