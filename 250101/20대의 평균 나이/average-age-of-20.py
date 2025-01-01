ages = 0
cnt = 0
while True:
    age = int(input())
    if age > 29 or age < 20:
        print("%.2f" % (ages/cnt))
        break
    ages += age
    cnt += 1