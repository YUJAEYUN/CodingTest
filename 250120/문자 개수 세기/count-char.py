arr = input()
alpha = input()
cnt=0
for i in range(len(arr)):
    if alpha == arr[i]:
        cnt+=1
print(cnt)