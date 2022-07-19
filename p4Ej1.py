import random 
count=1
list=[]
listcuad=[]
listcub=[]


while count <=10: 
    list.append(random.randint(0,10))
    x=(count-1)
    listcuad.append((list[x])*(list[x]))
    listcub.append((list[x])*(listcuad[x]))
    count+=1

print("La lista es: ", list)
print("El cuadrado de la lista es: ", listcuad)
print("El cubo de la lista es: ", listcub)

