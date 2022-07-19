list=[]
count=1


print("-Introduce 5 notas del alumno de 0 a 10-")
while count <=5: 
    adlist = float(input ("Dame la nota:"))
    list.append(adlist)
    count+=1
suma=sum(list)
prom=suma/5
print("Las notas del alumno son: ", list)
print("Su promedio es: ", prom)
print("Su maxima nota es: ", max(list))
print("su minima nota es: ", min(list))