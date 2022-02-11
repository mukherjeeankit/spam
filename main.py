import smtplib, ssl
import random

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "mukherjeeankit2001@gmail.com"
receiver_email = input("What's the to-be-spammed's address?\n")
password = "kingofmemes2021"

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    while True:
        server.sendmail(sender_email, receiver_email, str(random.choice(list(range(0, 1000)))))