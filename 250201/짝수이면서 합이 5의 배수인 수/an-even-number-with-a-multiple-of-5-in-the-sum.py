n = int(input())

# Write your code here!
def res(n):
    if n%2==0 and (n//10 + n%10)%5==0:
        print("Yes")
    else:
        print("No")

res(n)