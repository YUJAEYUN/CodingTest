n = int(input())
a = list(map(int, input().split()))

# Write your code here!
print(f"{min(a)} {a.count(min(a))}")