from unittest.mock import Mock
from jrPyCore.jrLogger import JrLogger
from jrPyCore.jrMail import JrMail

my_logger = JrLogger(__name__, conffile='../jrLogger.yml').get()
try:
    myMail = JrMail('../.jrNetrc')
    myMail.server = Mock()

    myMail.send('Test', 'JrMail Test von Testmodule')
except:
    my_logger.exception('Unknown Error')
    raise
