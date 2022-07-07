print("-Programa para que calcule cuanto se paga de 20 meses, mensualmete-")

meses = 20
cont= 1
montoF=10
monto = int
accl= 0
print("Lo que paga cada mes es:")
while (cont<=meses):
    monto=montoF*cont
    accl = accl+monto
    print("El mes:", cont, end="")
    print(", pagaste: ",monto)
    cont+=1
print("Al final de los 20 meses pagaste: ", accl)