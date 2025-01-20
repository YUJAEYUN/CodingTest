n = 4
arr = []

for _ in range(n):
    given_str = input()
    arr.append(given_str)

for string in arr[::-1]:
    print(string)
