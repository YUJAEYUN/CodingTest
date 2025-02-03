text = input()
pattern = input()

# Write your code here!
def isitokay():
    flag = False
    for i in range(len(text)-len(pattern)+1):
        if len(text) ==1:
            if text[i] == pattern[0]:
                return i
        if text[i]==pattern[0]:
            for j in range(1,len(pattern)):
                if text[i+j] != pattern[j]:
                    flag = False
                    break
                else:
                    flag = True
            if flag == True :
                return i

ans = isitokay()
if ans == None:
    print("-1")
else:
    print(ans)

                