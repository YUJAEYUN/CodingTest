a, b, c = map(int, input().split())

# Write your code here!
elapsed_time = 0
day, hour, mins = 11,11,11

while True:
    if a <= 11 and b <= 11 and c < 11:
        print("-1")
        break
    if hour==b and mins == c and day==a:
        print(elapsed_time)
        break
    elapsed_time+=1
    mins+=1

    if mins == 60:
        hour+=1
        mins=0
        if hour==24:
            day+=1
            hour=0
    
