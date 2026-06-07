matriz_original = [
    [1, 2],
    [3, 4],
    [5, 6]
]
total_linhas = len(matriz_original)
total_colunas = len(matriz_original[0])
matriz_transposta = []
for j in range(total_colunas):
    nova_linha = []
    for i in range(total_linhas):
        nova_linha.append(matriz_original[i][j])
    matriz_transposta.append(nova_linha)
print("--- Matriz Original ---")
for linha in matriz_original:
    for elemento in linha:
        print(f"{elemento:4}", end="")
    print()
print("\n" + "="*20 + "\n")
print("--- Matriz Transposta ---")
for linha in matriz_transposta:
    for elemento in linha:
        print(f"{elemento:4}", end="")
    print()
