arr = input().split()
arr1 = []
sumNum = 0
cnt = 0
for i in range(len(arr)):
    if arr[i] == "0":
        print(f"{sumNum} {sumNum/cnt:.1f}")
    else:
        arr1.append(arr[i])
        cnt+=1
        sumNum+= int(arr[i])

    if cnt == len(arr):
        print(f"{sumNum} {sumNum/cnt:.1f}")