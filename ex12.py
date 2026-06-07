somap = 0
somas = 0
n = 3
matriz = [[2, 5, 8], [5, 7, 3], [8, 6, 0]]
for i in matriz:
    print(i)
for j in range(3):
    somap += matriz[j][j]
    somas += matriz[j][n - 1 - j]
print(f"Diagonal principal soma: {somap}")
print(f"Diagonal secundária: {somas}")
