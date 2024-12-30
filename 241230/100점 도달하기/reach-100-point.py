n = int(input())

def findScore(score):
    if score >= 90:
        print("A", end=" ")
    elif score >= 80:
        print("B", end=" ")
    elif score >= 70:
        print("C", end=" ")
    elif score >= 60:
        print("D", end=" ")
    else:
        print("F", end=" ")

for i in range(n, 101):
    findScore(i)