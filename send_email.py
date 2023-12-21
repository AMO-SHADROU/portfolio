import smtplib
import ssl
import os


def send_email(user_massage):
    host = 'smtp.gmail.com'
    port = 465
    gmail = "amirali.shadrou@gmail.com"
    password = os.getenv("PASSWORD")
    receiver = "dr.shadrou@gmail.com"
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(gmail, password)
        server.sendmail(gmail, receiver, user_massage)
