n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

def in_range(x,y):
    return 0<=x and x<n and 0<=y and y<n-2


max_1 = 0
max_2 = 0
# Please write your code here.
for i in range(n):
    for j in range(n): # 2차원 다 돌아봄

        if in_range(i,j):
            block_1 = max(arr[i][j] + arr[i][j+1] + arr[i][j+2], max_1)

            for k in range(n):
                for l in range(n):
                    if in_range(k,l):
                        if k!=i and l!=j and l!=j+1 and l!=j+2:
                            block_2 = max(arr[k][l] + arr[k][l+1] + arr[k][l+2], max_2)

print(max_1 + max_2)



        

