import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define constantes
G = 6.67408e-11  # constante gravitacional
m1 = 5.97e24     # massa da Terra
m2 = 7.34e22     # massa da Lua
m3 = 1000        # massa do satélite
dt = 10          # intervalo de tempo em segundos

# Define as condições iniciais (posições e velocidades)
r1 = np.array([0, 0, 0])
r2 = np.array([384400000, 0, 0])
r3 = np.array([384400000, 1000000, 0])
v1 = np.array([0, 0, 0])
v2 = np.array([0, 1022, 0])
v3 = np.array([1000, 1000, 0])

# Define as listas para armazenar as posições dos corpos ao longo do tempo
pos1 = [r1]
pos2 = [r2]
pos3 = [r3]

# Define a função para calcular a força gravitacional entre dois corpos
def grav_force(r1, r2, m1, m2):
    r = r2 - r1
    norm = np.linalg.norm(r)
    F = (G * m1 * m2 / norm**2) * r
    return F

# Define a função para atualizar as posições e velocidades dos corpos
def update(r1, r2, r3, v1, v2, v3):
    # Calcula as forças gravitacionais entre os corpos
    F1 = grav_force(r1, r2, m1, m2) + grav_force(r1, r3, m1, m3)
    F2 = grav_force(r2, r1, m2, m1) + grav_force(r2, r3, m2, m3)
    F3 = grav_force(r3, r1, m3, m1) + grav_force(r3, r2, m3, m2)
    # Atualiza as velocidades dos corpos
    v1_new = v1 + F1 / m1 * dt
    v2_new = v2 + F2 / m2 * dt
    v3_new = v3 + F3 / m3 * dt
    # Atualiza as posições dos corpos
    r1_new = r1 + v1_new * dt
    r2_new = r2 + v2_new * dt
    r3_new = r3 + v3_new * dt
    # Retorna as novas posições e velocidades dos corpos
    return r1_new, r2_new, r3_new, v1_new, v2_new, v3_new

# Simula o movimento dos corpos por um determinado número de intervalos de tempo
for i in range(10000):
    r1, r2, r3, v1, v2, v3 = update(r1, r2, r3, v1, v2, v3)
    pos1.append(r1)
    pos2.append(r2)
    pos3.append(r3)

# Plota as trajetó
fig = plt.figure

fig, ax = plt.subplots()
plt.show()
