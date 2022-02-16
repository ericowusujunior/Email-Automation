import yagmail
import os
import time

"This was to send a single email"

sender = "e.owusu89@gmail.com"
receiver = "1yr89yqf@spymail.one"

subject = "Automated Trial Email"

content = """Sending email using python"""

while True:

  yag = yagmail.SMTP(user = sender,password = os.getenv('PASSWORD'))

  yag.send(to=receiver, subject = subject, contents = content)
  my_secret = os.environ['PASSWORD']
  print("Email Sent!")
  time.sleep(60)




