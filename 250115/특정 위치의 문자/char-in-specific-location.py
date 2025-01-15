inp = input()
arr =['L','E','B','R','O','S']
idx=0
for i in arr:
    if i!=inp:
        idx+=1
    else:
        print(idx)
        break
        
if idx == len(arr):
        print("None")

