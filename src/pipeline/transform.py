import pandas as pd

def concat_data_frames(data_frame_list):
    # Verificar se os DataFrames estão vazios
    if any(df.empty for df in data_frame_list):
        raise ValueError("DataFrames vazios não podem ser concatenados")

    # Verificar a compatibilidade de tipos de dados
    if not all(df.dtypes.equals(data_frame_list[0].dtypes) for df in data_frame_list):
        raise ValueError("Tipos de dados incompatíveis")

    # Verificar a indexação
    if not all(df.index.equals(data_frame_list[0].index) for df in data_frame_list):
        raise ValueError("Indexação incompatível")

    return pd.concat(data_frame_list, ignore_index=True)
