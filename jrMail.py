import netrc
import smtplib
from email.mime.text import MIMEText

from jrLogger import JrLogger


class JrMail:
    # -----------------------------------------------------------------------------------------------------
    def __init__(self, netrc_path='.jrNetrc', netrc_key='Mailprovider', mail_from='WetterSeyring@a1.net',
                 mail_to='robert.jonas@gmx.at'):
        self.__mail_from = mail_from
        self.__mail_to = mail_to
        try:  # first default .netrc and second local
            secrets = netrc.netrc()
        except (netrc.NetrcParseError, OSError):
            secrets = netrc.netrc(netrc_path)

        self.__mail_user, self.__smtp_server, self.__mail_pw = secrets.authenticators(netrc_key)
        self.__logger = JrLogger().config(__name__)

    # -----------------------------------------------------------------------------------------------------
    def send(self, subject, content=None):
        msg = MIMEText(content, 'plain', 'utf-8')
        msg['From'] = self.__mail_from
        msg['To'] = self.__mail_to
        msg['Subject'] = subject

        # server = smtplib.SMTP_SSL(self.__smtp_server)
        server = smtplib.SMTP(self.__smtp_server)
        server.login(self.__mail_user, self.__mail_pw)
        server.sendmail(self.__mail_from, self.__mail_to, msg.as_string())
        server.quit()
        self.__logger.info('Mail to ' + self.__mail_to + ' sent')


# ---------------------------------------------------------------------------------------------------------
def main():
    my_logger = JrLogger().config(__file__)
    try:
        my_mail = JrMail()
        my_logger.info('JRmail() Tests started')
        # test subject only mail
        my_mail.send('Testsubject')
        # test subject and content mail
        my_mail.send("Testsubject 2", "Testcontent")
        my_logger.info('JRmail() Tests finished')
    except:
        my_logger.exception('Unknown Error')
        raise


# ---------------------------------------------------------------------------------------------------------
__name__ == '__main__' and main()
