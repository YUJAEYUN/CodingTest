N = int(input())

# Write your code here!
def strange(N):
    if N==1:
        return 1
    elif N==2:
        return 2
    return strange(int(N/3))+strange(N-1)

print(strange(N))