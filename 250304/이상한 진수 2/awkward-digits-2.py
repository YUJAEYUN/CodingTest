a = list(input())
flag = True

for i in range(len(a)):
    if a[i] == '0':
        a[i] = '1'
        flag = False
        break
if flag == True:
    a[-1] = '0'

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
    
