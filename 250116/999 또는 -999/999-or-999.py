arr = map(int, input().split())
arr1 = []
for i in arr:
    if i!=999 and i!= -999:
        arr1.append(i)
    
print(f"{max(arr1)} {min(arr1)}")