Y, M, D = map(int, input().split())

# Write your code here!
def ans(Y,M,D):
    if 1<= M <= 7:
        if M%2==0:
            if is_yunyear(Y):
                if M == 2:
                    if 1<=D<=29:
                        return True
            else:
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

def is_yunyear(Y):
    if Y%4==0:
        if Y%100==0:
            return False
        elif Y%100==0 and Y%400==0:
            return True
        return True
    else:
        return False

if ans(Y,M,D):
    if 3<=M<=5:
        print("Spring")
    elif 6<=M<=8:
        print("Summer")
    elif 9<=M<=11:
        print("Fall")
    else:
        print("Winter")
else:
    print("-1")