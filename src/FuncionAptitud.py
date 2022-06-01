# Esta clase se encarga de construir mediante parametros, ya sean seteados para testear o obtenidos del usuario, para armar la funcion aptitud del calculo de atraccion a un libro/individuo.

from pandas import Series


class FuncionAptitud:
    def __init__(self):
        self.autor = None
        self.titulo = None
        self.genero = None
        self.calificacion = None
        self.publicador = None
        self.porcentaje_aprobacion = None

    def set_autor(self, autor):
        self.autor = autor

    def set_titulo(self, titulo):
        self.titulo = titulo

    def set_genero(self, genero):
        self.genero = genero

    def set_calificacion(self, calificacion):
        self.calificacion = calificacion

    def set_publicador(self, publicador):
        self.publicador = publicador

    def set_porcentaje_aprobacion(self, porcentaje_aprobacion):
        self.porcentaje_aprobacion = porcentaje_aprobacion

    def evaluar(self, individuo: Series) -> float:
        # contar vocales en titulo
        # return individuo["titulo"].str.count("a") + individuo["titulo"].str.count("e") + individuo["titulo"].str.count("i") + individuo["titulo"].str.count("o") + individuo["titulo"].str.count("u")

        # el titulo mas largo
        return individuo["titulo"].str.len()
