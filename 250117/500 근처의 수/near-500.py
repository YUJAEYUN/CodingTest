inp = list(map(int, input().split()))
li = []
li2 = []
for num in inp:
    if num<500:
        li.append(num)
    elif num > 500:
        li2.append(num)

print(f"{max(li)} {min(li2)}")