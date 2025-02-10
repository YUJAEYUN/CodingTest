n = int(input())
# Write your code here!
class Distance:
    def __init__(self, w, h, num):
        self.w, self.h, self.num = w, h, num

points = []
for i in range(n):
    w, h = tuple(input().split())
    num = i+1
    points.append(Distance(int(w), int(h), num))

points.sort(key=lambda x:(abs(-x.w-x.h), num))

for point in points:
    print(f"{point.num}")

