A = input()
result = 0
for i in range(len(A)):
    if A[i].isdigit():
        result+= int(A[i])
print(result)