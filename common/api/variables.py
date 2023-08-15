from common.base import logger

param_variables = {}


def set_value(key, value):
    param_variables[key] = value


def get_value(key):
    try:
        return param_variables[key]
    except Exception as e:
        logger.error("key error:{}".format(e))
        return None


def get_items():
    return param_variables
