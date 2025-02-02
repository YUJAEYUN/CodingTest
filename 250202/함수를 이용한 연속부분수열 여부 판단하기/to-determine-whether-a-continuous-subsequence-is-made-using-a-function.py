n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Write your code here!
def ans(n1,n2,a,b):
    flag = False
    for i in range(n1-n2+1):
        if a[i]==b[0]:
            if n1==1 or n2==1:
                return True
            for j in range(1,n2):
                if a[i+j]==b[j]:
                    flag = True
                else:
                    flag = False
            if flag == True:
                return True
            else:
                return False

if ans(n1,n2,a,b):
    print("Yes")
else:
    print("No")