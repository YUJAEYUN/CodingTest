arr = list(input())

for i in range(len(arr)):
    if arr[i].isalpha():
        print(arr[i].lower(),end="")
    elif arr[i].isdigit():
        print(arr[i],end="")
    else:
        pass