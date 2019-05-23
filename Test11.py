
二次方程式

"""
二次方程式 ax**2 + bx + c = 0
a、b、c用户提供，为实数，a≠0
"""
import cmath

a = float(input("输入a："))
b = float(input("输入b："))
c = float(input("输入c："))

# 计算
d = (b**2) - (4*a*c)

# 两种求解方式
data1 = (-b-d**2) / (2*a)
data2 = (-b+d**2) / (2*a)

print(data1)
print(data2)
