count=1
list3=[]
adlist=[]

while count==1: #poner 2 puntos

    adlist = (input ("Dame un dato para guardarlo en la lista:"))
    list3.append(adlist)
    count= int( input("¿Quieres agregar otro dato a tu lista? 1 para otro dato/2 para salir: "))
   

print("Tu lista es:", list3)