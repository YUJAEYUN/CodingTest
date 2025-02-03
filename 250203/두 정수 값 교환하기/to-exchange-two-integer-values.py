n, m = map(int, input().split())

# Write your code here!
def swap(a,b):
    a,b = b,a
    return a,b

print(*swap(n,m))