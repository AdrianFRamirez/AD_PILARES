def suma(num1, *otros): #con * se pone que en caso de que se pongan otros elementos despues de los asignados se guarden ahí
	print(num1)
	print(otros) #se guarda como tupla
suma(2,4,5,6,7,9)

  
tipo = type(1)
tipo2=type("Hola")
print(tipo)
print(tipo2)
print(tipo==tipo2)

class Humano:
    def __init__ (self,nombre,edad,ID):
        self.nombre= nombre
        self.edad= edad
        self.ID= ID

    def validador(self):
        tipo= type(1)
        if(type(self.ID)==tipo):
            print("Tu ID es valido")
        else:
            print("Tu ID no es valido, revisale intenta de nuevo")

    def mayoriaEdad(self):
        if (self.edad>18):
            print("Tienes mayoria de edad")
        else:
            print("Un no tienes mayoria de edad")    

persona=Humano("Adrian", 35 ,98765)
persona.validador()
persona.mayoriaEdad()