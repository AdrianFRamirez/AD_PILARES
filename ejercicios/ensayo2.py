print("Programa que muestra en pantalla hasta los números primos que le indiques. ")

num=int(input("¿Cuantos numeros primos quieres ver?: "))
cont=1
nPrimos=[]
lonLista=len(nPrimos)
a=0 

if (num==0):
        print("No tiene numeros primos")
elif(num>0):
    print("Los numeros primos que indicaste son: ")
    while (lonLista < num):
        if (cont<2):
            primo=False
        elif(cont>=2):    
            for inc in range(1, cont):
                if((cont%inc)==0):
                    a=a+1
            if(a!=2):
                primo=False
            else:
                primo=True
        if (primo==True):
            nPrimos.append(cont)
            cont+=1
            lonLista=len(nPrimos)
            int(lonLista)
        else:
            cont +=1
    print(nPrimos[:])
else:
    print("Indica solo numeros positivos")

