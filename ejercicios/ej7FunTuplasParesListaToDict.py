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
def ListToDicc():
    DictNom={}
    cont2=0
    while cont2<(len(list4)):
        DictNom[cont2+1]=list4[cont2]
        cont2 += 1
    print("Tu diccionario es:", DictNom)
    return DictNom
convert=int(input("¿Quieres convertir a diccionario? 1=Si/2=No: "))
if convert==1:
    ListToDicc()
else:
    print("Fin del programa")