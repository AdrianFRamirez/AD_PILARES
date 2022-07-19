#Adrian Felipe Ramirez Mendoza
#Folio 964ND09
#Practica 8 Métodos de los objetos Ejercicio 2
#creacion de diccionario para gurdar precios de frutas, se pedira nombre fruta, cantidad vendida y precio final, debe de pedir hacer una consulta

frutas1={"Sandia":40, "Melon":35, "Platano":25, "Manzana":30}
consulta=1
while consulta==1:
    fruta=input("Que fruta quieres comprar: ")
    if fruta in frutas1:
        cant=float(input("Cuantos kilos quieres: "))
        print("Tienes que pagar:", (frutas1[fruta])*cant,", de tu fruta ", fruta)
    else:
        print("Error, fruta no encontrada")
    consulta=int(input("¿Quieres hacer otra consulta? Si/1, No/2: "))