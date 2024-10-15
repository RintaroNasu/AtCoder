# 二つの正整数a,bが与えられます。aとbの積が偶数か奇数か判定してください。
a,b = map(int,input().split())
mul = a*b
if mul%2 == 0:
    print("Even")
elif mul%2 == 1:
    print("Odd")
