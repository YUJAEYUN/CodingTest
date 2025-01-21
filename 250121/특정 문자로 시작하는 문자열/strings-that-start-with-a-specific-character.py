n = int(input())

arr = []
cnt = 0
lens = 0
for i in range(n):
    inp = input()
    arr.append(inp)

alpha = input()

for i in arr:
    if i[0] == alpha:
        cnt+=1
        lens+=len(i)

print(f"{cnt} {lens/cnt:.2f}")
