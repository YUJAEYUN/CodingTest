class rainy_day:
    def __init__(self, date, day, weather):
        self.date = date
        self.day = day
        self.weather = weather

n = int(input())
arr = [input().split() for i in range(n)]
rainydays= [rainy_day(date, day, weather) for date, day, weather in arr]

sel = []
idx = 0
for i, rainyday in enumerate(rainydays):
    if rainyday.weather == "Rain":
        sel.append(rainyday)

res = sel[0].date
for i, rainyday in enumerate(sel):
    if res > rainyday.date:
        res = rainyday.date
        idx = i

print(f"{sel[idx].date} {sel[idx].day} {sel[idx].weather}")