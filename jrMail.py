import netrc
import smtplib
from email.mime.text import MIMEText

from jrPyCore.jrLogger import JrLogger


class JrMail:
    # -----------------------------------------------------------------------------------------------------
    def __init__(self, netrc_key='Mailprovider'):
        self.__mail_from = 'WetterSeyring@a1.net'
        self.__mail_to = 'robert.jonas@gmx.at'
        secrets = netrc.netrc('.myNetrc')
        self.__mail_user, self.__smtp_server, self.__mail_pw = secrets.authenticators(netrc_key)
        self.logger = JrLogger().config(__name__)

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
        self.logger.info('Mail to ' + self.__mail_to + ' sent')


# ---------------------------------------------------------------------------------------------------------
def main():
    # test subject only mail
    my_mail = JrMail()
    my_mail.send('Testsubject')
    # test subject and content mail
    my_mail.send("Testsubject 2", "Testcontent")
    my_mail.logger.info('JRmail() Tests finished')


# ---------------------------------------------------------------------------------------------------------
__name__ == '__main__' and main()
