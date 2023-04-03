import matplotlib.pyplot as plt

# Definir as constantes
r = 0.1 # taxa de crescimento
K = 1000 # capacidade de suporte
t0 = 0 # tempo inicial
tf = 50 # tempo final
dt = 0.1 # tamanho do passo

# Definir as condições iniciais
P0 = 100 # população inicial

# Definir as listas para armazenar os valores
t = [t0]
P = [P0]

# Resolver a equação diferencial usando o método de Euler
while t[-1] < tf:
    Pn = P[-1] + dt * r * P[-1] * (1 - P[-1]/K)
    P.append(Pn)
    tn = t[-1] + dt
    t.append(tn)

# Plotar o gráfico da população em função do tempo
plt.plot(t, P)
plt.xlabel('Tempo')
plt.ylabel('População')
plt.title('Crescimento populacional')
plt.show()
