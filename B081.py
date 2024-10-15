# 黒板にN個の正の整数が書かれています。
#すぬけ君は，黒板に書かれている整数がすべて偶数であるとき，次の操作を行うことができます。
# 黒板に書かれている整数すべてを，2で割ったものに置き換える。
# すぬけ君は最大で何回操作を行うことができるかを求めてください。

n = str(input())
a = list(map(int, input().split()))
count = 0
while True:
    if all(i % 2 == 0 for i in a):
        a = [i //2 for i in a]
        count += 1
    else:
        break
print(count)

