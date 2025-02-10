n = int(input())

class human:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight
arr = [tuple(input().split()) for i in range(n)]
people = [human(name,height,weight) for name,height,weight in arr]

people.sort(key=lambda x:x.height)

for person in people:
    print(f"{person.name} {person.height} {person.weight}")