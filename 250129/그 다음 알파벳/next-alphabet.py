alpha = input()
alpha = ord(alpha) + 1
if chr(alpha) == '{':
    alpha -= 26
print(chr(alpha))
