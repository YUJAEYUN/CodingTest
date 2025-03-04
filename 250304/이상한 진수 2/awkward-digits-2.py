a = list(input())

for i in range(len(a)):
    if len(a) == 1 and a[i] == '1':
        a[i] = '0'

    elif a[i] == '0':
        a[i] = '1'
        break

# Please write your code here.
def binary_to_decimal(arr):
    cnt = 0
    sum = 0
    for i in arr[::-1]:
        sum += int(i)*(2**cnt)
        cnt+=1
    return sum

ans = binary_to_decimal(a)
print(ans)
    
