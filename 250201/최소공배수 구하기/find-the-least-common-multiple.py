n, m = map(int, input().split())

# Write your code here!
def lcm(n,m):
    for i in range(1, n*m+1):
        if i%n==0 and i%m==0:
            return i

print(lcm(n,m))