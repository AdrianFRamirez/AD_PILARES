def es_par(numero):
    if numero%2==0:
        return numero
    else:
        pass

lista = [1,2,3,4,5,6,7,8,9,10]

lista_par = list(filter(es_par,lista)) #poner tipo list para evitar que regrese como tipo filtro
print(lista_par)