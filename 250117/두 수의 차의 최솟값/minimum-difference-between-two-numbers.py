n = int(input())
num = list(map(int, input().split()))

dif = 99

for i in range(n-1):
    for j in range(i+1, n):
        if num[j]-num[i] < dif:
            dif = num[j]-num[i]

print(dif)