word1 = list(input())
word2 = list(input())

# Write your code here!
word1.sort()
word2.sort()
"".join(word1)
"".join(word2)
if word1 == word2:
    print("Yes")
else:
    print("No")