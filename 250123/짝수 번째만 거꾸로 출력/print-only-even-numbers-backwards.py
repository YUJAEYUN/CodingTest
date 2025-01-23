arr = input()
new_arr = []
for i in range(1, len(arr), 2):
    new_arr.append(arr[i])

for arr in new_arr[::-1]:
    print(arr,end="")