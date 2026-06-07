c = int(input("Quantas vezes deseja repetir a soma: "))
s = 0
il = 1
f = 1
ilp = 1
fp = 1
for k in range(c + 1):
    s += il/f
    il += 1
    f += 2
for i in range(c):
    if i == c - 1:
        print(f" {ilp}/{fp}", end=f" = {s:.2f}")
    else:
        print(f" {ilp}/{fp}", end=" + ")
    ilp += 1
    fp += 2
