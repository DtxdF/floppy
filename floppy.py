# -*- coding: UTF-8 -*-

import smtplib
from os.path import basename
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

class smtp_interact:

    def __init__(self, email, password, smtp_server, smtp_port):

        self.email = email
        self.password = password
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.multipart = MIMEMultipart()
        self.multipart['from'] = self.email

    def connect(self):

        self.smtp = smtplib.SMTP(self.smtp_server, self.smtp_port)

        try:

            self.smtp.starttls()

        except smtplib.SMTPException:

            pass

    def login(self):

        self.smtp.login(self.email, self.password)

    def add_file(self, reader):

        self.mimebase = MIMEBase('application', 'octet-stream')
        self.mimebase.add_header('Content-Disposition', 'attachment;filename='+basename(reader.name))
        self.mimebase.set_payload(reader.read())
        encoders.encode_base64(self.mimebase)
        self.multipart.attach(self.mimebase)
        reader.close()

    def add_message(self, message):

        self.multipart.attach(MIMEText(message))

    def sendmail(self, to, subject):

        self.multipart['to'] = to
        self.multipart['subject'] = subject
        self.smtp.sendmail(self.email, to, self.multipart.as_string())

    def close(self):

        self.smtp.close()
