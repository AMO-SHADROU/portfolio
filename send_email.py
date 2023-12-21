import smtplib
import ssl


def send_email(user_massage):
    host = 'smtp.gmail.com'
    port = 465
    gmail = "amirali.shadrou@gmail.com"
    password = "gmxfzhfxuogtonoq"
    receiver = "dr.shadrou@gmail.com"
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(gmail, password)
        server.sendmail(gmail, receiver, user_massage)
