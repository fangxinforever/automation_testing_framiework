import os
from string import Template
import pandas as pd
from common.base.path import Base_path


def read_excel(file_path, params_value=None,sheet_name=None,):
    """
    read excel file
    :param file_path: excel file relative path
    :param params_value: assign values to variables in the file,should be a dict
    :param sheet_name: default is read all sheet;
                       can be sheetIndex, 0 is first sheet,1 is second sheet...
                       can be sheetName
                       can be a list which include several sheetIndex or sheetName,
                       such as :["sheet1Name","sheet2Name"] or [0,1]
    :return: return a list
    """
    data_list = []
    if sheet_name is None or isinstance(sheet_name, list):
        sheet_data = []
        sheet_data_pd = pd.read_excel(os.path.join(Base_path, file_path), sheet_name=sheet_name)
        sheet_names = sheet_data_pd.keys()
        for sheet_name in sheet_names:
            sheet_data.append(sheet_data_pd[sheet_name])
        data = pd.concat(sheet_data).fillna("")
    else:
        data = pd.read_excel(os.path.join(Base_path, file_path), sheet_name=sheet_name).fillna("")
    data_len = data.__len__()
    for i in range(0, data_len):
        data_list.append(data.iloc[i].to_dict())
    if params_value is None:
        return data_list
    else:
        return eval(Template(str(data_list)).safe_substitute(params_value))


def write_excel(file_path, data: dict, value_is_array=False):
    """
    write data to excel file
    :param file_path:  excel file relative path
    :param data:  should be a dict
    :param value_is_array: if the written value is an array,please set it to True;
                           Then it will write several rows data;
    :return:
    """
    if value_is_array:
        index = None
    else:
        index = [0]
    dataframe = pd.DataFrame(data, index=index)
    dataframe.to_excel(os.path.join(Base_path, file_path), index=False)


def clear_excel(file_path):
    """
    clear excel file data
    :param file_path: excel file relative path
    :return:
    """
    write_excel(file_path, {})