N = int(input())

# Write your code here!
def squrt(N):
    if N==0:
        return 0
    return squrt(N//10) + (N%10)**2

print(squrt(N))