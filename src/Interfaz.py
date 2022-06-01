from FuncionAptitud import FuncionAptitud
from dataset import generos, fechas, rangos_de_paginas, precios


class Interfaz:

    def selectOption(self, options):
        """
        Select an option from a list of options.
        """
        while True:
            for i, option in enumerate(options):
                print("{}. {}".format(i + 1, option))
            option = input("Seleccione una opcion: ")
            try:
                option = int(option)
                if option in range(1, len(options) + 1):
                    return options[option - 1]
            except ValueError:
                pass
            print("Opcion invalida")

    def confirmOptions(self) -> bool:
        answer = None
        while True:
            print("\nGenero: {}\nPrecio: {}\nCantidad de paginas: {}\nFecha de publicacion: {}".format(
                self.genero, self.precio, self.cantidad_paginas, self.fecha_publicacion))
            answer = input("Confirmar opciones? (y/n): ")
            if answer == "y" or answer == "n":
                break
            else:
                print("Opcion invalida. y/n")
                continue
        return answer == "y"

    def getFuncionAptitud(self):
        # pedir entrada de usuario para setear genero, subgenero, precio,calificacion, cantidad de paginas, fecha de publicacion, porcentaje de aprobacion
        while True:
            self.genero = self.selectOption(generos)
            self.precio = self.selectOption(precios)
            self.cantidad_paginas = self.selectOption(rangos_de_paginas)
            self.fecha_publicacion = self.selectOption(fechas)
            if self.confirmOptions():
                break
        return FuncionAptitud(genero=self.genero, precio=self.precio, cantidad_paginas=self.cantidad_paginas, fecha_publicacion=self.fecha_publicacion)


if __name__ == "__main__":
    interfaz = Interfaz()
    interfaz.getFuncionAptitud()
