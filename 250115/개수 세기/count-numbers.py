n, m = map(int, input().split())
arr = input().split()
cnt=0
for i in arr:
    if int(i) == m:
        cnt+=1
print(cnt)