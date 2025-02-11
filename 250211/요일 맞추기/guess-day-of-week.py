m1, d1, m2, d2 = map(int, input().split())
flag = True
if m1>m2 or (m1==m2 and d1>d2):
    m1,d1,m2,d2 = m2,d2,m1,d1
    flag = False
# Write your code here!
month, day = m1, d1
elapsed_days = 0

while True:
    if month == m2 and day == d2:
        if flag == False:
            elapsed_days*=-1
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

if elapsed_days == 0:
    print("Mon")

else:
    res = elapsed_days%7
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    print(days[res])