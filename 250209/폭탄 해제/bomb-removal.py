class bomb:
    def __init__(self, code, color, second):
        self.code = code
        self.color = color
        self.second = second
code1, color1, second1 = input().split()
bomb1 = bomb(code1, color1, second1)
print(f"code : {bomb1.code}")
print(f"color : {bomb1.color}")
print(f"second : {bomb1.second}")