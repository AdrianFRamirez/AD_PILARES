#Adrian Felipe Ramirez Mendoza
#Folio 964ND09
#Practica 9 Programación Funcinal Ejercicio 1
#Crea un programa que pregunte una multiplicacion al azar 10 veces y retorne los asiertos
import random

def numAlet():
    a=random.randint(1,10)
    b=random.randint(1,10)
    return a,b
def Multi10(fun):
    print("Prueba tus habilidades de multiplicacion")
    ac=0
    for i in range(1,11):
        a,b=fun()
        c=a*b
        j=int(input(f"cuanto es {a}x{b}:"))
        if j==c:
            print("¡Correcto!")
            ac+=1
        else:
            print("incorrecto =(, la respuesta correcta es:", c)
    print("Tus aciertos fueron: ",ac," de 10")

Multi10(numAlet)
