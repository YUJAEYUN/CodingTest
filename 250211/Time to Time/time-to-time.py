a, b, c, d = map(int, input().split())

# Write your code here!
elapsed_time = 0
hour, mins = a, b
while True:

    if hour == c and mins == d:
        break

    elapsed_time+=1
    mins+=1

    if mins == 60:
        hour+=1
        mins=0

print(elapsed_time)