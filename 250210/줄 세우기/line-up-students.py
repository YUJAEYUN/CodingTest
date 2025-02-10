class Student:
    def __init__(self, height, weight, num):
        self.height = height
        self.weight = weight
        self.num = num

N = int(input())
students=[]
for i in range(N):
    num = i+1
    height, weight = tuple(input().split())
    students.append(Student(int(height), int(weight), num))

students.sort(key=lambda x:(-x.height, -x.weight, x.num))

for student in students:
    print(f"{student.height} {student.weight} {student.num}")