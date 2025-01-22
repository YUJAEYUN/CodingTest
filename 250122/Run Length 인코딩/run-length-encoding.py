A = input()
cnt = 1
result = []
lens=0
# Write your code here!
for i in range(len(A)):
    if i == len(A)-1:
        result.append(A[i]+str(cnt))
    elif A[i] == A[i+1]:
        cnt+=1
    else:
        result.append(A[i]+str(cnt))
        cnt = 1
    

for res in result:
    lens+= len(res)
print(lens)

for res in result:
    print(res, end="")