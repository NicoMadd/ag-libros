from pandas import DataFrame

# TODO Definir un tipo de CriterioSeleccion

## Metodos ##
## Torneo, Ranking, Ruleta, Control sobre numero esperado ##


class CriterioSeleccion:
    def seleccionar(self, poblacion: DataFrame) -> DataFrame:
        return poblacion
