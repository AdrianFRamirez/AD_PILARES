count=1
list4=[]
adtupla=()
print("-Crea una lista de usuarios introduciendo Nombre y edad-")
while count==1: #poner 2 puntos
    
    nom = str( input ("Agrega un Nombre: "))
    edad = int (input ("Agrega la edad: "))
    adtupla = (nom,edad)
    tuple(adtupla)
    list4.append(adtupla)
    count= int( input("¿Quieres agregar otro Nombre y edad? 1 para otro /2 para salir: "))
   
print("Tus Usuarios son:", list4)
