import random 
count=1
list2=[]
suma=[]
while count <=10: #poner 2 puntos
    list2.append(random.randint(0,100))
    count+=1
    
print("La lista es; ", list2)
print("La suma es: ", sum(list2))

