arr = list(map(int, input().split()))

for i in range(3, 11):
    arr.append(arr[-1]+2*arr[-2])

print(*arr)