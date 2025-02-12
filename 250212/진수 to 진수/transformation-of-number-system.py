a, b = map(int, input().split())
n = input()

# Write your code here!
def return_decimal(n, a):
    num = 0
    for i in range(len(n)):
        num = num*a+ int(n[i])
    return num

def return_njinsu(n,b):
    digits=[]
    while True:
        if n<b:
            digits.append(n)
            break
        digits.append(n%b)
        n//=b
    for digit in digits[::-1]:
        print(digit,end="")

res = return_decimal(n,a)
return_njinsu(res,b)