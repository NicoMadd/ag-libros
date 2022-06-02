# Esta clase se encarga de construir mediante parametros, ya sean seteados para testear o obtenidos del usuario, para armar la funcion aptitud del calculo de atraccion a un libro/individuo.

import numpy as np
from pandas import DataFrame, Series

import dataset as ds


class FuncionAptitud:
    def __init__(self, autor=None, titulo=None, genero=None, calificacion=None, publicador=None,
                 porcentaje_aprobacion=None, precio=None, cantidad_paginas=None, fecha_publicacion=None, idioma=None):
        self.autor = autor
        self.titulo = titulo
        self.genero = genero
        self.idioma = idioma
        self.calificacion = calificacion
        self.publicador = publicador
        self.porcentaje_aprobacion = porcentaje_aprobacion
        self.precio = precio
        self.cantidad_paginas = cantidad_paginas
        self.fecha_publicacion = fecha_publicacion
        self.ppc = 200

    def __str__(self) -> str:
        return "\nIdioma: " + str(self.idioma) + "\nGenero: " + str(self.genero) + "\nPrecio: " + str(self.precio) + "\nCantidad de paginas: " + str(self.cantidad_paginas) + "\nFecha de publicacion: " + str(self.fecha_publicacion)

    def evaluar_buscado_en_conjunto(self, actual: str, conjunto: list, buscado: str, exacto: bool = False, rechazo: float = 0, aceptacion_parcial: float = 0.5) -> float:
        if(buscado is None or actual is None):
            return rechazo
        try:
            indiceActual = conjunto.index(actual)
        except ValueError as e:
            return rechazo
        indiceBuscado = conjunto.index(buscado)
        # si es el mismo devuelve ppc, si no se fija si es uno adyacente. Si lo es, devuelve ppc*0.5
        valor = self.ppc if indiceActual == indiceBuscado else self.ppc * \
            aceptacion_parcial if abs(
                indiceActual - indiceBuscado) == 1 and exacto is False else rechazo
        return valor

    def evaluar_precios(self, iterado: str) -> float:
        return self.evaluar_buscado_en_conjunto(iterado, ds.precios, self.precio)

    def evaluar_cantidad_paginas(self, iterado: str) -> float:
        return self.evaluar_buscado_en_conjunto(iterado, ds.rangos_de_paginas, self.cantidad_paginas)

    def evaluar_fecha_publicacion(self, iterado: str) -> float:
        return self.evaluar_buscado_en_conjunto(iterado, ds.fechas, self.fecha_publicacion)

    def evaluar_genero(self, iterado: str) -> float:
        return self.evaluar_buscado_en_conjunto(iterado, ds.generos, self.genero)

    def evaluar_idioma(self, iterado: str) -> float:
        return self.evaluar_buscado_en_conjunto(iterado, ds.idiomas, self.idioma, exacto=True, rechazo=-500)

    def evaluar(self, individuos: DataFrame) -> Series:
        """
        Evalua la funcion aptitud de un individuo.

        por ahora solo hay precio, genero(genero y subgenero), cantidad de paginas y fecha de publicacion
        """

        precios = np.vectorize(self.evaluar_precios)(individuos.precio)
        fechas = np.vectorize(self.evaluar_fecha_publicacion)(
            individuos.fechaPublicacion)
        paginas = np.vectorize(self.evaluar_cantidad_paginas)(
            individuos.numero_paginas)
        generosPrincipales = np.vectorize(self.evaluar_genero)(
            individuos.genero)
        generosSecundarios = np.vectorize(
            self.evaluar_genero)(individuos.subgenero)
        idioma = np.vectorize(self.evaluar_idioma)(individuos.idioma)

        aptitudes = precios + \
            fechas + paginas + \
            generosPrincipales + generosSecundarios + idioma
        return aptitudes
