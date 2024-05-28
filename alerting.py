#Integrate alerting using email or messaging systems like Slack.
import smtplib
from email.mime.text import MIMEText

def send_alert(message):
    msg = MIMEText(message)
    msg['Subject'] = 'Suspicious Activity Detected'
    msg['From'] = 'admin@company.com'
    msg['To'] = 'security@company.com'

    with smtplib.SMTP('smtp.company.com') as server:
        server.login('user', 'password')
        server.sendmail(msg['From'], [msg['To']], msg.as_string())

send_alert("Suspicious file access detected on workstation 1")

