
���η���ʽ

"""
���η���ʽ ax**2 + bx + c = 0
a��b��c�û��ṩ��Ϊʵ����a��0
"""
import cmath

a = float(input("����a��"))
b = float(input("����b��"))
c = float(input("����c��"))

# ����
d = (b**2) - (4*a*c)

# ������ⷽʽ
data1 = (-b-d**2) / (2*a)
data2 = (-b+d**2) / (2*a)

print(data1)
print(data2)
