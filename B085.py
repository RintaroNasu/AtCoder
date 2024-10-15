n = int(input())
d = list(map(int, input().split()))
num = [0] * 101
for value in d:
    num[value]  += 1
res = 0
for i in range(1,101):
    if num[i] > 0:
        res += 1
print(res)
