#o algoritmo para gerar variáveis aleatórias segundo uma distribuição
#uniforme, usando o método da transformação inversa, aula10.pdf / Página 15
# x = a + (b-a)u
# u = número aleatório
# a e b = intervalo ([a,b]). Nesse caso [10,20]
# x = variável aleatória
# - Gerar u e calcular x

import random

lista = []

def function(a, b, u):
        #print("u: ")
        #print(u)
        x = a + (b-a)*u 
        #print("x: ")
        #print(x)
        lista.append(x)

for i in range(1000):
    u = random.randint(10,20)
    function(10, 20, u)

print(lista)

