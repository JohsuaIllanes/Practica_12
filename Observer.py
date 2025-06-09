class Sujeto:
    def __init__(self):
        self.observadores = []
        self.estado = None

    def agregar(self, obs):
        self.observadores.append(obs)

    def notificar(self):
        for obs in self.observadores:
            obs.actualizar(self.estado)

    def cambiar_estado(self, estado):
        self.estado = estado
        self.notificar()

class Observador:
    def actualizar(self, estado):
        print(f"Observador notificado. Estado nuevo: {estado}")

# Uso
sujeto = Sujeto()
obs1 = Observador()
obs2 = Observador()

sujeto.agregar(obs1)
sujeto.agregar(obs2)

sujeto.cambiar_estado("ACTIVO")
