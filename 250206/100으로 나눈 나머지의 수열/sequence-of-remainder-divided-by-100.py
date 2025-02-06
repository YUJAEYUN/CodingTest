N = int(input())

# Write your code here!
def reculsive(N):
    if N  == 1:
        return 2
    elif N==2:
        return 4
    else:
        return (reculsive(N-1) * reculsive(N-2))%100

print(reculsive(N))