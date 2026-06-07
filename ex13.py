matriz = [[9, 3, 6], [6, 7, 9], [3, 2, 8]]
for k in matriz:
    print(k)
num = int(input("Qual número deseja rastrear na matriz: "))
soma = 0
for i in matriz:
    for j in i:
        if j == num:
            soma += 1
print(f"{num} aparece {soma} vezes na matriz.")
