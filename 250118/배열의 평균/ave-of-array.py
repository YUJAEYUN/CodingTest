arr = []
wid_sum0 =0
wid_sum1 =0
hei_sum0 =0
hei_sum1 =0
hei_sum2 =0
hei_sum3 =0
total_sum =0

for i in range(2):
    temp = list(map(int,input().split()))
    arr.append(temp)


for i in range(2):
    for j in range(4):

        #가로 합 계산
        if i == 0:
            wid_sum0+=arr[i][j]
        if i == 1:
            wid_sum1+=arr[i][j]
        
        #세로 합 계산
        if j==0:
            hei_sum0+=arr[i][j]
        if j==1:
            hei_sum1+=arr[i][j]
        if j==2:
            hei_sum2+=arr[i][j]
        if j==3:
            hei_sum3+=arr[i][j]
        
        #전체 합 계산
        total_sum += arr[i][j]

print(f"{wid_sum0/4:.1f} {wid_sum1/4:.1f}")
print(f"{hei_sum0/2:.1f} {hei_sum1/2:.1f} {hei_sum2/2:.1f} {hei_sum3/2:.1f}")
print(f"{total_sum/8:.1f}")

