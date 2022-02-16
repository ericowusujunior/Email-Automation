import yagmail
import os
import time
from datetime import datetime 

"This sends an email to the receiver everyday at 1:50"

sender = "e.owusu89@gmail.com"
receiver = "1yr89yqf@spymail.one"

subject = "Automated Trial Email"

content = """Sending email using python"""

while True:
  now = datetime.now()
  if now.hour == 1 and now.minute == 55:
    yag = yagmail.SMTP(user = sender,password = os.getenv('PASSWORD'))

    yag.send(to=receiver, subject = subject, contents = content)
    my_secret = os.environ['PASSWORD']
    print("Email Sent!")
    time.sleep(60)




