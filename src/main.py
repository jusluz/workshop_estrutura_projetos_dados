from pipeline.extract import extract_from_excel
from pipeline.load import load_to_excel
from pipeline.transform import concat_data_frames

if __name__ == '__main__':
    data_frame_list = extract_from_excel('./data/input')
    print(type(data_frame_list))
    data_frame = concat_data_frames(data_frame_list)
    print(type(data_frame_list))
    load_to_excel(data_frame, output_path='./data/output', file_name='output')
