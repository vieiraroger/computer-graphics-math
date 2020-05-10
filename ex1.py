from angle import radians_to_angle, tan_to_angle
from cartography import polar_to_cartesian, distance_bettewen_two_points
import math

print("=============================")
print("===== LISTA 01 MODELO D =====")
print("=============================")
print("=============================")
print("======= Exercicio 10 ========")
print("=============================")
# Exercicio 10 da 
base = [0, 0]
a = [50, "6P/5"]
a = [a[0], radians_to_angle(a[1])]
b = [90, "7P/8"]
b = [b[0], radians_to_angle(b[1])]
c = [60, 1338]
d = [58, 30]
e = [25, -18]

a_cartesian = polar_to_cartesian(a[0], a[1])
b_cartesian = polar_to_cartesian(b[0], b[1])
c_cartesian = polar_to_cartesian(c[0], c[1])
d_cartesian = polar_to_cartesian(d[0], d[1])
e_cartesian = polar_to_cartesian(e[0], e[1])
print("Cartezianos")
print(a_cartesian)
print(b_cartesian)
print(c_cartesian)
print(d_cartesian)
print(e_cartesian)
print()
# 01
print("01")

d_base_a = distance_bettewen_two_points(base[0], base[1], a_cartesian[0], a_cartesian[1])
d_base_b = distance_bettewen_two_points(base[0], base[1], b_cartesian[0], b_cartesian[1])

if(d_base_a <= 28 and d_base_b <= 28):
    print(True)
    print()
else:
    print(False)
    print(d_base_a)
    print(d_base_b)
    print()

#02
print("02")
d_c_e = distance_bettewen_two_points(c_cartesian[0], c_cartesian[1], e_cartesian[0], e_cartesian[1])
if(d_c_e > 100):
    print(True)
    print()
else:
    print(False)
    print(d_c_e)
    print()

#04
print("04")
d_d_b = distance_bettewen_two_points(d_cartesian[0], d_cartesian[1], b_cartesian[0], b_cartesian[1])
if(d_d_b <= 80):
    print(True)
else:
    print(False)
    print(d_d_b)
    print()

print("08")
d_d_a = distance_bettewen_two_points(d_cartesian[0], d_cartesian[1], a_cartesian[0], a_cartesian[1])
if(d_d_a <= 80):
    print(True)
else:
    print(False)
    print(d_d_a)
    print()

print("16")
d_e_b = distance_bettewen_two_points(e_cartesian[0], e_cartesian[1], b_cartesian[0], b_cartesian[1])
if(d_e_b <= 80*1.6975):
    print(True)
    print()
else:
    print(False)
    print(d_d_a)
    print()

print("32")
d_e_b = distance_bettewen_two_points(e_cartesian[0], e_cartesian[1], b_cartesian[0], b_cartesian[1])
if(d_e_b <= 80*1.175):
    print(True)
else:
    print(False)
    print(d_d_a)
    print()

print("=============================")
print("======= Exercicio 11 ========")
print("=============================")

r = 2
'''
2*2 = 4
4 * 4 = (f - 2) * (f - 2) + 2*(f - 2)*2*(f - 2)
16 = 5f*f - 20f + 20
5f*f - 20f + 4 = 0
f' = 3.78
f'' = 0.21
'''

f = 3.79
print((f - 2)*(f - 2) +2*(f - 2)*2*(f - 2))
a = [2, 2]
b = [f, f*2]
x = b[0] - a[0]
y = b[1] - a[1]
angle = tan_to_angle(y/x, 1)
print(angle)
print(90 - angle)