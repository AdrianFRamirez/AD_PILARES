#Adrian Felipe Ramirez Mendoza
#Folio 964ND09
#Practica 7 POO Ejercicio 1
#Construccion de metodos en clase Persona
class Persona:
    def __init__ (self,nombre,edad,dni):
        self.nombre= nombre
        self.edad= edad
        self.dni= dni


    @property
    def Nombre(self):
        return self.nombre
    
    @Nombre.setter
    def Nombre(self,nombre):
        self.nombre=nombre
        
    @property
    def Edad(self):
        return self.edad
    
    @Edad.setter
    def Edad(self,edad):
        self.edad=edad
        self.valEdad()
    @property
    def DNI(self):
        return self.dni
    
    @DNI.setter
    def DNI(self,dni):
        self.dni=dni
        self.valDNI()

    def valDNI(self):
        tipo= type(1)
        if(type(self.dni)==tipo and len(str(self.dni))<=10):
            print("Tu ID es valido")
        else:
            print("Tu ID no es valido, revisalo e intenta de nuevo")
            self.dni= 0

    def valEdad(self):
        if(self.edad>0):
            print("Edad Valida")
        else:
            print("Edad invalida")
            self.edad= 0

    def mostrar(self):
        print("Nombre de la persona:", self.nombre, ", Edad:",self.edad,", DNI:",self.dni)
    
    def esMayorDeEdad(self):
        Medad=self.edad>=18
        print("¿Es mayor de 18?:", Medad)

persona1=Persona("Adrian",35,98765)

persona1.mostrar()
persona1.esMayorDeEdad()
print()
persona1.DNI="458ouit"
persona1.Edad=20
persona1.mostrar()
