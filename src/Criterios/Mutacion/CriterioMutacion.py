from pandas import DataFrame, Series


# TODO Definir un tipo de CriterioMutacion

# Simple
# Adaptativa por Convergencia
# Adaptativa por Temperatura
# Ascendente
# Descendente
from src.FuncionAptitud import FuncionAptitud


class CriterioMutacion:
    def mutar(self, individuo: DataFrame) -> DataFrame:
        return individuo


class MutaSimple(CriterioMutacion):
    def mutar(self, individuo: DataFrame, dataset: DataFrame) -> DataFrame:
        # set titulo a Mutado
        individuo = dataset.sample(n=1)
        individuo.reset_index(drop=True, inplace=True)
        return individuo.iloc[0]
        # individuo["titulo"] = "Mutado"
        # return individuo

class MutaOrdenada(CriterioMutacion):

    def mutar(self, individuo: DataFrame, dataset: DataFrame) -> DataFrame:
        # set titulo a Mutado
        id = individuo["ID"].copy()
        id_actual = dataset.loc[dataset["ID"] == id].index.values[0]
        dataset = dataset.iloc[[id_actual - 1, id_actual + 1]]
        dataset.sort_values(by=['aptitud'], inplace=True, ignore_index=True)
        return dataset.iloc[0]
        # individuo["titulo"] = "Mutado"
        # return individuo
