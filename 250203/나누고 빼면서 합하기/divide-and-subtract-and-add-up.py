n, m = map(int, input().split())
A = list(map(int, input().split()))

# Write your code here!
def ans(n,m,A):
    tmp = 0
    while m>0:
        if m%2!=0:
            tmp+=A[m-1]
            m-=1
        else:
            tmp+=A[m-1]
            m//=2
    return tmp

print(ans(n,m,A))
    
