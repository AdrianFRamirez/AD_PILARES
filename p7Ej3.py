#Adrian Felipe Ramirez Mendoza
#Folio 964ND09
#Practica 7 POO Ejercicio 2
#Construccion de metodos en clase Cuenta Joven-super clase
class Cuenta:
    def __init__ (self,titular, cantidad=0):
        self.__titular= titular
        self.__cantidad= float(cantidad)
    @property
    def Titular(self):
        return self.__titular
    @Titular.setter
    def Titular(self,titular):
        self.__titular= titular
    @property 
    def Cantidad(self):
        return self.__cantidad
    
    @Cantidad.setter
    def Cantidad(self,cantidad=0):
        self.__cantidad= float(cantidad)
        self.valEdad()
    
    def mostrar(self):
        print("Nombre:", self.__titular, ", Estado de cuenta:",self.__cantidad,)
  
    def ingresar(self,cantidad):
        if cantidad>0:
            self.__cantidad=self.__cantidad+float(cantidad)
                
    def retirar(self,cantidad):
        if cantidad>0:
            self.__cantidad=self.__cantidad-float(cantidad)

class CuentaJoven(Cuenta):

    def __init__ (self,titular,edad, cantidad=0, bonificacion=0):
        self.edad=edad
        Cuenta.__init__(self,titular,cantidad)
        self.bonificacion= bonificacion  
       
    @property 
    def Bono(self):
        return self.bonificacion
    
    @Bono.setter
    def Bono(self,bonificacion):
        self.bonificacion= bonificacion
        self.valEdad()

    def TitularValido(self):
        Vedad=(self.edad>=18 and self.edad<25)
        print("¿Aplica para cuenta joven?:", Vedad)
        return Vedad
        
    def mostrar(self):
        Vedad=CuentaJoven.TitularValido(self)
        if (Vedad==True):
            print("Cuenta Joven")
        else:
            print("Cuenta Normal")
            self.bonificacion=0
        Cuenta.mostrar(self)
        print("Con bonificacion de:",self.bonificacion,"%" )
    
    def retirar(self,cantidad):
        Vedad=(self.edad>=18 and self.edad<25)
        if Vedad==True:
            Cuenta.retirar(self,cantidad)
            print("Operacion realizada con exito")
        else:
            print("Edad no valida para retirar")

persona2=CuentaJoven("Adrian",35,600,5)
persona2.mostrar()
print()
persona2.retirar(55)
persona2.mostrar()
print()
print()
persona1=CuentaJoven("Juan",22,300,5)
persona1.mostrar()
print()
persona1.retirar(20)
persona1.mostrar()

