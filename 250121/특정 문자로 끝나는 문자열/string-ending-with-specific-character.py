arr = []
cnt=0
for i in range(10):
    inp = input()
    arr.append(inp)

alpha = input()

for arr in arr:
    if arr[-1] == alpha:
        print(arr)
        cnt+=1

if cnt == 0:
    print("None")
