class living_region:
    def __init__(self, name, adress, region):
        self.name = name
        self.adress = adress
        self.region = region

n = int(input())
lives = []
for i in range(n):
    name, adress, region = input().split()
    lives.append(living_region(name,adress,region))

find = 'a'
idx = 0
for j in range(len(lives)):
    if find < lives[j].name:
        find = lives[j].name
        idx = j

print(f"name {lives[idx].name}")
print(f"addr {lives[idx].adress}")
print(f"city {lives[idx].region}")
