n = int(input())

# Write your code here!
def ans(n):
    res = 0
    for i in range(1, n+1):
        res+=i
    return res//10
print(ans(n))