class private:
    def __init__(self, name, height, weight):
        self.name, self.height, self.weight = name, height, weight

n = 5
arr=[]
for i in range(n):
    name, height, weight = tuple(input().split())
    arr.append(private(name, int(height), float(weight)))

arr.sort(key=lambda x: x.name)
print("name")
for _ in arr:
    print(f"{_.name} {_.height} {_.weight:.1f}")
print()

arr.sort(key=lambda x: -x.height)
print("height")
for _ in arr:
    print(f"{_.name} {_.height} {_.weight:.1f}")