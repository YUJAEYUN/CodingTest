secret_code, meeting_point, time = input().split()
time = int(time)

# Write your code here!
class code:
    def __init__(self, code, point, time):
        self.code = code
        self.point = point
        self.time = time

code1 = code(secret_code, meeting_point, time)
print("secret code :",code1.code)  # 90
print("meeting point :",code1.point)  # 80
print("time :",code1.time)