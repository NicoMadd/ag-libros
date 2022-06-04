from FuncionAptitud import FuncionAptitud
from dataset import generos, fechas, rangos_de_paginas, precios, idiomas


class Interfaz:

    def selectOption(self, options: list, title: str = None, values: list = None) -> str:
        """
        Select an option from a list of options.
        """
        while True:
            for i, option in enumerate(options):
                print("{}. {}".format(i + 1, option))
            print("{}. {}".format(len(options) + 1, "No Considerar"))
            #print(len(options) + 1, "No Considerar")
            label = "Seleccione una opcion: " if title is None else f"Seleccione {title}: "
            option = input(label)
            try:
                option = int(option)
                if option in range(1, len(options) + 1):
                    if values is None:
                        return options[option - 1]
                    else:
                        return values[option - 1]
                elif option == len(options) + 1:
                    return None
            except ValueError:
                pass
            print("Opcion invalida")

    def confirmOptions(self) -> bool:
        answer = None
        while True:
            print("\nGenero: {}\nPrecio: {}\nCantidad de paginas: {}\nFecha de publicacion: {}\nIdioma: {}".format(
                self.genero, self.precio, self.cantidad_paginas, self.fecha_publicacion, self.idioma))
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
            self.genero = self.selectOption(generos, "Genero")
            self.precio = self.selectOption(precios, "Precio")
            self.cantidad_paginas = self.selectOption(
                rangos_de_paginas, "Cantidad de paginas")
            self.fecha_publicacion = self.selectOption(
                fechas, "Fecha de publicacion")
            self.idioma = self.selectOption(idiomas, "Idioma")
            if self.confirmOptions():
                break
        return FuncionAptitud(genero=self.genero, precio=self.precio, cantidad_paginas=self.cantidad_paginas, fecha_publicacion=self.fecha_publicacion, idioma=self.idioma)


if __name__ == "__main__":

    interfaz = Interfaz()
    interfaz.getFuncionAptitud()
