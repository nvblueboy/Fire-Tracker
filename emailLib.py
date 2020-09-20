import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import config


def sendEmail(htmlMessage):
    configObject = config()

    sender_email = configObject.email_sender
    smtp_user = configObject.smtp_user
    smtp_pass = configObject.smtp_pass
    receiver_email = configObject.addresses[0]["address"]

    message = MIMEMultipart("alternative")
    message["Subject"] = "Fire Update"
    message["From"] = sender_email
    message["To"] = receiver_email
    part1 = MIMEText(htmlMessage, "html")

    message.attach(part1)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(configObject.smtp_server, 465, context=context) as server:
        server.login(smtp_user, smtp_pass)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )


if __name__ == "__main__":
    sendEmail("<b>Test Email</b>")