n, A = input().split()
cnt = 0
for i in range(int(n)):
    inp = input()
    if inp == A:
        cnt+=1
print(cnt)