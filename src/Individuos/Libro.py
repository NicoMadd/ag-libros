# TODO Definir Libro

from Individuos.Individuo import Individuo


class LibroAPI(Individuo):

    def __init__(self, numero_paginas, ratings, precio, fechaPublicacion):
        self.numero_paginas = numero_paginas
        self.ratings = ratings
        self.precio = precio
        self.fechaPublicacion = fechaPublicacion

    def __str__(self) -> str:
        return f"paginas:{self.numero_paginas} ratings:{self.ratings} precio:{self.precio} fechaPublicacion:{self.fechaPublicacion}"

    def __repr__(self):
        return self.__str__()
