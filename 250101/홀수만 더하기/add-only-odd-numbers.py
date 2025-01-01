n = int(input())
result=0
for i in range(n):
    num = int(input())
    if num%3==0 and num%2!=0:
        result+=num

print(result)