import os

import pandas as pd


def load_to_excel(
    data_frame: pd.DataFrame, output_path: str, file_name: str
) -> str:

    """
    Função para receber um data frame e salvar como excel

    args: data_frame (pd.DataFrame): data frame a ser salvo como excel
    output_path (str): nome do arquivo de saída
    file_name (str): nome do arquivo de saída
    """

    if not os.path.exists(output_path):
        os.makedirs(output_path)

        data_frame.to_excel(f'{output_path}/{file_name}.xlsx', index=False)

    return 'Arquivo salvo com sucesso'
