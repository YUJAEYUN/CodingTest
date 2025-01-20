maxlen = 0
minlen = 20
for i in range(3):
    inp = input()
    if maxlen < len(inp):
        maxlen = len(inp)
    if minlen > len(inp):
        minlen = len(inp)
print(f"{maxlen-minlen}")