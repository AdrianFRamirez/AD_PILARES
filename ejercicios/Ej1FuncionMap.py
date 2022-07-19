def cubo(numero):
    numero=numero**3
    return numero
lista = [1,2,3,4,5,6,7,8,9,10]   

lista_cubo = list(map(cubo,lista))
print(lista_cubo)