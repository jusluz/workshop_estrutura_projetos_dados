import pandas as pd

from src.pipeline.transform import concat_data_frames

"""
Função pata testar a função concat_data_frames
"""


def testar_concatenacao_da_lista_de_dataframe():

    arrange = pd.concat(
        [pd.DataFrame({'a': [1, 2, 3]}), pd.DataFrame({'a': [4, 5, 6]})],
        ignore_index=True,
    )

    act = concat_data_frames(
        [pd.DataFrame({'a': [1, 2, 3]}), pd.DataFrame({'a': [4, 5, 6]})]
    )

    assert act.equals(arrange)
