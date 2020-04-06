import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import credentials_list
import fbchat

def wyslij_maila(receiver_address, subject, mail_content, credentials):


    # The mail addresses and password
    # Setup the MIME
    message = MIMEMultipart()
    message['From'] = credentials.sender_address
    message['To'] = receiver_address
    message['Subject'] = subject  # The subject line
    # The body and the attachments for the mail
    message.attach(MIMEText(mail_content, 'plain'))
    # Create SMTP session for sending the mail
    session = smtplib.SMTP(credentials.smtp_adress, credentials.smtp_port)  # use gmail with port
    session.starttls()  # enable security
    session.login(credentials.sender_address, credentials.sender_pass)  # login with mail_id and password
    text = message.as_string()
    session.sendmail(credentials.sender_address, receiver_address, text)
    session.quit()
    print('Mail Sent')

def wyslij_facebook(receiver_ids, message_content, credentials):
    client = fbchat.Client(credentials.fbuser, credentials.fbpass)
    #friends = client.searchForUsers(name)  # return a list of names
    #friend = friends[0]
    for id in receiver_ids:
        print(id.split(':')[0])
        sent = client.sendMessage(message_content, thread_id=id.split(':')[0])
        if sent:
            print("Message sent successfully!")
        time.sleep(2)



f = open("message.txt", "r", encoding="utf-8")
message_from_file = f.read()
f.close()

emails = open("emails.txt", "r", encoding="utf-8")
for adress in emails:
    print(adress.rstrip())
    wyslij_maila(adress.rstrip(),'Raport z mojej produkcji przyłbic dla służb',message_from_file,credentials_list)
emails.close()

facebook_ids = open("facebook_profiles.txt", "r", encoding="utf-8")
wyslij_facebook(facebook_ids, message_from_file, credentials_list)
facebook_ids.close()