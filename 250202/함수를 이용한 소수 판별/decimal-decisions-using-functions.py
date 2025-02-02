a, b = map(int, input().split())
# Write your code here!
def is_sosu(n):
    for i in range(2, n):
        if n%i==0:
            return False
    return True


def ans(a,b):
    result = 0
    if a == 1:
        pass
    for i in range(a, b+1):
        if is_sosu(i):
            result+=i
    print(result)

ans(a,b)