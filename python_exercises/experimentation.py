from math import sin, pi

dsin = lambda x: sin(pi*x/180)
# 100 * ((v - gsin0)/gsin0)
gsin = 9.8 * dsin(3.8)
percentage_error = 100 * (0.402 - gsin)/gsin

print(percentage_error)