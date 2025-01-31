def ans(arr):
    tmp = []
    for i in range(len(arr)):
        if arr[i].isdigit():
            tmp.append(arr[i])
    tmp = int("".join(tmp))
    return tmp


arr1 = input()
arr2 = input()
print(ans(arr1)+ans(arr2))

