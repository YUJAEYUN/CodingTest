arr = input()
s = list(arr)
while len(arr)!=1:
    num = int(input())
    if num>len(s):
        s.pop(-1)
    else:
        s.pop(num)
    arr = "".join(s)
    print(arr)

