A = input()

# Write your code here!
def ans(A):
    cnt = 1
    for i in range(len(A)-1):
        if A[i] != A[i+1]:
            cnt+=1
        if cnt >=2:
            return True
    return False

if ans(A):
    print("Yes")
else:
    print("No")
