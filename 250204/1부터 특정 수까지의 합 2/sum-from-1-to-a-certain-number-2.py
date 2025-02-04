N = int(input())

# Write your code here!
def ans(N):
    if N==1:
        return 1
    return ans(N-1) + N

print(ans(N))