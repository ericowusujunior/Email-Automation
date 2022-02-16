import yagmail
import os

sender = "e.owusu89@gmail.com"
receiver = "e.owusu@dal.ca"

subject = "Automated Trial Email"

content = """" I am writing this email to see how it goes"""

yag = yagmail.SMTP(user = sender,password = os.getenv('PASSWORD'))

yag.send(to=receiver, subject = subject, contents = content)

print("Email Sent!")
my_secret = os.environ['PASSWORD']
