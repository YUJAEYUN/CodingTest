input_str = input()
target_str = input()
flag = True

# Write your code here!
for i in range(len(input_str)):
    if input_str[i] == target_str[0]:
        result = i
        if len(target_str)==1:
            falg = False
            break
        for j in range(1, len(target_str)-1):
            if input_str[i+j] == target_str[j]:
                flag = False
            else:
                flag = True
        if flag == False:
            break


if flag == False:
    print(i)
else:
    print(-1)
