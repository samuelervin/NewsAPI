import smtplib, ssl,os

def send_mail(sender, subject, message):
    """Sends an email from the specified email address.

    Args:
        sender (_type_): _description_
        subject (_type_): _description_
        message (_type_): _description_
    """
    host = "smtp.gmail.com"
    port = 465 
    username = "samuel.ervin@gmail.com"
    password = "pmly bkvc pgft vrjj"
    my_context = ssl.create_default_context()
    #may get ascii error if so encode message to utf-8 message.encode('utf-8')
    final_message = f"Subject: {subject}\n\n From: {sender}\n\n {message}"

    with smtplib.SMTP_SSL(host, port, context=my_context) as server:
        server.login(username, password)
        server.sendmail(sender, username, final_message)
