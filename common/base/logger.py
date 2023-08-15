import logging
import sys
from logging import handlers
from common.base.path import Base_path


class LogFileOperation(object):
    level_relations = {
        'debug': logging.DEBUG,
        'info': logging.INFO,
        'warning': logging.WARNING,
        'error': logging.ERROR,
        'critical': logging.CRITICAL
    }  # Log level relationship mapping

    def __init__(self, filename="{}/test_results/logs/all.log".format(Base_path), level='info', when='D', interval=1,
                 back_count=3,
                 fmt='%(asctime)s - [%(filename)s-->line:%(lineno)d] - %(levelname)s: %(message)s'):
        self.logger = logging.getLogger(filename)
        format_str = logging.Formatter(fmt)  # set log format
        self.logger.setLevel(self.level_relations.get(level))  # set log level
        sh = logging.StreamHandler(stream=sys.stdout)  # Output on the screen
        sh.setFormatter(format_str)  # Set format is displayed on the screen
        if not self.logger.handlers:
            fh = handlers.TimedRotatingFileHandler(filename=filename, when=when, backupCount=back_count,
                                                   interval=interval,
                                                   encoding='utf-8')  # Write into the file specified time interval

            # Instance TimedRotatingFileHandler
            # interval: time interval，backupCount: backed file number，If exceed，it will delete automatically.
            # S: second
            # M: minute
            # H: hour
            # D: day
            # W: week（interval==0, Monday）
            # midnight: every morning
            fh.setFormatter(format_str)  # Set file format
            self.logger.addHandler(sh)
            self.logger.addHandler(fh)


if __name__ == '__main__':
    log = LogFileOperation().logger
    log.info('info')
