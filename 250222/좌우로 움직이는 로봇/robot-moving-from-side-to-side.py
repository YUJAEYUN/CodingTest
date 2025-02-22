OFFSET = 500000
MAX_R = 1000000
n,m = map(int,input().split())
li_a = [0] * (MAX_R+1)
li_b = [0] * (MAX_R+1)
time_a = 1

for i in range(n):
    t,d = input().split()
    for _ in range(int(t)):
        li_a[time_a] = li_a[time_a-1] + (1 if d=='R' else -1)
        time_a+=1

time_b = 1
for _ in range(m):
    t,d = input().split()
    for _ in range(int(t)):
        li_b[time_b] = li_b[time_b-1] + (1 if d=='R' else -1)
        time_b+=1

if time_a < time_b:
    for i in range(time_a, time_b):
        li_a[i] = li_a[i-1]
elif time_a > time_b:
    for i in range(time_b, time_a):
        li_b[i] = li_b[i-1]

cnt = 0
time_max = max(time_a, time_b)
for i in range(1, time_max):
    if li_a[i] == li_b[i] and li_a[i-1] != li_b[i-1]:
        cnt+=1

print(cnt)