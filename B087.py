# 500円玉をA枚、100円玉をB枚、50円玉をC枚持っています。
# これらの硬貨の中から何枚かを選び、合計金額をちょうどX円にする方法は何通りあるでしょうか？
a,b,c,x = map(int, input().split())
count = 0
for i in range(a+1):
    for j in range(b+1):
        for k in range(c+1):
            total = 500*i + 100*j + 50*k
            if total == x:
                count += 1
print(count)
