from configparser import ConfigParser
from common.base.path import conf_dir
import os

class Config(ConfigParser):
    def __init__(self, filename, encoding='utf-8'):
        super().__init__()
        self.read(filename, encoding=encoding)
        self.filename = filename
        self.encoding = encoding

    def write_data(self, select, option, value):
        """
        Input data in the config
        :param select:
        :param option:
        :param value:
        :return:
        """
        self.set(select, option, value)
        self.write(fp=open(self.filename, "w", encoding=self.encoding))


# Create a ConfigParser
conf = Config(os.path.join(conf_dir, "config.ini"))
