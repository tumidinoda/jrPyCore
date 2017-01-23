import logging
import unittest
from os import environ
from unittest import TestCase

import jrLogger

# initialize logging
jrLogger.config()
myLogger = logging.getLogger(__name__)


# ---------------------------------------------------------------------------------------------------------
class TestJrLogger(TestCase):

    # logging based on default log-options
    environ['LOG_CFG'] = ''
    jrLogger.config()
    logging.debug('Hallo Debug')
    logging.info('Hallo Info')
    myLogger.warning('Hallo Warning')
    myLogger.error('Hallo Error')
    myLogger.critical('Hallo Critical')
    myLogger.exception('Hallo Error with traceback')


    # logging based on config file options
    environ['LOG_CFG'] = '../jrLogger.yaml'
    jrLogger.config()
    myLogger.debug('Hallo Debug')
    myLogger.info('Hallo Info')
    myLogger.warning('Hallo Warning')
    myLogger.error('Hallo Error')
    myLogger.critical('Hallo Critical')
    myLogger.exception('Hallo Error with traceback')


# ---------------------------------------------------------------------------------------------------------
__name__ == '__main__' and unittest.main()
