M, D = map(int, input().split())

# Write your code here!
def ans(M,D):
    if 1<= M <= 7:
        if M%2==0:
            if M == 2:
                if 1<=D<=28:
                    return True
            else:
                if 1<=D<=30:
                    return True
        else:
            if 1<=D<=31:
                return True

        return False
    elif 8<=M<=12:
        if M%2==0:
            if 1<=D<=31:
                return True
        else:
            if 1<=D<=30:
                return True
        return False

if ans(M,D):
    print("Yes")
else:
    print("No")
        