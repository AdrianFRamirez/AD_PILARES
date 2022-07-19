print("Programa para imprimir un patron triangular")
def mTriangulo(n,Simbolo):
    for fila in range(1,n+1):
        for colu in range(1,fila+1):
            print(Simbolo,end=" ")
        print()

n=int(input("Dame el numero de filas para el medio triangulo:"))
S=input("Dame el simbolo de un caracter que quieres ver: ")

print("Tu triangulo se ve: ")
mTriangulo(n,S)