n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort()
B.sort()
# Write your code here!
if A == B:
    print("Yes")
else:
    print("No")