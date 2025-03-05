A = input()
cnt=0

# Please write your code here.
for i in range(len(A)-3):
    if A[i] =='(' and A[i+1] == '(':
        for j in range(i+1, len(A)-1):
            if A[j]==')' and A[j+1] ==')':
                cnt+=1

print(cnt)