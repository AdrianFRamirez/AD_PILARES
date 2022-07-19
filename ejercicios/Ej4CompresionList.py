#Crear una lista de pares a partir de otra lista creada con los cuadrados de los primeros 10 números. lista anidada
#Metodo tradicional
list1=[]
for numero in range(0,11):
    list1.append(numero**2)
print(list1)
pares=[]
for numero in list1:
    if numero%2==0:
        pares.append(numero)
print(pares)
#con comprension de listas
lista = [numero for numero in [numero**2 for numero in range(0,11)] if numero % 2 == 0 ]
print(lista)