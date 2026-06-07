c = int(input("Quantas vezes deseja repetir a soma: "))
s = 0
il = 2
f = 3
ilp = 2
fp = 2
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
    
