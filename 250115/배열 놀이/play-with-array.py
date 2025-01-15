n, q = map(int, input().split())
arr = list(input().split())

for i in range(q):
    inp = list(input().split())

    if inp[0] == "1":
        print(arr[int(inp[1])-1])
    elif inp[0] == "2":
        if inp[1] not in arr:
            print(0)
        else:
            print(arr.index(inp[1])+1)
    elif inp[0] == "3":
        for j in range(int(inp[1])-1, int(inp[2])):
            print(arr[j], end=" ")
        print()

