import numpy as np
import random as rnd

n_part = 5
p = np.zeros((n_part,5), 'int16')


for i in range (0, n_part):
    for j in range (0, 2):
        p[i,j] = rnd.randint(0,100)

for i in range (0, n_part):
    for j in range (2, 4):
        p[i,j] = rnd.randint(-10,10)


print(p, p[0], p[1,0])