A = list(input())
B = list(input())
flag = False
# Write your code here!
while True:
    
    for i in range(len(A)-len(B)+1):
        
        for j in range(len(B)):
            if A[i+j] == B[j]:
                flag = True
            else:
                flag = False
                break

        if flag == True:
            for k in range(len(B)):
                A.pop(i)
            break

    if flag == False or len(A) == 0:
        break

A = "".join(A)
print(A)