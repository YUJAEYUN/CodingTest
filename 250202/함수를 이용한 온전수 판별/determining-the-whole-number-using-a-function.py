a, b = map(int, input().split())

# Write your code here!
def is_onjeonsu(n):
    if n%2==0 or n%10==5 or n%3==0 and n%9!=0:
        return False
    else:
        return True
cnt=0
for i in range(a, b+1):
    if is_onjeonsu(i):
        cnt+=1

print(cnt)