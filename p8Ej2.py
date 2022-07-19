#Adrian Felipe Ramirez Mendoza
#Folio 964ND09
#Practica 8 Métodos de los objetos Ejercicio 2
#Creacion de un programa que lea una cadena y devuelva un diccionario con aparciones del caracter
#forma normal
cadena1= input("Introduce un enunciado: ")
"""dicct1={}
for caracter in cadena1:
    dicct1[caracter]=cadena1.count(caracter)
print(dicct1)"""

#con comprension de diccionarios
dicct2={caracter:cadena1.count(caracter) for caracter in cadena1}
print(dicct2)