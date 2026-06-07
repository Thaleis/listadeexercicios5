preço = 0
lista_compras = 0
produtos = ["Cachorro-Quente", "Bauru Simples", "Bauru com Ovo", "Hambúrguer", "Cheeseburguer", "Refrigerante"]
codigo = ["100","101","102","103","104","105"]
preco = ["1.20, 1.30, 1.50, 1.20, 1.30, 1.0"]
matriz = [produtos, codigo, preco]
while True:
    print("Produto             Codigo            Preço")
    print("Cachorro-Quente      100              R$1,20")
    print("Bauru Simples        101              R$1,30")
    print("Bauru com Ovo        102              R$1,50")
    print("Hambúrguer           103              R$1,20")
    print("Cheeseburguer        104              R$1,30")
    print("Refrigerante         105              R$1,00")
    print("                                            ")
    print("O que deseja comprar? Digite o código do produto(tecle 0 para finalizar o pedido)")
    while True:
        pedido = input("Digite:")
        if pedido == 0:
            print("Pedido Finalizado")
            break
            
        if pedido not in codigo:
            while True:
                pedido = input("Código inválido! Digite um código existente: ")
                if pedido in codigo:
                    break
        if pedido in codigo:
            lista_compras.append(pedido)
            
        print("                     ")
        print("Algo mais?")
        
        
        

    