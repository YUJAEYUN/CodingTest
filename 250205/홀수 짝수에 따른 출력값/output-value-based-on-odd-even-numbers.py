N = int(input())

# Write your code here!
def odd_even(N):
    if N == 1 or N == 2:
        return N
    elif N%2!=0:
        return odd_even(N-2) + N
    return odd_even(N-2) + N

print(odd_even(N))