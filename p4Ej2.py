list=[]
count=1
adlist=[]
list2=[]
print("-Introduce 5 cadenas de caracter a continuacion-")
while count <=5: 
    adlist = (input ("Dame un texto:"))
    list.append(adlist)
    count+=1

list2=sorted(list)
list2.reverse()
print("Tu lista invertida es: ", list2)
