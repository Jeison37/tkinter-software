from credentials import user_email, user_email_password

from email.message import EmailMessage
import smtplib
import ssl

def send_email(recept_email,name):
  email_password = user_email_password
  email_receiver = recept_email

  subject = "Your information has been saved succesfully"
  body = "Hello " + name

  em = EmailMessage()
  em["From"] = user_email
  em["to"] = email_receiver
  em["Subject"] = subject
  em.set_content(body)

  context = ssl.create_default_context()

  with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
    smtp.login(user_email, email_password)
    smtp.sendmail(user_email, email_receiver, em.as_string())