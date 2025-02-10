import os # Biblioteca para manipular arquivos e pastas
import glob # Bilioteca para listar arquivos

import pandas as pd # Biblioteca para manipulação de Data Frame
from typing import List
import openpyxl

'''
Função para ler arquivos da pasta data/input e retornar uma lista de Data Frames

args: input_path (str): caminho da pasta com os arquivos

return lista de Data frames
'''
def extract_from_excel(path: str) -> List[pd.DataFrame]:
    # Listar todos os arquivos .xlsx na pasta
    all_files = glob.glob(os.path.join(path, "*.xlsx"))
    
    data_frame_list = []
    for file in all_files:
        # Ler o arquivo .xlsx e converter em Data Frame
        data = pd.read_excel(file)
        data_frame_list.append(data)
        
    return data_frame_list

if __name__ == "__main__":
    data_frame_list = extract_from_excel(path="./data/input")
    print(data_frame_list)