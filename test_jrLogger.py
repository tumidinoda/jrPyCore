import logging
import unittest
from os import environ
from unittest import TestCase

from jrPyCore.jrLogger import JrLogger


# ---------------------------------------------------------------------------------------------------------
class TestJrLogger(TestCase):
    # logging based on default log-options
    environ['LOG_CFG'] = ''
    myLogger = JrLogger().config(__name__)
    myLogger.debug('Hallo Debug')
    myLogger.info('Hallo Info')
    myLogger.warning('Hallo Warning')
    myLogger.error('Hallo Error')
    myLogger.critical('Hallo Critical')
    myLogger.exception('Hallo Error with traceback')

    # logging based on config file options
    environ['LOG_CFG'] = '../jrLogger.yaml'
    myLogger = JrLogger().config(__name__)
    myLogger.debug('Hallo Debug')
    myLogger.info('Hallo Info')
    myLogger.warning('Hallo Warning')
    myLogger.error('Hallo Error')
    myLogger.critical('Hallo Critical')
    myLogger.exception('Hallo Error with traceback')

    #loop test for cyclic logging
    for i in range(400):
        myLogger.info('Loggin Test line: '+str(i))


# ---------------------------------------------------------------------------------------------------------
__name__ == '__main__' and unittest.main()
