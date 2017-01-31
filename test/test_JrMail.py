from jrLogger import JrLogger
from jrMail import JrMail

my_logger = JrLogger().config(__name__,file='../jrLogger.yaml')
try:
    myMail = JrMail('../.jrNetrc')
    myMail.send('Test', 'JrMail Test von Testmodule')
except:
    my_logger.exception('Unknown Error')
    raise
