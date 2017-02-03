import logging.config
import os
import sys

import yaml


# ---------------------------------------------------------------------------------------------------------
class JrLogger:
    # -----------------------------------------------------------------------------------------------------
    def __init__(self,
                 level=logging.INFO,
                 logfile='jrLogger.yml',
                 env_key='LOG_CFG'
                 ):
        __my_logfile = os.getenv(env_key, None)
        if not __my_logfile:
            __my_logfile = logfile
        if os.path.exists(__my_logfile):
            try
                with open(__my_logfile, 'rt') as f:
                    __config = yaml.safe_load(f.read())
                logging.config.dictConfig(__config)
            except (IOError):
                logging.basicConfig(level=level)
        else:
            logging.basicConfig(level=level)

        # look back one level in execution to get calling module name
        # noinspection PyProtectedMember
        __frame = sys._getframe(1)
        module = __frame.f_globals['__name__']
        if module == '__main__':
            # if name='__main__' then create module name out of filename
            file_name = __frame.f_globals['__file__']
            module = os.path.basename(file_name)

        self.__my_logger = logging.getLogger(module)

    # -----------------------------------------------------------------------------------------------------
    def get(self):
        return self.__my_logger


# ---------------------------------------------------------------------------------------------------------
def main():
    # some Test cases
    my_logger = JrLogger(logging.WARNING).get()
    my_logger.debug('Hallo Debug')
    my_logger.info('Hallo Info')
    my_logger.warning('Hallo Warning')
    my_logger.error('Hallo Error')
    logging.critical('Hallo Critical')
    logging.exception('Hallo Error with traceback')
    logging.warning('Hallo Warning')
    logging.info('Hallo Info')


# ---------------------------------------------------------------------------------------------------------
__name__ == '__main__' and main()
