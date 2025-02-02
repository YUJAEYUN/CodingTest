y = int(input())

# Write your code here!
def is_yunyear(y):
    if y%4==0:
        if y%100==0 and y%400!=0:
            return False
        return True
    else:
        return False

if is_yunyear(y):
    print("true")
else:
    print("false")