atletas = []
saltos = []
maior = 0
menor = 0
lista_saltos = []
st = [ "Primeiro", "Segundo", "Terceiro", "Quarto", "Quinto" ]
while True:
    atleta = input("Digite o nome do atleta: ")
    if atleta == " ":
        print("Encerrando o programa.")
        break
    atletas.append(atleta)
    for i in range(5):
        salto = float(input(f"Qual o {i+1} salto do atleta: "))
        saltos.append(salto)
    for j in range(0, 4):
        lista_saltos.append(saltos[j])
    maior = max(saltos)
    menor = min(saltos)
    saltos.remove(maior)
    saltos.remove(menor)
    media = (sum(saltos)/len(saltos))
    for l in atletas:
        print(f"Atleta {l}  ")
        for k in lista_saltos:
            print(f"{k}m")
    print(f"Melhor salto = {maior}")
    print(f"Pior salto = {menor}")
    print(f"Média  = {media}")
    
