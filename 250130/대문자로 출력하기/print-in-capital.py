inp = list(input())
for i in range(len(inp)):
    if inp[i].isalpha():
        print(inp[i].upper(),end="")