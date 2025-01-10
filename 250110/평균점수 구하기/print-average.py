scores = input().split()
score = 0
for i in range(len(scores)):
    score += float(scores[i])

avg = score/8

print(f"{avg:.1f}")
