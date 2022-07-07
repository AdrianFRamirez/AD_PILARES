print("-Programa que recibe el monto de un préstamo y el interés mensual-")

prestamo= float(input("Dame el monto de tu prstamo: "))
interesMen= float(input("Dame el interes sin el %: "))

if (interesMen>30):
    print("Error el interes es muy alto, intentalo de nuevo")
else:
    interDeci=interesMen/100
    
    importeTotal=prestamo*(1+interDeci)
    print("Tu importe total es: ", importeTotal)