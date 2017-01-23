import logging.config
import os

import yaml


# ---------------------------------------------------------------------------------------------------------
class JrLogger:
    def __init__(self,
                 file='jrLogger.yaml',
                 level=logging.INFO,
                 env_key='LOG_CFG'
                 ):
        self.config(file, level, env_key)

    # -----------------------------------------------------------------------------------------------------
    def config(self,
               file='jrLogger.yaml',
               level=logging.INFO,
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


# ---------------------------------------------------------------------------------------------------------
def main():
    JrLogger()

    #   logger = logging.getLogger(__name__)
    logging.debug('Hallo Debug')
    logging.info('Hallo Info')
    logging.warning('Hallo Warning')
    logging.error('Hallo Error')
    logging.critical('Hallo Critical')
    logging.exception('Hallo Error with traceback')


# ---------------------------------------------------------------------------------------------------------
__name__ == '__main__' and main()
