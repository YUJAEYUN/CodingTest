n = int(input())
result = 0

for i in range(1, n): # division by zero 에러 나와서 제외해줘야함
    if n%i == 0:
        result+=i

if result == n:
    print("P")
else:
    print("N")