import sys
x=int(sys.argv[1])
y=int(sys.argv[2])
print("--Programa que suma con argumentos Directo desde comando--")

def sumaDos(x,y):
	res=x+y
	print("La suma es: ", res)

sumaDos(x,y)
