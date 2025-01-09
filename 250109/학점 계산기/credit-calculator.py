n = int(input())
arr_sum=0
arr = input().split()

for i in range(len(arr)):
    arr_sum+=float(arr[i])

result = arr_sum/n
print(f"{result:.1f}")
if result>=4:
    print("Perfect")
elif result>=3:
    print("Good")
else:
    print("Poor")