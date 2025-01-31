A = input()
B = input()
n = 0

while True:
    n+=1
    A = A[-1]+A[0:len(A)-1]
    if A == B:
        print(n)
        break
    if n > len(A):
        print('-1')
        break
