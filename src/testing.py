'''
Testing various pymath functions.
'''

import pymath as pm

print(pm.avg([1,2,3,4]))

print(pm.std_dev([2,4,4,4,5,5,7,9], True))

print(pm.std_dev([727.7,1086.5,1091.0,1361.3,1490.5,1956.1]))

print(pm.std_norm_distrib(1))

print(pm.general_norm_distrib(1,1,1))

print(pm.triangle_area(2, 2))

print(pm.triangle_perimeter(1, 2, 3))