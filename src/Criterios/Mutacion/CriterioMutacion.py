from pandas import DataFrame, Series


# TODO Definir un tipo de CriterioMutacion

# Simple
# Adaptativa por Convergencia
# Adaptativa por Temperatura
# Ascendente
# Descendente

class CriterioMutacion:
    def mutar(self, individuo: DataFrame) -> DataFrame:
        return individuo


class MutaSimple(CriterioMutacion):
    def mutar(self, individuo: DataFrame, dataset: DataFrame) -> DataFrame:
        # set titulo a Mutado
        return dataset.sample(n=1)
        # individuo["titulo"] = "Mutado"
        # return individuo
