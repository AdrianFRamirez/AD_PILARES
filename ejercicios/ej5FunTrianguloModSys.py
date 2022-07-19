import sys
x=int(sys.argv[1])
y=sys.argv[2]
print("Programa para imprimir un patron triangular")
def mTriangulo(x,y):
    for fila in range(1,x+1):
        for colu in range(1,fila+1):
            print(y,end=" ")
        print()

print("Tu triangulo se ve: ")
mTriangulo(x,y)