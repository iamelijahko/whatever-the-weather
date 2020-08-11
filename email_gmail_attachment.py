import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# define the SMTP server:
port = 587
smtp_server = "smtp.gmail.com"
sender_email = "iamelijahko@gmail.com"
receiver_email = "elijah.ko@network.rca.ac.uk"
password = "hkgnyqtgytcpdwpo"

message = MIMEMultipart()
message["Subject"] = "Python: Sending Email Testing"
message["From"] = sender_email
message["To"] = receiver_email

# Add body to email
body = "This is an example of how you can send a pdf in attachment with Python"
message.attach(MIMEText(body, "plain"))

filename = "strange_weather_science_gallery.pdf"
# Open PDF file in binary mode
# We assume that the file is in the directory where you run your Python script from
with open(filename, "rb") as attachment:
    # The content type "application/octet-stream" means that a MIME attachment is a binary file
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())

# Encode to base64
encoders.encode_base64(part)

# Add header
part.add_header(
    "Content-Disposition",
    f"attachment; filename= {filename}",
)

# Add attachment to your message and convert it to string
message.attach(part)  # To attach several files, you can call the message.attach() method several times.
text = message.as_string()

smtplibObj = smtplib.SMTP(smtp_server, port)  # 587 for STARTTLS connection. 465 for SSL/TLS connection
smtplibObj.ehlo()  # say hello to the gmail server
smtplibObj.starttls()  # in case a problem occurs
smtplibObj.login(sender_email, password)
smtplibObj.sendmail(sender_email, receiver_email, text)
smtplibObj.quit()
print('Sent')
