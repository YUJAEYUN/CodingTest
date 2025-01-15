A = 0
B = 0
C = 0
D = 0
E = 'E'

for i in range(3):
    inp = input().split()
    if inp[0]=="Y" and int(inp[1]) >= 37:
        A += 1
    elif inp[0]=="N" and int(inp[1]) >= 37:
        B+=1
    elif inp[0]=="Y" and int(inp[1]) < 37:
        C+=1
    elif inp[0]=="N" and int(inp[1]) < 37:
        D+=1

if A>=2:
    print(f"{A} {B} {C} {D} {E}")
else:
    print(f"{A} {B} {C} {D}")
    