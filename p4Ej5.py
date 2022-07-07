
count=1
alumnos={}
listaCalif=[]

print("-Crea La lista de alumnos con sus calificacines-")
n=int(input("¿Cuantos alumnos vas a registrar?:"))
while count<=n: #poner 2 puntos
    nom=input("Introduce el nombre del alumno: ")
    otro=True
    while count>1:
        nom2=nom
        if (nom1==nom2):
            print("Este nombre ya fue guardado, inicia de nuevo")
            otro=False
            break
        else:
            break
    if otro==True:
        c2=1
        listaCalif=[]
        while c2>=0:
            calif=float(input("Dame su califiacion(para salir pon un numero negativo): "))
            if calif>0:
                listaCalif.append(calif)
            c2=calif
        nom1=nom
    elif otro==False:
        break
    count+=1
    alumnos[nom]=listaCalif

print("Tu registro de alumnos con calificaciones es:",alumnos)
list1=list(alumnos.keys())
# para ver si corre print(list1)
for i in range (0,n):
    print("El alumno: ", list1[i], end="")
    lista2=(alumnos[list1[i]])
    #para ver si corre print(lista2)
    suma=(sum(lista2))
    prom=suma/(len(lista2))
    print(", saco en promedio: ", prom )