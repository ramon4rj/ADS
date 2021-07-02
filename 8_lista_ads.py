#algoritmo para gerar variáveis aleatórias segundo uma distribuição
#uniforme, usando o método da transformação inversa, aula10.pdf / Página 15
# x = a + (b-a)u
# u = número aleatório
# a e b = intervalo ([a,b]). Nesse caso [10,20]
# x = variável aleatória
# - Gerar u e calcular x
#
#Quantidade de valores esperadas para cada intervalo [a,b] = 100. Mas a quantidade
#observada pode ser diferente.

import random

lista = []
intervalo1 = []
intervalo2 = []
intervalo3 = []
intervalo4 = []
intervalo5 = []
intervalo6 = []
intervalo7 = []
intervalo8 = []
intervalo9 = []
intervalo10 = []

class Metodo:

    def function(self, a, b, u):
            #print("u: ")
            #print(u)
            self.a = a
            self.b = b
            self.u = u
            self.x = a + (b-a)*u 
            #print("x: ")
            #print(x)
            #lista.append(x)

    def processo(self):

        for i in range(1000):
            # Método no intervalo fixo

            u = random.randint(10,20)
            self.function(10, 20, u)
            lista.append(self.x)

            # Método nos intervalos separados
            #usar a função len como contador
            self.cont1 = 0
            self.function(10, 11, u)
            intervalo1.append(self.x)
            self.cont1 += 1

            self.cont2 = 0
            self.function(11, 12, u)
            intervalo2.append(self.x)
            self.cont2 += 1

            self.cont3 = 0
            self.function(12, 13, u)
            intervalo3.append(self.x)
            self.cont3 += 1

            self.cont4 = 0
            self.function(13, 14, u)
            intervalo4.append(self.x)
            self.cont4 += 1

            self.cont5 = 0
            self.function(14, 15, u)
            intervalo5.append(self.x)
            self.cont5 += 1

            self.cont6 = 0
            self.function(15, 16, u)
            intervalo6.append(self.x)
            self.cont6 += 1

            self.cont7 = 0
            self.function(16, 17, u)
            intervalo7.append(self.x)
            self.cont7 += 1

            self.cont8 = 0
            self.function(17, 18, u)
            intervalo8.append(self.x)
            self.cont8 += 1

            self.cont9 = 0
            self.function(18, 19, u)
            intervalo9.append(self.x)
            self.cont9 += 1

            self.cont10 = 0
            self.function(19, 20, u)
            intervalo10.append(self.x)
            self.cont10 += 1


    def quiquadrado(self, cont, ei):
        #( (quantidade observada - quantidade esperada)^2 / quantidade esperada )
        qui = ( (self.cont1 - ei)**2 / ei )

    def chamaqui(self, cont):
        self.quiquadrado(self.cont1)



a = Metodo()
a.processo()
print(lista)
print(" ")
print(" ")
print("divisao")
print(" ")
print(" ")
print(intervalo1)
#print(intervalo2)
#a.quiquadrado(cont1, 100)
#a.chamaqui(cont1)
print(len(intervalo1))
print(len(intervalo2))
