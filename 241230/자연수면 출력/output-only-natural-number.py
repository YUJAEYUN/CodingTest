a, b = map(int, input().split())

if type(a) == int:
    if a <= 0:
        print(0)
    else:
        for i in range(b):
            print(a, end="")
