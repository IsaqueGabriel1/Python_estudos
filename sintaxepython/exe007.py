#listas e collection

familia = ["Isaque","Mãe", "Pai", "Davi", "Mariana"]
#print(familia)
#print(familia[0:2])
#print(familia[2:])

#Alterando valor da lista pelo indice
familia[3] = "Roger"
#print(familia)

#adicionando dois usuarios em forma de lista
familia.extend(["User1", "User2"])
print(familia)

#adicionando gatos
familia.append("gatos")

print(familia)

#inserindo cavalo depois do indice 2
familia.insert(2, "Cavalo")
print(familia)
#remove o ultimo
familia.pop()
print(familia)

#removendo um item especifico
familia.remove("Pai")
print(familia)

x = "Mãe" in familia

print(x)
familia.index()


