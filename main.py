import yagmail
import os

"Email With Attachment"

sender = "e.owusu89@gmail.com"
receiver = "e.owusu@dal.ca"

subject = "Automated Trial Email"

content = ["""Sending email using python""", 'attachment.txt']


yag = yagmail.SMTP(user = sender,password = os.getenv('PASSWORD'))

yag.send(to=receiver, subject = subject, contents = content)
my_secret = os.environ['PASSWORD']
print("Email Sent!")




