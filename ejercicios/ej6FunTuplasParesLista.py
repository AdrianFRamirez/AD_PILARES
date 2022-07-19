print("-Crea una lista de usuarios introduciendo Nombre y edad-")
def ListaTuplas():
    count=1
    list4=[]
    adtupla=()
    while count==1: #poner 2 puntos
        nom = str( input ("Agrega un Nombre: "))
        edad = int (input ("Agrega la edad: "))
        adtupla = (nom,edad)
        tuple(adtupla)
        list4.append(adtupla)
        count= int( input("¿Quieres agregar otro Nombre y edad? 1 para otro /2 para salir: "))
    return list4
    
list4=ListaTuplas()
print("Tus Usuarios son:", list4)

#ejercicio Datos que retorna se deben de guardar como funcion