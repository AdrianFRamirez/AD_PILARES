def pares(n):
    for numero in range(n+1):
        if numero%2==0:
            yield numero
pares(10)

print([numero for numero in pares(10)])