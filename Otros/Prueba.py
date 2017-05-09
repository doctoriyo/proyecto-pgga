import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import norm, det


def vec_aleat(k):

    if k == 1:

        vec = [np.random.randint(0, 50), np.random.randint(0, 50)]
        # print(vec)

    elif k == 2:

        vec = [np.random.randint(-10, 10), np.random.randint(-10, 10)]
        # print(vec)

    return vec


class cc():
    def __init__(self):

        self.top = 50
        self.bottom = 0
        self.left = 0
        self.right = 50
        self.e = 1  # coef restitución
        self.sale = False

    def paredes(self, g_part, i):

        if g_part[i].posicion[0] < self.left or g_part[i].posicion[0] > self.right:

            g_part[i].velocidad[0] = -self.e * g_part[i].velocidad[0]

            if g_part[i].posicion[0] > self.right:

                g_part[i].posicion[0] = self.right - (g_part[i].posicion[0] - self.right)

            elif g_part[i].posicion[0] < self.left:

                g_part[i].posicion[0] = self.left - (g_part[i].posicion[0] - self.left)

            self.sale = True

            #print("Se sale")

        if g_part[i].posicion[1] < self.bottom or g_part[i].posicion[1] > self.top:

            g_part[i].velocidad[1] = -self.e * g_part[i].velocidad[1]

            if g_part[i].posicion[1] > self.top:

                g_part[i].posicion[1] = self.top - (g_part[i].posicion[1] - self.top)

            elif g_part[i].posicion[1] < self.bottom:

                g_part[i].posicion[1] = self.bottom - (g_part[i].posicion[1] - self.bottom)

            self.sale = True

            #print("Se sale")

        return self.sale



class metodos():
    def __init__(self, n, g_part, vel, dt, alpha):

        self.vel = vel
        self.v_act = 0

    def actualiza(self, i):


        self.v_act = self.vel * np.array([np.cos(g_part[i].angulo), np.sin(g_part[i].angulo)])

        # actualiza velocidad y vector de posicion

        # for i in range(n):

        g_part[i].angulo = g_part[i].angulo + np.random.uniform(-0.2, 0.2)  # actualiza tetha con ruido

        #print("ang con ruido", np.degrees(g_part[i].angulo))
        g_part[i].velocidad = alpha * g_part[i].velocidad + \
                              (1 - alpha) * self.v_act
        g_part[i].posicion = g_part[i].posicion + dt * g_part[i].velocidad

        Cond = cc()
        Cond.paredes(g_part, i)

        print("¿Se sale? " + str(Cond.sale))


class visual():
    def __init__(self, g_part, indice):
        self.i = indice
        self.colores = ['or', 'ob', 'om', 'oy', 'og', '*r', '*b', '*m', '*y', '*g']

    def dibuja(self):
        plt.plot(g_part[i].posicion[0], g_part[i].posicion[1], self.colores[i])

    def datos_vuelta(self, t):
        if i == 0:
            print("------VUELTA " + str(t) + "------")

        print("Velocidad " + str(i) + " : ", g_part[i].velocidad)
        print("Posición " + str(i) + " : ", g_part[i].posicion)
        print("Ángulo " + str(i) + " : ", np.degrees(g_part[i].angulo))


class particula():
    def __init__(self, v_o, r, pos, v):
        self.radio = r
        self.v_o = v_o

        # self.v = v
        # self.pos = pos

    def posicion(self):

        self.posicion = pos
        print("jeje")
        # return self.posicion

    def velocidad(self):

        self.velocidad = v / norm(v)
        print("jiji")
        # return self.velocidad

    def angulo(self):

        if v[0] == 0:

            self.angulo = np.pi / 2

        else:

            self.angulo = np.arctan(v[1] / v[0])

        return self.angulo


####### PROGRAMA PRINCIPAL ########

v_o = 1
t = 0
n = 5
r = 3
dt = 1
stop = 200
alpha = 0.3  # Inercia a mantener la dirección del instante anterior

p = np.zeros(n)
pos = np.zeros(n)
v = np.zeros(n)
g_part = []
print(g_part)

for i in range(0, n):
    pos = vec_aleat(1)
    v = vec_aleat(2)
    p = particula(v_o, r, pos, v)
    print(pos)
    p.posicion()  # si no se pone el argumento de dentro no va
    p.velocidad()
    p.angulo()
    print("La posicion de la particula es: " + np.str(p.posicion))
    print("La velocidad de la particula es: " + np.str(p.velocidad))

    g_part.append(p)

    #visual(g_part, i).dibuja()

# print(g_part[0].posicion)
# print(g_part[1].velocidad)

fig = plt.figure()
plt.xlim(0, 50)
plt.ylim(0, 50)

# with writer.saving(fig, "pruebamision.mp4", 100):
for t in range(stop):

    if t == 0:
        #Mision = mision(g_part, t, stop)
        Play = metodos(n, g_part, v_o, dt, alpha)
        #print("En formacion?", Mision.formacion)

    #Play.thetamed()
    #Mision.movimiento(t)
    # print("Thetas med ", g_part.angulo)
    # Play.actualiza()
    # print("x", g_part[0].posicion, g_part[1].posicion, g_part[2].posicion, g_part[3].posicion)

    # print("t",t)
    # print("tethas",np.degrees(g_part.angulo))

    for i in range(n):
        visual(g_part, i).dibuja()
        visual(g_part, i).datos_vuelta(t)
        # print("tethas", np.degrees(g_part[i].angulo))
        #    writer.grab_frame()

plt.show()


'''''

plt.ion() # decimos de forma explícita que sea interactivo

 # los datos que vamos a dibujar y a actualizar

# el bucle infinito que irá dibujando
while True:
    #y.append(np.random.randn(1)) # añadimos un valor aleatorio a la lista 'y'

    # Estas condiciones las he incluido solo para dibujar los últimos
    # 10 datos de la lista 'y' ya que quiero que en el gráfico se
    # vea la evolución de los últimos datos
    if len(g_part) <= 10:
        plt.plot(g_part)
    else:
        plt.plot(g_part[-10:])

    plt.pause(0.05) # esto pausará el gráfico
    plt.cla() # esto limpia la información del axis (el área blanca donde
              # se pintan las cosas.


'''''