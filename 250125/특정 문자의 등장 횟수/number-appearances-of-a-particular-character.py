arr = input()
case1 = 0
case2 = 0
for i in range(len(arr)-1):
    if arr[i]=="e":
        if arr[i+1]=="e":
            case1+=1
        elif arr[i+1]=="b":
            case2+=1
print(case1, case2)