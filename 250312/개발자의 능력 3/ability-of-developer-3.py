abilities = list(map(int, input().split()))
tmp = 0

for val in abilities:
    tmp += val

# Please write your code here.
min_dif = 1000000
total_value = tmp

for i in range(len(abilities)-2):
    for j in range(i+1, len(abilities)-1):
        for k in range(j+1, len(abilities)):
            min_dif = min(min_dif, abs(tmp - 2 * (abilities[i]+abilities[j]+abilities[k])))

print(min_dif)