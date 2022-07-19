try:
    #forzamos excepción
    x= 2/0
except:
    #Se entra ya que ha habido una excepción
    print("Entra en except, ha ocurrido una excepción")
finally:
    #Tambien entra porque finally es ejecutado siempre
    print("Entra en finally, se ejecuta el bloque finally")
    
#Entra en except, ha ocurrido una excepción
#Entra en finally, se ejecuta el bloque finally