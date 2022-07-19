#Metodo tradicional
list=[]
for letra in "casa":
    list.append(letra)
print(list)

#Con comprension de listas
lista = [letra for letra in "casa"]
print(lista)
#o tambien
print([letra for letra in "casa"])