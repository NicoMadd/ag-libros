from pandas import DataFrame


# TODO Definir un tipo de CriterioMutacion

# Simple
# Adaptativa por Convergencia
# Adaptativa por Temperatura
# Ascendente
# Descendente

class CriterioMutacion:
    def mutar(self, poblacion: DataFrame) -> DataFrame:
        return poblacion
