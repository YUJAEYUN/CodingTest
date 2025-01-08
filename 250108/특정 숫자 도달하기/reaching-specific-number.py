num_sum = 0
cnt = 0
arr = []

n = input().split()

for i in range(len(n)):
    if int(n[i]) >=250:
        print(num_sum, num_sum/cnt)
        break
    arr.append(n[i])
    num_sum+=int(n[i])
    cnt+=1
    if cnt == 10:
        print(num_sum, num_sum/cnt)
    
    
        