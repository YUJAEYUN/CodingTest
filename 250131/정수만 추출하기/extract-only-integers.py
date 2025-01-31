def ans(arr):
    tmp = []
    for i in range(len(arr)):
        if arr[i].isdigit():
            tmp.append(arr[i])
        else:
            break
    tmp = int("".join(tmp))
    return tmp
    
A, B = input().split()

print(ans(A)+ans(B))




