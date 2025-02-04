N = int(input())

# Write your code here!
def recursiveflower(N):
    if N==0:
        return
    print(N,end=" ")
    recursiveflower(N-1)
    print(N,end=" ")

recursiveflower(N)