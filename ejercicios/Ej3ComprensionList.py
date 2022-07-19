#Ejemplo 3: Crear una lista con todos los múltiplos de 2 entre 0 y 10.
#metodo tradicional
list1=[]
for numero in range(0,11):
    if numero%2==0:
        list1.append(numero)
print(list1)

#con comprension de listas
lista=[numero for numero in range(0,11) if numero%2==0]
print(lista)