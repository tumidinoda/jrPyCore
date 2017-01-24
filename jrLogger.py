import logging.config
import os

import yaml


# ---------------------------------------------------------------------------------------------------------
class JrLogger:
    def config(self,
               module,
               level=logging.INFO,
               file='jrLogger.yaml',
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
        return logging.getLogger(module)


# ---------------------------------------------------------------------------------------------------------
def main():
    # isome Test cases
    myLogger = JrLogger().config('Test jrLogger', logging.WARNING)
    myLogger.debug('Hallo Debug')
    myLogger.info('Hallo Info')
    myLogger.warning('Hallo Warning')
    myLogger.error('Hallo Error')
    logging.critical('Hallo Critical')
    logging.exception('Hallo Error with traceback')
    logging.warning('Hallo Warning')
    logging.info('Hallo Info')


# ---------------------------------------------------------------------------------------------------------
__name__ == '__main__' and main()
