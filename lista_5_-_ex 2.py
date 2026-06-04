lista_intervalos1 = []
lista_intervalos2 = []
lista_intervalos3 = []
lista_intervalos4 = []
for l1 in range (0,26):
    lista_intervalos1.append(l1)
for l2 in range (26,51):
    lista_intervalos2.append(l2)
for l3 in range (51,76):
    lista_intervalos3.append(l3)
for l4 in range (75,101):
    lista_intervalos4.append(l4)
intervalo1 = 0
intervalo2 = 0
intervalo3 = 0
intervalo4 = 0
semintervalo = 0
while True:
    numero = float(input("Digite um numero positivo entre 0 e 100: "))
    if numero in lista_intervalos1:
        print(f"{numero} está na lista 1 de intervalos.")
        intervalo1 += 1
    elif numero in lista_intervalos2:
        print(f"{numero} está na lista 2 de intervalos.")
        intervalo2 += 1
    elif numero in lista_intervalos3:
        print(f"{numero} está na lista 3 de intervalos.")
        intervalo3 += 1
    elif numero in lista_intervalos4:
        print(f"{numero} está na lista 4 de intervalos.")
        intervalo4 += 1
    elif numero < 0:
        print("Número negativo digitado, encerrando o programa...")
        semintervalo += 1
        break
    else:
        print(f"{numero} está fora de todos os intervalos.")
print(f"{intervalo1} números digitados estão no intervalo 1.")
print(f"{intervalo2} números digitados estão no intervalo 2.")
print(f"{intervalo3} números digitados estão no intervalo 3.")
print(f"{intervalo4} números digitados estão no intervalo 4.")
print(f"{semintervalo} números digitados estão sem intervalo.")

