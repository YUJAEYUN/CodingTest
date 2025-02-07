n = int(input())

# Write your code here!
def rec(n):
    if n==0:
        return
    print("HelloWorld")
    return rec(n-1)
rec(n)