import smtplib
from email.message import EmailMessage
import sys

# ─── CONFIGURE THESE ─────────────────────────────
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT   = 465          # 465 (SSL) or 587 (TLS)
USERNAME    = "your_email@gmail.com"
PASSWORD    = "your_password"
TO_ADDRESS  = "reciever_address@mail.com"
# ─────────────────────────────────────────────────

def send_cleaning_alert(days):
    msg = EmailMessage()
    msg["Subject"] = f"🔔 Solar Panel Cleaning in {days} Day(s)"
    msg["From"]    = USERNAME
    msg["To"]      = TO_ADDRESS
    msg.set_content(f"""\
Hello,

Your solar panels need cleaning in {days} day(s).
Please schedule maintenance.

Best,
Solar Monitor Bot
""")
    # Connect & send
    with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as smtp:
        smtp.login(USERNAME, PASSWORD)
        smtp.send_message(msg)
    print(f"Email sent: cleaning in {days} day(s)")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: send_email.py <days>")
        sys.exit(1)
    days = sys.argv[1]
    send_cleaning_alert(days)