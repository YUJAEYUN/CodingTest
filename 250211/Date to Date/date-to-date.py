m1, d1, m2, d2 = map(int, input().split())

# Write your code here!
elapsed_days = 1
month, day = m1, d1

while True:
    if month == m2 and day == d2:
        break
    elapsed_days+=1
    day+=1
    if month == 2:
        if day == 29:
            month+=1
            day= 1
        
    elif month ==1 or month==3 or month==5 or month==7or month==8 or month==10 or month==12:
        if day==32:
            month+=1
            day=1
    else:
        if day==31:
            month+=1
            day=1
print(elapsed_days)