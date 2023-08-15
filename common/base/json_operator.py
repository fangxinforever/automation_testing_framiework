import json
from string import Template
from jsonpath import jsonpath
from jsonpath_ng import parse
from common.base.logger import LogFileOperation
LOGGER = LogFileOperation().logger


class JsonOperation(object):

    def json_dumps(self, python_data=None):
        """
        serialization data
        :param: python type data
        :return: json type data
        """
        try:
            if python_data is not None:
                return json.dumps(python_data)
            else:
                LOGGER.info("parameter python_data shouldn't be None")
        except Exception as e:
            LOGGER.exception(e)
            LOGGER.info("exception occurred, reason-->{}".format(e))

    def json_loads(self, json_data=None):
        """
        deserialization data
        :param json_data: json type data
        :return: python type data
        """
        try:
            if json_data is not None:
                return json.loads(json_data)
            else:
                LOGGER.info("parameter json_data shouldn't be None")
        except Exception as e:
            LOGGER.exception(e)
            LOGGER.info("exception occurred, reason-->{}".format(e))

    def read_json_file(self, json_file=None, mode='r'):
        """
        read json from file-like object
        :param json_file: file including json type data
        :param mode: file open mode,default value is only read
        :return: python type data
        """
        try:
            with open(json_file, mode) as fp:
                return json.load(fp)
        except Exception as e:
            LOGGER.exception(e)
            LOGGER.info("exception occurred, reason-->{}".format(e))

    def write_json_file(self, python_data=None, json_file=None, mode='w', indent=4):
        """
        write json into file-like object
        :param python_data: python type data
        :param json_file: file including json type data
        :param mode: file open mode,default value is only write
        :param indent: non-negative integer, JSON will be pretty-printed with that indent level
        :return: None, write json into file successfully
        """
        try:
            with open(json_file, mode) as fp:
                if python_data is not None:
                    return json.dump(python_data, fp, indent=indent)
                else:
                    LOGGER.info("parameter python_data shouldn't be None")
        except Exception as e:
            LOGGER.exception(e)
            LOGGER.info("exception occurred, reason-->{}".format(e))

    def is_json(self, raw_data):
        """
        check string whether if json format
        :param json_str:
        :return: True/False
        """
        if isinstance(raw_data, str):
            try:
                json.loads(raw_data)
            except Exception as e:
                LOGGER.exception(e)
                return False
            return True
        else:
            return False

    def get_value_from_json(self, json_data=None, json_key=None, list_index=None):
        """
        get value according to jsonpath from json
        :param list_index: list data index
        :param json_data: json data
        :param json_key: json_key
        :return:  value, if not found return -1
        """
        try:
            json_path = '$..' + json_key
            python_data = self.json_loads(json_data)
            if list_index is None:
                value_list = jsonpath(python_data, json_path)
                if isinstance(value_list, list):
                    if len(value_list) == 1:
                        value_list_return = value_list[0]
                        return value_list_return
                    else:
                        return value_list
                return -1
            else:
                value_path = parse(json_path)
                value_return = value_path.find(python_data)[list_index].value
                return value_return
        except Exception as e:
            LOGGER.exception(e)
            LOGGER.info("exception occurred, please check jsonpath or list index if correct!")
            return -1

    def get_value_from_jsonfile(self, json_file=None, json_key=None, list_index=None):
        """
        get value according to jsonpath
        :param list_index: list data index
        :param json_file: file including json data
        :param json_key: json_key
        :return:  value, if not found return -1
        """
        try:
            json_path = '$..' + json_key
            python_data = self.read_json_file(json_file)
            if list_index is None:
                value_list = jsonpath(python_data, json_path)
                if isinstance(value_list, list):
                    if len(value_list) == 1:
                        value_list_return = value_list[0]
                        return value_list_return
                    else:
                        return value_list
                return -1
            else:
                value_path = parse(json_path)
                value_return = value_path.find(python_data)[list_index].value
                return value_return
        except Exception as e:
            LOGGER.exception(e)
            LOGGER.info("exception occurred, please check jsonpath or list index if correct!")
            return -1

    def get_value_from_jsonfile_parameter(self, json_file=None, json_key=None, list_index=None, parameter_dict=None):
        """
        :param parameter_dict: parameters and values to be replaced, like {'${host}': '127.0.0.1'}
        :param list_index: list data index
        :param json_file: file including json data
        :param json_key: json_key
        :return: value, otherwise return -1
        """
        template_value = self.get_value_from_jsonfile(json_file, json_key, list_index)
        value_origin = Template(template_value)
        if parameter_dict is not None:
            value_return = value_origin.safe_substitute(parameter_dict)
            return value_return
        else:
            LOGGER.info("please provide the parameter_dict!")
            return -1

    def get_value_from_jsonfile_key(self, json_file=None, json_key=None, list_index=None, key_dict=None):
        """
        according to unique key:value get value
        :param list_index: list data index
        :param key_dict: key and value dict
        :param json_file: file including json data
        :param json_key: json_key
        :return: value, otherwise return -1
        """
        try:
            value_list = self.get_value_from_jsonfile(json_file, json_key, list_index)
            index_key = ''.join(str(i) for i in list(key_dict.keys()))
            index_value = ''.join(str(i) for i in list(key_dict.values()))
            index_value_list = self.get_value_from_jsonfile(json_file, index_key)
            index_number = 0
            for i in range(len(index_value_list)):
                if index_value_list[i] == index_value:
                    index_number = i
            return value_list[index_number]
        except Exception as e:
            LOGGER.exception(e)
            LOGGER.info("exception occurred, please check jsonpath or list index if correct!")
            return -1


