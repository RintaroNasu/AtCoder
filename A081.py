# 0と1から成る3桁の番号sが与えられます。1が何個含まれるかを求めてください。
s = str(input())
len = len(s)
count = 0
for i in range(len):
    if s[i] == "1":
        count+=1
print(count)
