import sys

INT_MAX = sys.maxsize

arr = list(map(int, input().split()))
n = len(arr)

def diff(i, j, k, l):
    # 세 번째 팀원의 합은 전체에서 첫 번째 팀원과 두 번째 팀원의 합을 빼줌
    sum1 = arr[i] + arr[j]
    sum2 = arr[k] + arr[l]
    sum3 = sum(arr) - sum1 - sum2
    
    if sum1 == sum2 or sum2 == sum3 or sum1 == sum3:
        return False
    
    max_score = max(sum1, sum2, sum3)
    min_score = min(sum1, sum2, sum3)
    
    return max_score - min_score

# 최소 차이를 찾기 위한 초기화
min_diff = INT_MAX
for i in range(n):
    for j in range(i + 1, n):
        for k in range(n):
            for l in range(k + 1, n):
                # 팀원이 겹치는지 여부 확인
                if k == i or k == j or l == i or l == j:
                    continue
                
                result = diff(i, j, k, l)
                if result:
                    min_diff = min(min_diff, result)

# 결과 출력
if min_diff == INT_MAX:
    print("-1")
else:
    print(min_diff)