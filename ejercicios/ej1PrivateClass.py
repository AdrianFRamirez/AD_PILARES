class Humano:
    def __init__ (self, nombre, edad):
        self.nombre= nombre
        self.edad= edad
        self.valEdad()
        
        
    @ property #se declara funcioin de consulta-getter
    def Nombre (self):
        return self.nombre

    @Nombre.setter #se declara funcion de manipular dato
    def Nombre (self, nuevoNombre):
        self.nombre= nuevoNombre
    @property
    def Edad(self):
        return self.edad
    
    @Edad.setter
    def Edad(self,nuevaEdad):
        self.edad=nuevaEdad
        self.valEdad()

    def valEdad(self):
        if (self.edad>18):
            print("Tiene mayoria de edad")
        else:
            print("No tiene mayoria de edad")

persona1= Humano("Adrian", 35)
print(persona1.Nombre)
persona1.Nombre= "Juan"
print(persona1.Nombre)
print(persona1.Edad)
persona1.Edad= 5
print(persona1.Edad)