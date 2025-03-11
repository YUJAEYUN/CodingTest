N, H, T = map(int,input().split())

arr = input().split()
min_cost = 999999

for i in range(N-T+1):
    cost = 0
    for j in range(i, i+T):
        cost += abs(int(arr[j])-H)

    min_cost = min(cost, min_cost)
        
print(min_cost)
        
        
            