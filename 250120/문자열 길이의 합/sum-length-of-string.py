n = int(input())
lensum = 0
cnt = 0

for i in range(n):
    arr = input()
    lensum+=len(arr)
    if arr[0] == "a":
        cnt+=1

print(f"{lensum} {cnt}")
