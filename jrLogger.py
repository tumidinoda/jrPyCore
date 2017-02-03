import logging.config
import os
import sys

import yaml


# ---------------------------------------------------------------------------------------------------------
class JrLogger:
    def setup(self,
              module,
              level=logging.INFO,
              file='jrLogger.yml',
              env_key='LOG_CFG'
              ):
        env_file = os.getenv(env_key, None)
        if env_file:
            file = env_file
        if os.path.exists(file):
            with open(file, 'rt') as f:
                config = yaml.safe_load(f.read())
            logging.config.dictConfig(config)
        else:
            logging.basicConfig(level=level)

        # lock back one level in execution to get calling module name
        frame = sys._getframe(1)
        module = frame.f_globals['__name__']
        if module == '__main__':
            # if name='__main__' then create module name out of filename
            file_name = frame.f_globals['__file__']
            module = os.path.basename(file_name)

        return logging.getLogger(module)


# ---------------------------------------------------------------------------------------------------------
def main():
    # some Test cases
    #    my_logger = JrLogger().setup('Test jrLogger', logging.WARNING)
    my_logger = JrLogger().setup(__name__, logging.WARNING)
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
