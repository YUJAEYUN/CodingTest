input_str, q = input().split()
q = int(q)
queries = [int(input()) for _ in range(q)]

# Write your code here!
for i in range(q):
    if len(input_str) == 1:
        print(input_str)
    elif queries[i] == 1:
        input_str = input_str[1:] + input_str[0]
        print(input_str)
    elif queries[i] == 2:
        input_str = input_str[-1] + input_str[0:q-1]
        print(input_str)
    else:
        input_str = input_str[::-1]
        print(input_str)