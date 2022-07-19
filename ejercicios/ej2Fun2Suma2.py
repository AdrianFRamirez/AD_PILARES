print("--Programa que suma con argumentos y no afecta variables globales--")
res=0
def sumaDos(x,y):
	res=x+y
	print("La suma es: ", res)

a=int (input("Dame un Numero: "))
b=int (input("Dame otro numero: "))
sumaDos(a,b)
print("Valor de la variable global con el mismo nombre: ", res)