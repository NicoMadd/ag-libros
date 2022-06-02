# TODO Definir un tipo de CriterioDeParo

# Cantidad de Vueltas
# Tiempo Transcurrido
# f(Ix)>Valor
# Promedio [f(Ix)] ≈ Valor

import time


class CriterioDeParo:

    def iniciar(self):
        pass

    def parar(self, poblacion) -> bool:
        return True


class CantidadDeVueltas(CriterioDeParo):
    def __init__(self, cantidad_vueltas=5):
        self.cantidad_vueltas = cantidad_vueltas
        self.vueltas = 0

    def parar(self, poblacion) -> bool:
        self.vueltas += 1
        # print("Vuelta:", self.vueltas)
        return self.vueltas >= self.cantidad_vueltas

# Tiempo transcurrido en segundos


class TiempoTranscurrido(CriterioDeParo):
    def __init__(self, tiempo_minimo=5*1e9):
        self.tiempo_minimo = tiempo_minimo

    def iniciar(self):
        self.tiempo_inicial = time.perf_counter_ns()
        print("Tiempo Inicial:", self.tiempo_inicial)

    def parar(self, poblacion) -> bool:
        self.tiempo = time.perf_counter_ns() - self.tiempo_inicial
        if self.tiempo >= self.tiempo_minimo*1e9:
            print("Tiempo Minimo:", f'{self.tiempo_minimo}s')
            print("Tiempo Transcurrido:", f'{self.tiempo/1e9}s')
            return True
        else:
            return False


class AptitudMayorA(CriterioDeParo):
    def __init__(self, valor_minimo=0.0):
        self.valor_minimo = valor_minimo

    def parar(self, poblacion) -> bool:
        return poblacion['aptitud'].max() >= self.valor_minimo
