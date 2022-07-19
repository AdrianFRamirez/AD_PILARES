n= int(input("Cuantos valores quieres meter a tu diccionario:  "))
dicct1={}
for clave in range(0,n):
	dicct1[n]=n*n
print(dicct1)
#solo pone el ultimo digito

n= int(input("Cuantos valores quieres meter a tu diccionario:  "))
dicct2={}
for clave in range(1,n+1):
	dicct2[clave]=clave*clave
print(dicct2)
#con la clave en el [], pone cada elemento

#con comprension de lista
n= int(input("Cuantos valores quieres meter a tu diccionario:  "))
dicct2={clave:clave*clave for clave in range(1,n+1)}
print(dicct2)

cadena1= input("Introduce un enunciado: ")
#con comprensión de diccionarios
dicct2={caracter:cadena1.count(caracter) for caracter in cadena1}
print(dicct2)
#forma normal
cadena1= input("Introduce un enunciado: ")
"""dicct1={}
for caracter in cadena1:
    dicct1[caracter]=cadena1.count(caracter)
print(dicct1)"""
