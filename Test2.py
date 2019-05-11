"""
请编写一个程序，从键盘上输入n（n 的范围是1～20），求n 的阶乘。
"""

import math

count = input()
count = int(count)
l = []
# python range() 函数可创建一个整数列表，一般用在 for 循环中。
# range(start, stop[, step])
for i in range(count):
    num = input()
    num = int(num)
    l.append(num)

for i in range(count):
    print(math.factorial(l[i]))


