saltos = []
maior = 0
menor = 0
lista_saltos = []
st = ["Primeiro", "Segundo", "Terceiro", "Quarto", "Quinto"]
while True:
    atleta = input(f"Digite o nome do atleta: ")
    if not atleta:
        print("Encerrando o programa.")
        break
    for i in range(5):
        salto = float(
            input(f"Qual a nota do {i+1} salto do atleta {atleta}: "))
        saltos.append(salto)
    for j in range(0, 5):
        lista_saltos.append(saltos[j])
    maior = max(saltos)
    menor = min(saltos)
    saltos.remove(maior)
    saltos.remove(menor)
    media = (sum(saltos)/len(saltos))

    print(f"Atleta {atleta}")
    for k in lista_saltos:
        print(f"{k}")
    print(f"Melhor salto = {maior}")
    print(f"Pior salto = {menor}")
    print(f"Média  = {media}")
    print("Resultado final")
    print(f"{atleta} = {media}")
