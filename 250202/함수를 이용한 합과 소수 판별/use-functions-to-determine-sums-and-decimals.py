a, b = map(int, input().split())

def evensum(n):
    res=0
    while n>0:
        res+= n%10
        n//=10
    if res%2==0:
        return True
    return False

# Write your code here!
def is_sosu(n):
    if n == 1:
        pass
    for i in range(2,n):
        if n%i==0:
            return False
    return True

cnt=0
for i in range(a,b+1):
    if is_sosu(i) and evensum(i):
        cnt+=1

print(cnt)