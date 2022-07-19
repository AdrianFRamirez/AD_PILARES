n=int(input("Dame el numero de filas para hacer un patron de medio triangulo:"))
for fila in range(1,n+1):
    for colu in range(1,fila+1):
        print("*",end=" ")
    print()