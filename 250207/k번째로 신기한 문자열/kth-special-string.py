n, k, t = input().split()
n, k = int(n), int(k)

words = [input().strip() for _ in range(n)]
words.sort()  # 사전순 정렬

filtered_words = [word for word in words if word.startswith(t)]  # 접두사가 t인 단어만 필터링

if len(filtered_words) >= k:
    print(filtered_words[k - 1])  # k번째 단어 출력 (0-indexed라 k-1)
else:
    print("-1")  # k번째 단어가 존재하지 않으면 -1 출력
