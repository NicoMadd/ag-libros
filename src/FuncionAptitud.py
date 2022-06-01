# Esta clase se encarga de construir mediante parametros, ya sean seteados para testear o obtenidos del usuario, para armar la funcion aptitud del calculo de atraccion a un libro/individuo.

import numpy as np
from pandas import DataFrame, Series


class FuncionAptitud:
    def __init__(self, autor=None, titulo=None, genero=None, calificacion=None, publicador=None,
                 porcentaje_aprobacion=None, precio=None, cantidad_paginas=None, fecha_publicacion=None):
        self.autor = autor
        self.titulo = titulo
        self.genero = genero
        self.calificacion = calificacion
        self.publicador = publicador
        self.porcentaje_aprobacion = porcentaje_aprobacion
        self.precio = precio
        self.cantidad_paginas = cantidad_paginas
        self.fecha_publicacion = fecha_publicacion
        self.once = True

    def evaluar(self, individuo: DataFrame) -> Series:
        """
        Evalua la funcion aptitud de un individuo.
        """

        # return random float series
        return np.random.normal(0, 100, individuo.shape[0])

        # aptitud = 0
        # if(self.once == True):
        #     print(individuo)
        #     print(aptitud)
        # self.once = False
        # return aptitud
