#Adrian Felipe Ramirez Mendoza
#Folio 964ND09
#Practica 7 POO Ejercicio 2
#Construccion de metodos en clase Cuenta
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


persona1=Cuenta("Adrian",500)

persona1.mostrar()
persona1.ingresar(20)
persona1.mostrar()
persona1.retirar(800)
persona1.mostrar()
