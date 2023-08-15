import os
from string import Template
import yaml
from common.base.path import Base_path
import ruamel.yaml


def read_yml(file_path, params_value=None):
    """
    read yml file
    :param params_value: assign values to variables in the file,such as :{'name':'dan'}
    :param file_path: yml file relative path
    :return: data list
    """
    with open(os.path.join(Base_path, file_path), mode='r', encoding='utf-8') as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
    if params_value is None:
        return data
    else:
        # assign values to variables in the file and return
        return eval(Template(str(data)).safe_substitute(params_value))


def write_yml(file_path, data, mode='w'):
    """
    write data to yml file
    :param file_path: yml file relative path
    :param data: should be a dict
    :param mode: 'w' open for writing, truncating the file first
                 'a' open for writing, appending to the end of the file if it exists
    :return:
    """
    with open(os.path.join(Base_path, file_path), mode=mode, encoding='utf-8') as f:
        writer = ruamel.yaml.YAML()
        # set yml format
        writer.indent(mapping=2, sequence=4, offset=2)
        writer.dump(data, f)


def clear_yml(file_path):
    """
    clear yml file content
    :param file_path: yml file relative path
    :return:
    """
    with open(os.path.join(Base_path, file_path), mode='w', encoding='utf-8') as f:
        f.truncate()
