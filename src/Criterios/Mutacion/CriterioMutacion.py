from pandas import DataFrame, Series


# TODO Definir un tipo de CriterioMutacion

# Simple
# Adaptativa por Convergencia
# Adaptativa por Temperatura
# Ascendente
# Descendente
from FuncionAptitud import FuncionAptitud


class CriterioMutacion:
    def mutar(self, individuo: Series) -> Series:
        return individuo


class MutaSimple(CriterioMutacion):
    def mutar(self, individuo: Series, dataset: DataFrame) -> Series:
        # set titulo a Mutado
        individuo = dataset.sample(n=1)
        individuo.reset_index(drop=True, inplace=True)
        return individuo.iloc[0]
        # individuo["titulo"] = "Mutado"
        # return individuo


class MutaOrdenada(CriterioMutacion):

 # A partir del indice del individuo, traer el anterior y su siguiente.
 # elegir el que tenga mayor aptitud y sustituirlo por el individuo.

    def mutar(self, individuo: Series, dataset: DataFrame) -> Series:
        id_actual = dataset.loc[dataset["ID"]
                                == individuo["ID"]].index.values[0]
        vecinos = dataset.iloc[[id_actual - 1, id_actual + 1]]
        vecinos.sort_values(by=['aptitud'], inplace=True,
                            ignore_index=True, ascending=False)
        return vecinos.iloc[0]
