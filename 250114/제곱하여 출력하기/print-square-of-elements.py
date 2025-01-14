n = int(input())

arr = map(int, input().split())
arr1 = [i*i for i in arr]

print(*arr1)
