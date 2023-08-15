from common.base import logger
import json


class JsonCompare:

    def compare(self, expect, actual):
        expect = self._convert_format(expect)
        actual = self._convert_format(actual)
        difference = []
        self._compare(expect, actual, difference, '')
        return difference

    def _convert_format(self, input_data):
        try:
            if isinstance(input_data, str):
                return json.loads(input_data)
            else:
                return input_data
        except Exception as e:
            logger.exception(e)
            logger.info("exception occurred, reason-->{}".format(e))

    def _compare(self, expected_data, actual_data, diff_data, path):
        if type(expected_data) != type(actual_data):
            diff_data.append(f"{path} 类型不一致,{expected_data} != {actual_data},期望值为{type(expected_data)} 实际值为{type(actual_data)}")
            # return
        if isinstance(expected_data, dict):
            keys = []
            for key in expected_data.keys():
                pt = path + "/" + key
                if isinstance(actual_data, dict):
                    if key in actual_data.keys():
                        self._compare(expected_data[key], actual_data[key], diff_data, pt)
                        keys.append(key)
                    else:
                        diff_data.append(f"{pt} 在实际值中不存在")
                else:
                    diff_data.append(f"{pt} 在实际值中不存在")
            if isinstance(actual_data, dict):
                for key in actual_data.keys():
                    if key not in keys:
                        pt = path + "/" + key
                        diff_data.append(f"{pt} 在实际值中多出")
        elif isinstance(expected_data, list):
            i = j = 0
            while i < len(expected_data):
                pt = path + "/" + str(i)
                if j >= len(actual_data):
                    diff_data.append(f"{pt} 在实际值中不存在")
                    i += 1
                    j += 1
                    continue
                self._compare(expected_data[i], actual_data[j], diff_data, pt)
                i += 1
                j += 1
            while j < len(actual_data):
                pt = path + "/" + str(j)
                diff_data.append(f"{pt} 在实际值中多出")
                j += 1
        else:
            if expected_data != actual_data and type(expected_data) == type(actual_data):
                if path != "":
                    diff_data.append(f"{path} 数据不一致: {expected_data} != {actual_data}")
                else:
                    diff_data.append(f"数据不一致: {expected_data} != {actual_data}")