arr, alpha = input().split()
flag = False
for i in range(len(arr)):
    if arr[i] == alpha:
        print(i)
        flag = True
        break
if flag == False:
    print("No")