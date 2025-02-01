# 변수 선언 및 입력:
a, b = tuple(map(int, input().split()))

def contain_369(n):
    while n>0:
        if n%10 == 3 or n%10 == 6 or n%10 == 9:
            return True
        n//=10
    return False

def ans(n):
    if n%3==0:
        return True
    else:
        return False
cnt=0
for i in range(a, b+1):
    if contain_369(i) or ans(i):
        cnt+=1

print(cnt)