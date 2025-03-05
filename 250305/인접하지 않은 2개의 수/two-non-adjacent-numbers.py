n = int(input())
numbers = list(map(int, input().split()))

# Please write your code here.
max_num = 0
for i in range(n-2):
    for j in range(i+2, n):
        temp = numbers[i] + numbers[j]
        max_num = max(max_num, temp)
print(max_num)
