import os
import smtplib
import imghdr
import csv
import pandas as pd
from email.message import EmailMessage


EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

contacts = [''] # enter the list of email id you want to send and

msg = EmailMessage()
msg['Subject'] = "Checkout the image"
msg['From'] = EMAIL_ADDRESS
msg['To'] = contacts
# or can use the below format to attach multiple eamil address
#msg['To'] = ','.join(contacts)
#
# code for attachments
#msg.set_content("PFA the image for trial basis"
# files = [''] #list for adding the location of the attachment on the local PC or on the web
#
# for file in files:
#     with open(file,'rb') as f:
#         file_data = f.read()
#         file_type = imghdr.what(f.name)
#         file_name = f.name
#
#     msg.add_attachment(file_data, maintype = 'image', subtype=file_type, filename = file_name)


msg.set_content('This is a plain text email')
msg.add_alternative(
"""
<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title></title>
  </head>
  <body>
      <h1 style="color:pink;">This is a simple html for mail purpose</h1>
  </body>
</html>

""", subtype='html')


with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)
