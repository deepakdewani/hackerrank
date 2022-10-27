# Enter your code here. Read input from STDIN. Print output to STDOUT

import math

ab = float(input())
bc = float(input())

ac = math.sqrt((ab*ab) + (bc*bc))

bm = ac / 2.0

mc = bm

b = mc
c = bm
a = bc

angle_b = math.acos(a / (2*b))

angel_b_degree = int(round((180 * angle_b) / math.pi))

print(angel_b_degree,'\u00B0',sep='')
