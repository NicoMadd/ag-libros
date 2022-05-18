# TODO Definir un tipo de CriterioDeParo

# Cantidad de Vueltas
# Tiempo Transcurrido
# f(Ix)>Valor
# Promedio [f(Ix)] ≈ Valor

class CriterioDeParo:
    def debeParar(self, poblacion) -> bool:
        return True


class CantidadDeVueltas(CriterioDeParo):
    def __init__(self, cantidad_vueltas=5):
        self.cantidad_vueltas = cantidad_vueltas
        self.vueltas = 0

    def parar(self, poblacion) -> bool:
        self.vueltas += 1
        # print("Vuelta:", self.vueltas)
        return self.vueltas >= self.cantidad_vueltas
