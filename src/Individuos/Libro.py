# TODO Definir Libro

from Individuos.Individuo import Individuo


class Libro(Individuo):

    def __init__(self, titulo, autor, numero_paginas):
        self.titulo = titulo
        self.autor = autor
        self.numero_paginas = numero_paginas

    def __str__(self):
        return "Titulo: {}, Autor: {}, Numero de paginas: {}".format(self.titulo, self.autor, self.numero_paginas)

    def __repr__(self):
        return self.__str__()
