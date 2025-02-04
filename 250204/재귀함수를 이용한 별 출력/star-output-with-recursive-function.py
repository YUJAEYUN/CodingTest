n = int(input())

# Write your code here!
def star(n):
    if n==0:
        return
    star(n-1)
    print('*'*n)

star(n)