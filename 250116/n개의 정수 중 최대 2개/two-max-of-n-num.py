n = int(input())
a = list(map(int, input().split()))

# Write your code here!
a.sort(reverse=True)
print(f"{a[0]} {a[1]}")