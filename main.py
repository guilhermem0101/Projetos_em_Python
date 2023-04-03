import matplotlib.pyplot as plt
import cmath
import math

"""nome = input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: "))"""



class Pessoa: #O parâmetro self é obrigatório em todos os métodos da classe e representa o próprio objeto
    def __init__(self, nome, idade): # __init__ é um método especial em Python que é chamado quando um objeto é criado a partir de uma classe.
        self.nome = nome
        self.idade = idade






"""x = (1, 2,3, 4, 5)
y = (6, 7,8, 9, 10)
z=x + y
s=x[1:4]
print(max(s) )"""


"""def calculadora1(x, y):
    return x + y, x - y


print(calculadora1(1, 2))

def	calculadora(x,	y):
    return	{'soma':x+y,	'subtração':x-y}
resultados	=	calculadora(1,	2)
for	i	in	resultados:
    print('{}:	{}'.format(i,	resultados[i]))"""

"""while condição:
   comandos executados enquanto a condição for verdadeira
"""

"""for x in range(10):
   comandos executados 10 vezes """


x = []  # lista vazia
y = []  # lista vazia
for i in range(1, 200): # i varia de 0 a 19
  x.append(i)  # append acrescenta um elemento a uma lista
  y.append(math.sin(i))
plt.plot(x, y)
plt.show()
print('x =', x)
print('y =', y)