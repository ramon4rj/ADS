
#Método para gerar u = (125 *(xn-1) + 1) mod (2^12)

#Método da transformação inversa : x = a + (b-a)*u onde f será o x obtido 
#f = a + (b-a)*u
#a = 10
#b = 20 
#u = resultado da função geradora u

#listas utilizadas
lista = []
lista2 = []
lista3 = []
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

x = 27
for i in range(1000):
    u = ((125*(x) + 1) % (2**12))
    x = u 
    ri = u / (2**12)  # Ri = Xn / m  (Relação usada p/ transformar inteiros obtidos de u em números aleatórios)
    f = 10 + (20-10)*ri

    if f >= 10 and f <= 11:
        intervalo1.append(f)
    if f >= 11 and f <= 12:
        intervalo2.append(f)
    if f >= 12 and f <= 13:
        intervalo3.append(f)
    if f >= 13 and f <= 14:
        intervalo4.append(f)
    if f >= 14 and f <= 15:
        intervalo5.append(f)
    if f >= 15 and f <= 16:
        intervalo6.append(f)
    if f >= 16 and f <= 17:
        intervalo7.append(f)
    if f >= 17 and f <= 18:
        intervalo8.append(f)
    if f >= 18 and f <= 19:
        intervalo9.append(f)
    if f >= 19 and f <= 20:
        intervalo10.append(f)
    
    lista.append(f)
        

#lista2 será usada p/ guardar os numeros observados em cada intervalo 
lista2.append(len(intervalo1))
lista2.append(len(intervalo2))
lista2.append(len(intervalo3))
lista2.append(len(intervalo4))
lista2.append(len(intervalo5))
lista2.append(len(intervalo6))
lista2.append(len(intervalo7))
lista2.append(len(intervalo8))
lista2.append(len(intervalo9))
lista2.append(len(intervalo10))


esperados = 100
#lista3 será usada p/ armazenar os erros calculados
#erro D = ( (observados - esperados)^2 / esperados )
for i in range(10):
    d = ( (lista2[i] - esperados)**2 / 100 )
    lista3.append(d)

#Soma os valores observados 
tot_obs = 0
for numero in lista2:
    tot_obs += numero
    
#Soma os valores calculados do erro d
tot_erro = 0 
for valor in lista3:
    tot_erro += valor


#Listas p/ imprimir tabela
tabela_nomes = ["Intervalos", "Observados", "Erro D    "]
tabela1 = [len(intervalo1), "             100           ", lista3[0] ]
tabela2 = [len(intervalo2), "             100            ", lista3[1] ]
tabela3 = [len(intervalo3), "              100           ", lista3[2] ]
tabela4 = [len(intervalo4), "              100           ", lista3[3] ]
tabela5 = [len(intervalo5), "             100           ", lista3[4] ]
tabela6 = [len(intervalo6), "              100           ", lista3[5] ]
tabela7 = [len(intervalo7), "              100           ", lista3[6] ]
tabela8 = [len(intervalo8), "              100           ", lista3[7] ]
tabela9 = [len(intervalo9), "             100            ", lista3[8] ]
tabela10 = [len(intervalo10), "             100            ", lista3[9] ]
tabela_total = [tot_obs, "            100          ", tot_erro]

    


#print(lista)  #mostra todos os numeros gerados
#print(len(lista)) #mostra o total de numeros gerados
#print(lista2) #mostra os numeros observados p/ cada intervalo
#print(lista3) #Mostra os erros obtidos

print(tabela_nomes)
print(tabela1)
print(tabela2)
print(tabela3) 
print(tabela4) 
print(tabela5)
print(tabela6)
print(tabela7) 
print(tabela8) 
print(tabela9) 
print(tabela10)
print("Resultados totais")
print(tabela_total)

print(" ")
print("D = {} < χ2(0,8; 9) = 12,242 ".format(tot_erro))
print("Portanto, É um bom algoritmo")

