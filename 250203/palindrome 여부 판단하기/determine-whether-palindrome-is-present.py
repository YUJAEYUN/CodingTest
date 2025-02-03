A = input()

# Write your code here!
def is_palindrome(A):
    if A == A[::-1]:
        return True
    return False

if is_palindrome(A):
    print("Yes")
else:
    print("No")