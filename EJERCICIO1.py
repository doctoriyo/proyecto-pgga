import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import norm, det


def vec_aleat(k):
    
    if k == 1:

        vec = [np.random.randint(0, 100), np.random.randint(0, 100)]
        #print(vec)
        
    elif k == 2:
        
        vec = [np.random.randint(-10, 10), np.random.randint(-10, 10)]
        #print(vec)
        
    return vec



#CREAR MODULO CONDICIONES DE CONTORNO
class cc():
    def __init__(self):
        
        self.top = 100
        self.bottom = 0
        self.left = 0
        self.right = 100
        self.e = 1 #coef restitución
        self.sale = False

    def paredes(self, g_part, i):
        
        if g_part[i].posicion[0] < self.left or g_part[i].posicion[0] > self.right:
            
            g_part[i].velocidad[0] = -self.e * g_part[i].velocidad[0]
            
            if g_part[i].posicion[0] > self.right:
            
                g_part[i].posicion[0] = self.right - (g_part[i].posicion[0] - self.right)
                
            elif g_part[i].posicion[0] < self.left:
                
                g_part[i].posicion[0] = self.left - (g_part[i].posicion[0] - self.left)
            
            self.sale = True
            
            print("Se sale")
    
        if g_part[i].posicion[1] < self.bottom or g_part[i].posicion[1] > self.top:
            
            g_part[i].velocidad[1] = -self.e * g_part[i].velocidad[1]
            
            if g_part[i].posicion[1] > self.top:
            
                g_part[i].posicion[1] = self.top - (g_part[i].posicion[1] - self.top)
                
            elif g_part[i].posicion[1] < self.bottom:
                
                g_part[i].posicion[1] = self.bottom - (g_part[i].posicion[1] - self.bottom)
            
            self.sale = True
            
            print("Se sale")
            
        return self.sale



#CREAR MODULO METODOS
class metodos():
    def __init__(self, n, g_part, vel, dt, alpha):
        
        self.n = n
        self.theta_m = 0
        #self.thetas = np.zeros(n)
        self.s_x = 0
        self.s_y = 0
        self.vel = vel
        self.v_act = 0

    def actualiza(self):
        
        #actualiza velocidad y vector de posicion
        
        for i in range(n):
            g_part[i].angulo = g_part[i].angulo + np.random.uniform(-0.1, 0.1) #actualiza tetha con ruido
            
            print("ang con ruido", np.degrees(g_part[i].angulo))
            g_part[i].velocidad = alpha * g_part[i].velocidad + \
                                  (1-alpha)*self.vel*np.array([np.cos(g_part[i].angulo), np.sin(g_part[i].angulo)])
            g_part[i].posicion = g_part[i].posicion + dt * g_part[i].velocidad
            g_part[i].velocidad = g_part[i].velocidad/norm(g_part[i].velocidad)

            Cond = cc()
            Cond.paredes(g_part, i)
            
            print("¿Se sale? " + str(Cond.sale))

    def thetamed(self):

        for i in range(n):

            s_x = g_part[i].velocidad[0]
            s_y = g_part[i].velocidad[1]

            # for j in range(n):

            #   if 0 < norm(np.array(g_part[i].posicion) - np.array(g_part[j].posicion))< r:

            #      s_x = s_x + g_part[j].velocidad[0]
            #     s_y = s_y + g_part[j].velocidad[1]

            #    print('j',j)

            # print("sx",s_x,"v",g_part[i].velocidad)


            if s_x == 0 and s_y > 0:

                theta_m = np.pi / 2

            elif s_x == 0 and s_y < 0:

                theta_m = 3 * np.pi / 2

            elif s_y == 0 and s_x < 0:

                theta_m = np.pi

            else:

                theta_m = np.arctan(s_y / s_x)

                if theta_m < 0 and s_x < 0:

                    theta_m = np.pi + theta_m

                elif theta_m > 0 and s_x < 0:

                    theta_m = np.pi + theta_m

            print("theta_m", np.degrees(theta_m))

            g_part[i].angulo = theta_m

            # return g_part.angulo

class visual():
    def __init__(self, g_part, indice):
        
        self.i = indice
        self.colores = ['or', 'ob', 'om', 'oy', 'og', '*r', '*b', '*m', '*y', '*g']
    
    def dibuja(self):
        
        plt.plot(g_part[i].posicion[0], g_part[i].posicion[1], self.colores[i])
        
    def datos_vuelta(self, t):
        
        if i == 0:    
            print("------VUELTA " + str(t)+ "------") 
            
        print("Velocidad " + str(i)+ " : ", g_part[i].velocidad)
        print("Posición " + str(i)+ " : ", g_part[i].posicion)
        print("Ángulo " + str(i) + " : ", np.degrees(g_part[i].angulo))  

class particula():
    def __init__(self, v_o, r, pos, v):
        self.radio = r
        self.v_o = v_o
        
        #self.v = v
        #self.pos = pos

    def posicion(self):
        
        self.posicion = pos
        #print("jeje")
        #return self.posicion

    def velocidad(self):
        
        self.velocidad = v/norm(v)
        #print("jiji")
        #return self.velocidad
    
    def angulo(self):
        
        if v[0] == 0:
            
            self.angulo = np.pi/2
            
        else:
            
            self.angulo = np.arctan(v[1]/v[0])
              
        return self.angulo


####### PROGRAMA PRINCIPAL ########

v_o = 1
t = 0
n = 10
r = 3
dt = 0.8
stop = 100
alpha = 0.3  #Inercia a mantener la dirección del instante anterior

t_in = float(input("Introduzca el tiempo: "))


pos_foco = np.zeros(n)
p = np.zeros(n)
pos = np.zeros(n)
v = np.zeros(n)
g_part = []
print(g_part)

pos_foco = vec_aleat(1)
print("pos_foco: ", str(pos_foco))

for i in range(0, n):

    pos = vec_aleat(1)
    v = vec_aleat(2)
    p = particula(v_o, r, pos, v) 
    print(pos)
    p.posicion()     #si no se pone el argumento de dentro no va
    p.velocidad()
    p.angulo()
    print("La posicion de la particula es: " + np.str(p.posicion))
    print("La velocidad de la particula es: " + np.str(p.velocidad))
    
    g_part.append(p)
    
    visual(g_part, i).dibuja()

#print(g_part[0].posicion)
#print(g_part[1].velocidad)

fig = plt.figure()
plt.xlim(0, 100)
plt.ylim(0, 100)

for t in range(stop):
        
    Play = metodos(n, g_part, v_o, dt, alpha)
    Play.thetamed()
    #print("Thetas med ", g_part.angulo)
    Play.actualiza()
    #print("x", g_part[0].posicion, g_part[1].posicion, g_part[2].posicion, g_part[3].posicion)
    
    #print("t",t)     
    #print("tethas",np.degrees(g_part.angulo))
        
    for i in range(n):
            
        visual(g_part, i).dibuja()
        visual(g_part, i).datos_vuelta(t)
            #print("tethas", np.degrees(g_part[i].angulo))
plt.show()
            
         