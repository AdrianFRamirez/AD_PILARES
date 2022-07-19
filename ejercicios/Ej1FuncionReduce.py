from functools import reduce
def suma(a,b):
    return a+b
lista = [1,2,3,4,5,6,7,8,9,10] 
lista_suma = reduce(suma,lista)
print(lista_suma)