matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
matrizi = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input("Digite um valor: "))
    print(matriz[l])
print("-=" * 30)
print("Matriz original")
for m in range(0, 3):
    print(matriz[m])
print("Matriz invertida")
for v in range(0, 3):
    matrizi[v] = matriz[v][::-1]
    print(matrizi[v])
