N, K = map(int, input().split())
MAX_LEN = 100

arr = [0] * (MAX_LEN)

for _ in range(N):
    candy, pos = map(int,input().split())
    arr[pos] += candy # 제한조건 같은 위치에 여러 바구니가 놓여 있는 것이 가능합니다...를 못봄

# Please write your code here.
max_candy = 0

for i in range(K, MAX_LEN-K): # 중앙값의 인덱스는 i
    candy_count = 0
    tmp_arr = arr[i-K:i+K+1] # 이거 자꾸 빼먹네 슬라이싱 끝값은 포함 안되서 +1 해야함.......

    for candys in tmp_arr:
        candy_count += candys
    
    max_candy = max(max_candy, candy_count)

print(max_candy)


