n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [tuple(map(int, input().split())) for _ in range(m)]

# Write your code here!
def ans(arr, queries):
    for i in range(m):
        answer = 0
        for j in range(queries[i][0]-1, queries[i][1]):
            answer+=arr[j]
        print(answer)

ans(arr,queries)

