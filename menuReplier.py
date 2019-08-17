#!/usr/bin/python3

import imaplib
import email
import smtplib, ssl
import getpass
from multiprocessing import Pool


mail = imaplib.IMAP4_SSL('imap.gmail.com')

# print(getpass.getpass(prompt='yo password b'))

mail.login('', "")
mail.select('INBOX')
status, response = mail.search(None, '(UNSEEN)')
unread_msg_nums = response[0].split()

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = ""
password = ''

 

def sendMessage(message, recipients):
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, recipients, message)

 

# Print the count of all unread messages
print (len(unread_msg_nums))
unread_msg_nums = response[0].split()

da = []

for e_id in unread_msg_nums:
    _, response = mail.fetch(e_id, '(RFC822)')
    da.append(email.message_from_string(response[0][1].decode('utf-8')))



m = {}

for email_message in da:
    sender = email_message['from']
    for part in email_message.walk():
        # this part comes from the snipped I don't understand yet...
        if part.get_content_maintype() == 'multipart':
            continue
        #if part.get('Content-Disposition') is None:
            #continue
        fileName = part.get_filename()
        m[sender] = (part.get_payload(decode=True).decode('utf-8')).rstrip()

print(m)

for entity in m.keys():
    if m[entity] == '69':
        sendMessage("Heh niiiiiiiiiiiiiiiiiiiiiiiiiiiiice", entity)
