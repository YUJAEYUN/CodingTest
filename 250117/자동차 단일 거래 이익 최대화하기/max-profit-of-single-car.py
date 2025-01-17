n = int(input())
price = list(map(int, input().split()))

# Write your code here!
gap = 0

for i in range(n-1):
    for j in range(i+1, n):
        if price[j] - price[i] > gap:
            gap = price[j]-price[i]
print(gap)
