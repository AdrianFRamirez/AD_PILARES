#Crear una lista con los cuadrados de los primeros 10 números.
list1=[]
for numero in range(0,11):
    list1.append(numero**2)
print(list1)

#con comprension de listas
lista=[numero**2 for numero in range(0,11)]
print(lista)

#al cubo
nums = [2,3,5,7]
num_cubes = [num**3 for num in nums]
print(num_cubes)