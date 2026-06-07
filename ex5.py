gabarito = ["A", "B", "C", "D", "E", "E", "D", "C", "B", "A"]
res_possi = ["A", "B", "C", "D", "E"]
acertos = []
for i in range(1, 11):
    while True:
        resposta = input(f"Qual a resposta da questão {i}?: ")
        if resposta not in res_possi:
            print("Essa alternativa não estava na prova!")
        if resposta in res_possi:
            break
    if resposta in gabarito[i-1]:
        acertos.append(i)
print("Você acertou as questões")
for ac in acertos:
    print(ac)
