n = int(input())
cnt = 0
for i in range(n):
    scoreSum = 0
    arr = input().split()
    for j in range(len(arr)):
        scoreSum+= int(arr[j])
    if scoreSum/4>=60:
        print("pass")
        cnt+=1
    else:
        print("fail")
print(cnt)