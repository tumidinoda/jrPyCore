import logging
import netrc
import smtplib
from email.mime.text import MIMEText


class JrMail:
    # -----------------------------------------------------------------------------------------------------
    def __init__(self, netrc_key='Mailprovider'):
        self.myLogger = logging.getLogger('jrWetterstationLogger')
        self.myLogger.debug('Mail constructor')

        self.__mail_from = 'SeyringWetter@a1.net'
        self.__mail_to = 'robert.jonas@gmx.at'
        secrets = netrc.netrc('.myNetrc')
        self.__mail_user, self.__smtp_server, self.__mail_pw = secrets.authenticators(netrc_key)

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


# ---------------------------------------------------------------------------------------------------------
def main():
    # test subject only mail
    my_mail = JrMail()
    my_mail.send('Testsubject')
    # test subject and content mail
    my_mail.send("Testsubject 2", "Testcontent")
    print('JRmail() Tests finished')


# ---------------------------------------------------------------------------------------------------------
__name__ == '__main__' and main()
