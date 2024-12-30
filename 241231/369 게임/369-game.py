n = int(input())
def is369(num):
    num = str(num)
    for i in range(len(num)):
        if num[i] == "3" or num[i] == "6" or num[i] == "9":
            return 0

for i in range(1, n+1):
    if i%3==0:
        print(0, end=" ")
    elif is369(i) == 0:
        print("0", end=" ")
    else:
        print(i, end=" ")
