maior = 0
menor = 0
matriz = [[2, 5, 9], [1, 12, 14, 6], [6, 7, 22]]
for i in matriz:
    for j in i:
        if j > maior:
            maior = j
        if j < menor:
            menor = j
print(f"Maior numero da matriz: {maior}")
print(f"Menor número da matriz: {menor}")
