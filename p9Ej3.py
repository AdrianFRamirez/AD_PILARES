#Adrian Felipe Ramirez Mendoza
#Folio 964ND09
#Practica 9 Programación Funcinal Ejercicio 3
#Obtener elementos mayores a 5 en tupla
def may5():
    tupla = (5,2,6,7,8,10,77,55,2,1,30,4,2,3)
    print(tuple(i for i in tupla if i>5))
may5()