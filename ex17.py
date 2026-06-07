matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input("Digite um valor: "))
    print(matriz[l])
print("-=" * 30)
for m in range(0, 3):
    print(matriz[m])
print("É uma matriz quadrada.")
