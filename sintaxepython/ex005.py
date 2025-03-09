minha_string = "texto qualquer"
espado = " "
tudoTexto = "asdasdas"
##upper/lower case
#print(minha_string.upper())
#print(minha_string.lower())
#
##Primeira letra maiuscula
#print(minha_string.capitalize())
##é maiusculo
#print(minha_string.isupper())
##é minuscolo
#print(minha_string.islower())
##é espaço
#print(espado.isspace())
##pritavel
##print(espado.isprintable())
#todos os caracteres são texto?
#print(espado.isalpha())
#print(minha_string.isalpha())
#print(tudoTexto.isalpha())
#print(tudoTexto.isascii())#

#comEspacoInicioFim = " texto qualquer "
#print(comEspacoInicioFim)
#print(comEspacoInicioFim.strip())

#print(comEspacoInicioFim.replace('texto','cavalo'))
#print(comEspacoInicioFim.replace('texto','texto'.upper()))
#verifica quantas letras tem, não conta espaço
#print(len(comEspacoInicioFim.strip()))

#String é um array
#pega primeira letra
#print(minha_string[0])
#print(minha_string[2:5])
for letra in minha_string:
    if letra != 'q':
        letra
        #print(letra)



#print(minha_string.index("quer"))
#usa a posição de quer, como parametro para achar o q de quer
#print(minha_string[minha_string.index("quer")])

#print(minha_string[minha_string.index("quer")])

#x = "texto" in minha_string
#print(x)

carrinho = ["carro", "moto"]



def modificarValor():
    resp = input("digite o nome do item da lista que deseja alterar: ")
    x = resp in carrinho
    indice = carrinho.index(resp)
    print(indice)
    if x:
        resp = input("Agora, digite o item substituto: ")
        carrinho[indice] = resp
        #mostraLista()
        #controlador()
    else:
        print("Este item não existe na lista!")
        #controlador()


modificarValor()

print(carrinho)