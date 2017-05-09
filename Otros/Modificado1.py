import numpy as np
import random as rnd

n_part = 5
p = np.zeros((n_part,4))

#GENERACION POSICIONES Y VELOCIDADES PARTICULAS
for i in range (0, n_part):
    for j in range (0, 2):
        p[i,j] = rnd.randint(0,50)

for i in range (0, n_part):
    for j in range (2, 4):
        p[i,j] = rnd.randint(-1,1)

print(p)

#MOVIMIENTO DE LAS PARTICULAS
for t in range(0,100):
    for i in range (0, n_part):
        p[i,2] = p[i,2] + 0.1*rnd.randint(-1,1)     #PERTURBACION EN VELOCIDADES
        p[i,3] = p[i,3] + 0.1*rnd.randint(-1,1)

        if p[i,0] < 0 or p[i,0] > 50:       #CONDICIONES DE CONTORNO
            p[i,2] = -1*p[i,2]
        elif p[i,1] < 0 or p[i,1] > 50:
            p[i,3] = -1*p[i,3]

        p[i,0] = p[i,0] + p[i,2]
        p[i,1] = p[i,1] + p[i,3]

print(p)