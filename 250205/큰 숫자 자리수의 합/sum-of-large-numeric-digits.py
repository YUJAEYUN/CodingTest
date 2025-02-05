a, b, c = map(int, input().split())
mul = a*b*c
# Write your code here!
def maxsum(mul):
    if mul < 10:
        return mul
    tmp = mul%10
    mul = mul//10
    return maxsum(mul) + tmp

print(maxsum(mul))