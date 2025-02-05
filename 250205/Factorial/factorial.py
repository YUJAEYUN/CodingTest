N = int(input())

# Write your code here!
def factorial(N):
    if N == 0:
        return 1
    return factorial(N-1) * N

print(factorial(N))