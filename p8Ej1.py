#Adrian Felipe Ramirez Mendoza
#Folio 964ND09
#Practica 8 Métodos de los objetos Ejercicio 1
#Creacion de diccionario con longitud dada por el usuario y sean el cuadrado del key
#forma normal
"""n= int(input("Cuantos valores quieres meter a tu diccionario:  "))
dicct1={}
for clave in range(1,n+1):
	dicct1[clave]=clave*clave
print(dicct1)"""

#con comprension de diccionarios
n= int(input("Cuantos valores quieres meter a tu diccionario:  "))
dicct2={clave:clave*clave for clave in range(1,n+1)}
print(dicct2)