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

persona=Humano("Adrian",35,98765)
persona.validador()
persona.mayoriaEdad()