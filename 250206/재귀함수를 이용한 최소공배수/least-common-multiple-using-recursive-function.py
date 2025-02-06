n = int(input())
arr = list(map(int, input().split()))

def gcd(x, y):
    if(y==0):
        return x
    else:
        return gcd(y,x%y)
        
def lcm(x,y):
	return (x*y)//gcd(x,y)

for i in range(n-1):
    arr[i+1] = lcm(arr[i], arr[i+1])
print(arr[-1])