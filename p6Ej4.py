print("Programa que calcula el factoial")
cont=1
accl=1
num= int(input("Dame un numero entero: "))

if(num==0):
    print("El factorial es 1")
elif (num==1):
    print("El factorial es 1")
elif(num>1):
    while(cont<=num):
        accl=accl*cont
        cont+=1
    print("El factorial es: ", accl)
else:
    print("No es un numero")
