import smtplib

def send_email(receiver, message):

    server = smtplib.SMTP(
        'smtp.gmail.com',
        587
    )

    server.starttls()

    server.login(
        "yourmail@gmail.com",
        "password"
    )

    server.sendmail(
        "yourmail@gmail.com",
        receiver,
        message
    )

    server.quit()