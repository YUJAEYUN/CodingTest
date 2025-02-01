n, m = map(int, input().split())

# Write your code here!
def gcf(n,m):
    if n>m:
        n, m = m, n
    for i in range(m, 0, -1):
        if m%i==0 and n%i==0:
            return i

print(gcf(n,m))