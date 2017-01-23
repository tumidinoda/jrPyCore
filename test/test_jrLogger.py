from os import environ
import logging
import unittest
from unittest import TestCase

import jrLogger


# ---------------------------------------------------------------------------------------------------------
class TestJrLogger(TestCase):
    myLogger=jrLogger.JrLogger()

    #logging based on default log-options
    logging.debug('Hallo Debug')
    logging.info('Hallo Info')
    logging.warning('Hallo Warning')
    logging.error('Hallo Error')
    logging.critical('Hallo Critical')
    logging.exception('Hallo Error with traceback')

    #logging based on config file options
    environ['LOG_CFG']='../jrLogger.yaml'
    myLogger.config()
    logging.debug('Hallo Debug')
    logging.info('Hallo Info')
    logging.warning('Hallo Warning')
    logging.error('Hallo Error')
    logging.critical('Hallo Critical')
    logging.exception('Hallo Error with traceback')

# ---------------------------------------------------------------------------------------------------------
__name__ == '__main__' and unittest.main()
