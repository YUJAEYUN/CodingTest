arr = list(map(int, input().split()))
sumodd = 0
sumeven = 0
for i in range(len(arr)):
    if i%2==0:
        sumodd+=arr[i]
    else:
        sumeven+=arr[i]

print(abs(sumeven-sumodd))
