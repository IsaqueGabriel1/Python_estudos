carrinho = []
resp = ""

print("Seja vem vindo loga de produtos aleatórios!")

def mostraLista():
    print("-----------------")
    print("Carrinho: {}".format(carrinho))
    print("-----------------")

def controlador():
    mostraOpcoes()
    resp = input("Resp:")

    if resp == "1":
        mostraLista()
        controlador()
    else:
        if resp == "2":
            item = input("Digite o item que deseja adicionar: ")
            if item.isalnum() or item.isnumeric():
                adicionaItem(item)
                controlador() 
            else:
                print("Item invalido")
                controlador()    
        else:
            if resp == "3":
                mostraLista()
                item = input("Digite o nome do item")
                removedor(item)
            else:
                if resp == "4":
                    limparLista()
                else:
                    if resp == "5":
                        modificarValor()
                    else:
                        print("bye")

        


def adicionaItem(item):
    carrinho.append(item)

def mostraOpcoes():
    print("Digite 1 para ver a lista")
    print("Digite 2 para adicionar")
    print("Digite 3 para remover") 
    print("Digite 4 para remover")
    print("Digite 5 para remover")
    print("Ou digite qualquer coisa para sair!")

def modificarValor():
    resp = input("digite o nome do item da lista que deseja alterar: ")
    x = resp in carrinho
    indice = carrinho.index(resp)
    if x:
        mostraLista()
        resp = input("Agora, digite o item substituto: ")
        carrinho[indice] = resp
        mostraLista()
        controlador()
    else:
        print("Este item não existe na lista!")
        controlador()

def removedor(item):
    x = item in carrinho
    if x:
        resp = input('Realmente deseja remover {}? s/n'.format(item))
        if resp == "s":
            carrinho.remove(item)
            mostraLista()
            controlador()
        else:
            controlador()
    else:
        print("Item invalido!")
        controlador()


def limparLista():
    mostraLista()
    resp = input("Realmente deseja limpar a lista? s/n")
    if resp == "s":
        carrinho.clear()
        mostraLista()
        controlador()
    else:
        controlador()



controlador()