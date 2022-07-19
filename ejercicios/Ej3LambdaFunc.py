from functools import reduce
lista = [1,2,3,4,5,6,7,8,9,10] 
print(list(filter(lambda numero:numero%2==0,lista)))
print(list(map(lambda numero:numero**3,lista)))
print(reduce(lambda a,b:a+b, lista))