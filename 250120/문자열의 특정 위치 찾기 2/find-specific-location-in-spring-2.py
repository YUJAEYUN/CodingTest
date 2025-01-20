arr = ["apple", "banana", "grape", "blueberry", "orange"]

aplha = input()
cnt = 0

for arr in arr:
    if aplha == arr[2] or aplha == arr[3]:
        cnt+=1
        print(arr)
print(cnt)