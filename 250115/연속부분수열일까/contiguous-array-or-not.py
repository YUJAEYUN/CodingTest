n1, n2 = map(int, input().split())

n1arr = input().split()
n2arr = input().split()
cnt = 0

for i in range(n1-n2+1):
    if n1arr[i] == n2arr[0]:
        cnt+=1
        for j in range(1, n2):
            if n1arr[i+j] == n2arr[j]:
                cnt+=1
            else:
                cnt = 0
                break
if cnt == n2:
    print("Yes")
else:
    print("No")