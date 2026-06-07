vogais = ["A", "E", "I", "I", "O", "U"]
vog = 0
palavra = input("Digite uma palavra: ")
for i in palavra:
    if i.upper() in vogais:
        vog += 1
con = len(palavra) - vog
print(f"{palavra} tem {vog} vogais e {con} consoantes.")
