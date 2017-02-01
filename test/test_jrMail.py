from jrPyCore.jrLogger import JrLogger
from jrPyCore.jrMail import JrMail

my_logger = JrLogger().setup(__name__, file='../jrLogger.yml')
try:
    myMail = JrMail('../.jrNetrc')
    myMail.send('Test', 'JrMail Test von Testmodule')
except:
    my_logger.exception('Unknown Error')
    raise
