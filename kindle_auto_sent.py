import email, smtplib, ssl
import os
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

print("This program does not support polish characters in file's name.")
if not os.path.exists('files_to_sent'):
    os.mkdir('files_to_sent')
    print("Directory " , 'files_to_sent' ,  " Created ")

if not os.path.exists('sended'):
    os.mkdir('sended')
    print("Directory " , 'sended' ,  " Created ")

sender_email = 'type your email here'
receiver_email = 'type your kindle mail here'

password = 'type password to your email'



'''
    For the given path, get the List of all files in the directory tree 
'''
from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir('files_to_sent') if isfile(join('files_to_sent', f))]



print(onlyfiles)

files = []

for file in onlyfiles:
    # Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email

    # Open PDF file in binary mode
    with open('files_to_sent/{}'.format(file), "rb") as attachment:
        # Add file as application/octet-stream
        # Email client can usually download this automatically as attachment
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    # Encode file in ASCII characters to send by email
    encoders.encode_base64(part)

    # Add header as key/value pair to attachment part
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {file}",
    )

    # Add attachment to message and convert message to string
    message.attach(part)
    text = message.as_string()

    # Log in to server using secure context and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, text)

    os.replace('files_to_sent/{}'.format(file), 'sended/{}'.format(file))

    
print('Files send.')
time.sleep(10)
