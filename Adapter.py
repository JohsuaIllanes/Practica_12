class EnchufeEuropeo:
    def conectar(self):
        return "Conectado a enchufe europeo"

class EnchufeAmericano:
    def plug_in(self):
        return "Plugged into American socket"

class AdaptadorEuropeo:
    def __init__(self, americano):
        self.americano = americano

    def conectar(self):
        return self.americano.plug_in()

# Uso
americano = EnchufeAmericano()
adaptador = AdaptadorEuropeo(americano)
print(adaptador.conectar())
