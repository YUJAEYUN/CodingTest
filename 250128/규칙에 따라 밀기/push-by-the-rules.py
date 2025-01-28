A = input()
query = list(input())

for i in range(len(query)):
    if query[i] == "L":
        A = A[1:] + A[0]
    else:
        A = A[-1] + A[0:len(A)-1]

print(A)