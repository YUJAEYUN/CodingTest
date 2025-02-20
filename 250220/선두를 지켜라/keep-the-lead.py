N, M = map(int,input().split())
MAX_T = 1000000
arr_a = [0] * (MAX_T+1)
arr_b = [0] * (MAX_T+1)
cnt = 0
time_a = 0
time_b = 0
for i in range(N):
    v,t = input().split()
    time_a += int(t)
    for i in range(time_a-int(t)+1, time_a+1):
        arr_a[i] = arr_a[i-1] + int(v) * (i)

for j in range(M):
    v,t = input().split()
    time_b += int(t)
    for i in range(time_b-int(t)+1, time_b+1):
        arr_b[i] = arr_b[i-1] + int(v) * (i)

for i in range(1, len(arr_a)-1):
    if (arr_a[i] - arr_b[i]) * (arr_a[i+1] - arr_b[i+1]) < 0:
        cnt+=1
print(cnt)