arr = input().split()
cnt = 0
sumNum = 0

for i in range(len(arr)):
    if arr[i] == "0":
        break
    if int(arr[i])%2==0:
        cnt+=1
        sumNum+=int(arr[i])

print(f"{cnt} {sumNum}")