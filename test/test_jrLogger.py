import unittest
from os import environ
from unittest import TestCase

from jrPyCore.jrLogger import JrLogger


# ---------------------------------------------------------------------------------------------------------
class TestJrLogger(TestCase):
    # logging based on default log-options
    environ['LOG_CFG'] = ''
    my_logger = JrLogger().setup(__name__)
    my_logger.debug('Hallo Debug')
    my_logger.info('Hallo Info')
    my_logger.warning('Hallo Warning')
    my_logger.error('Hallo Error')
    my_logger.critical('Hallo Critical')
    my_logger.exception('Hallo Error with traceback')

    # logging based on setup file options
    environ['LOG_CFG'] = '../jrLogger.yml'
    my_logger = JrLogger().setup(__name__)
    my_logger.debug('Hallo Debug')
    my_logger.info('Hallo Info')
    my_logger.warning('Hallo Warning')
    my_logger.error('Hallo Error')
    my_logger.critical('Hallo Critical')
    my_logger.exception('Hallo Error with traceback')

    # loop test for cyclic logging
    for i in range(400):
        my_logger.info('Loggin Test line: ' + str(i))


# ---------------------------------------------------------------------------------------------------------
__name__ == '__main__' and unittest.main()
