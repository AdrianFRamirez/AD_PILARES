def saludar(idioma):
    def saludar_es():
        print("Hola")
    def saludar_fr():
        print("Salut")
    def saludar_en():
        print("Hello")
        
    idioma_lista= {"es":saludar_es, "fr":saludar_fr, "en":saludar_en} #cada clave asociado al nombre de la funcion
    return idioma_lista[idioma] 
    
f= saludar("en") #se guarda la funcion en f
f()  #se ejecuta f como funcion