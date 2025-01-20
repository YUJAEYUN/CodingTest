arr1 = input()
arr2 = input()

def printer(arr):
    for i in range(len(arr)):
        if arr[i]!=" ":
            print(arr[i],end="")
        else:
            pass
    
printer(arr1)
printer(arr2)