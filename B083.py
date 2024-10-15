# 1以上N以下の整数のうち、10進法で各桁の和がA以上B以下であるものについて、総和を求めてください。
n,a,b = map(int, input().split())
total = 0

for i in range(1,n+1):
    degit_sum = 0
    temp = i
    while temp >=1:
        degit_sum += temp % 10
        temp = temp // 10
    if a<= degit_sum <= b:
        total += i

print(total)

