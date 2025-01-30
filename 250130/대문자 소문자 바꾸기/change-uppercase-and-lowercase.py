arr = input()

for i in range(len(arr)):
    if arr[i].islower():
        print(arr[i].upper(),end="")
    else:
        print(arr[i].lower(),end="")