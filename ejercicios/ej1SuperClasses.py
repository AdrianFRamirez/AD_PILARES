class Terrestre:
    def camina(self):
        print("Caminando")

class Acuatico:
    def nadar(self):
        print("Nadando")

class Cocodrilo(Terrestre, Acuatico):
    pass
godzilla=Cocodrilo()
godzilla.camina()