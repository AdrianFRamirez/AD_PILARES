
"""#ejemplos funciones
def swap(x, y):
    temp = x
    x = y
    y = temp
    return x,y
 
# Driver code
x = 2
y = 3
print(swap(x, y))
print()
print(x)
print(y)"""

def numeros():
    a=33
    b=45
    return a,b


print(numeros())

def multiplicacion(fun):
    a,b=fun()
    c=a*b
    print(c)

multiplicacion(numeros)