class Student:
    def __init__(self, h, w,num):
        self.h, self.w,self.num = h, w,num

N=int(input())
students=[]
for i in range(N):
    h,w = input().split()
    num = i+1
    students.append(Student(int(h),int(w),num))

students.sort(key=lambda x:(x.h, -x.w))

for result in students:
    print(f"{result.h} {result.w} {result.num}")