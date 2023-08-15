import os
from string import Template
import pandas as pd
from common.base.path import Base_path


def read_csv(file_path, params_value=None):
    """
    read csv file
    :param file_path: csv file relative path
    :param params_value: assign values to variables in the file,should be a dict
    :return: return a list
    """
    data_list = []
    with open(os.path.join(Base_path, file_path), 'r', encoding='utf-8-sig') as f:
        data = pd.read_csv(f, encoding='utf-8').fillna("")
    data_len = data.__len__()
    for i in range(0, data_len):
        data_list.append(data.iloc[i].to_dict())
    if params_value is None:
        return data_list
    else:
        return eval(Template(str(data_list)).safe_substitute(params_value))


def write_csv(file_path, data: dict, value_is_array=False):
    """
    write data to csv file
    :param file_path:  csv file relative path
    :param data:  should be a dict
    :param value_is_array: if the written value is a list,please set it to True;
                           Then it will write several rows data;
    :return:
    """
    if value_is_array:
        index = None
    else:
        index = [0]
    dataframe = pd.DataFrame(data, index=index)
    dataframe.to_csv(os.path.join(Base_path, file_path), mode='w', index=False, encoding='utf-8-sig')


def clear_csv(file_path):
    """
    clear csv file data
    :param file_path: csv file relative path
    :return:
    """
    with open(os.path.join(Base_path, file_path), mode='w', encoding='utf-8') as f:
        f.truncate()
if __name__ == '__main__':
    api_data = read_csv("test_data/api/example/postAddDepartmentData.csv", {'name': 'guangzhou', 'name_en': 'test'})
    print(api_data)