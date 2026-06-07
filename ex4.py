total_de_votos = 0
lista_candidatos = ["jose","joao", "paulo", "jean"]
lista_votos = [1,2,3,4,5]
matriz = [lista_candidatos, lista_votos]
votacao = []

print ("Tabela de Candidatos")
print("Candidato       Numero")
print("José               1")
print("João               2")
print("Paulo              3")
print("Jean               4")
print("Nulo               5")
print("Branco             6")
while True:
    voto = int(input("Qual o seu voto? (Digite o número do candidato): "))
    if voto not in lista_votos:
        print("Numero não corrresponde a nenhum candidato. ")
total_de_votos += 1

print(total_de_votos)


    