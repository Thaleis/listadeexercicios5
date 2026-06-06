divida = float(input("Digite o valor da sua dívida:R$ "))
juros0 = 0
juros10 = divida / 10
juros15 = (divida * 15)/100
juros20 = (divida * 20)/100
juros25 = (divida * 25)/100
lista_juros = (juros0, juros10, juros15, juros20, juros25)
print("Valor da Dívida   Valor dos Juros   Qtd de Parcelas    Valor da Parcela")
parcelas = 1
for i in range(0, 4):
    print(
        f"{divida + lista_juros[i]}                       {lista_juros[i]}             {parcelas}                    {(divida + lista_juros[i]) / parcelas} ")
    if parcelas == 1:
        parcelas = 3
    else:
        parcelas = parcelas * 2
