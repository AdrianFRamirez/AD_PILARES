n = int(input("Dame el numero de filas para hacer un patron de triangulo invertido-espejo : "))

print("El triangulo espejo-invertido es:")
fila = 1
for fila in range(1,n+1):
        for colu in range (1,n+1):
            if(colu < fila):
                print(' ', end = '  ')
            else:
                print('*', end = '  ') 
        print()