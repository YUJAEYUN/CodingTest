class person:
    def __init__(self, name, height, weight):
        self.name, self.height, self.weight = name, height, weight

n = int(input())
people = []
for i in range(n):
    name, height, weight = tuple(input().split())
    people.append(person(name, int(height), int(weight)))

people.sort(key=lambda x: (x.height, -x.weight))

for human in people:
    print(f"{human.name} {human.height} {human.weight}")
    