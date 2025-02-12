N = list(input())

# Write your code here!
def return_decimal(n):
    num = 0
    for i in range(len(n)):
        num = num*2+ int(n[i])
    return num

def return_binary(n):
    digits=[]
    while True:
        if n<2:
            digits.append(n)
            break
        digits.append(n%2)
        n//=2
    for digit in digits[::-1]:
        print(digit,end="")

res = return_decimal(N) * 17
return_binary(res)