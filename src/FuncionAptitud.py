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

    # Deberia ser por individuo pero es por subgrupo

    def evaluar(self, individuos: DataFrame) -> Series:
        """
        Evalua la funcion aptitud de un individuo.

        por ahora solo hay precio, genero(genero y subgenero), cantidad de paginas y fecha de publicacion
        """

        precios = individuos.precio.apply(lambda x: x == self.precio)
        fechas = individuos.fechaPublicacion.apply(
            lambda x: x == self.fecha_publicacion)
        paginas = individuos.numero_paginas.apply(
            lambda x: x == self.cantidad_paginas)
        generosPrincipales = individuos.genero.apply(
            lambda x: x == self.genero)

        aptitudes = precios.astype(
            int)*10 + fechas.astype(int)*10 + paginas.astype(int)*10 + generosPrincipales.astype(int)*10
        return aptitudes

        # aptitud = 0
        # if(self.once == True):
        #     print(individuo)
        #     print(aptitud)
        # self.once = False
        # return aptitud
