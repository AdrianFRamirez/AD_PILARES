def div(a,b):
    try:
        return a/b
    except:
        print("No se puede dividir entre 0")
        
def div2(a,b):
    try:
        return a/b
        
    except ZeroDivisionError: #ZeroDivisionError se sabe que da ese error, entonces en ese caso que aparesca exactamente ese error se pone el print
        print("No se puede dividir entre 0")
    

div(1,0)

div2(1,0)