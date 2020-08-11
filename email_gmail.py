import smtplib

port = 587
smtp_server = "smtp.gmail.com"
sender_email = "iamelijahko@gmail.com"
receiver_email = "elijah.ko@network.rca.ac.uk"
password = "hkgnyqtgytcpdwpo"
text = "Subject: Python: Sending Email Testing\nTesting 01"

smtplibObj = smtplib.SMTP(smtp_server, port)  # 587 for STARTTLS connection. 465 for SSL/TLS connection
smtplibObj.ehlo()  # say hello to the gmail server
smtplibObj.starttls()  # in case a problem occurs
smtplibObj.login(sender_email, password)
smtplibObj.sendmail(sender_email, receiver_email, text)
smtplibObj.quit()
