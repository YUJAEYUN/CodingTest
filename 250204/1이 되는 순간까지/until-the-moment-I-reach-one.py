N = int(input())

# Write your code here!
def ans(N):
    if N==1:
        return 0
    elif N%2==0:
        return ans(N//2)+1
    elif N%2!=0:
        return ans(N//3)+1
    
print(ans(N))