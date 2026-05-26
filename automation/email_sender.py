import smtplib
from email.mime.text import MIMEText

sender = "your_email@gmail.com"
password = "your_password"
receiver = "client@example.com"

msg = MIMEText("Automation completed successfully")
msg["Subject"] = "Automation Status"
msg["From"] = sender
msg["To"] = receiver

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    server.login(sender, password)
    server.sendmail(sender, receiver, msg.as_string())