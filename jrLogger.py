import logging.config
import os

import yaml


# ---------------------------------------------------------------------------------------------------------
def config(file='jrLogger.yaml',
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
    # initialize logging
    config()
    myLogger = logging.getLogger(__name__)
    myLogger.debug('Hallo Debug')
    myLogger.info('Hallo Info')
    myLogger.warning('Hallo Warning')
    myLogger.error('Hallo Error')
    logging.critical('Hallo Critical')
    logging.exception('Hallo Error with traceback')


# ---------------------------------------------------------------------------------------------------------
__name__ == '__main__' and main()
